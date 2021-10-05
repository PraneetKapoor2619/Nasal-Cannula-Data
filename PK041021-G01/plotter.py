import numpy as np
import matplotlib.pyplot as plt
import re

flag = 1

def read_file(extension):
	fp = open(extension + "data.txt", 'r')
	t = np.array([])
	timestamps = np.array([])
	r_f = np.array([])
	SFM = np.array([])
	DP = np.array([])
	SDP = np.array([])
	k = np.array([])
	'''
	Format of a single data line is:
	[time in seconds] [r-F] [SFM] [DP] [PREDICTION/SDP] [k]
			0			1	  2     3		   4         5
	'''
	target_flags = -1
	for line in fp:
		extr = re.findall("[0-9.]+", line)
		try:
			if(len(extr) == 6):
				print(extr)
				if(float(extr[1]) != target_flags):
					timestamps = np.append(timestamps, float(extr[0]))
					target_flags = float(extr[1])
				t = np.append(t, float(extr[0]))
				r_f = np.append(r_f, float(extr[1]))
				SFM = np.append(SFM, float(extr[2]))
				DP = np.append(DP, float(extr[3]))
				SDP = np.append(SDP, float(extr[4]))
				k = np.append(k, float(extr[5]))
		except:
			continue
	return t, timestamps, r_f, SFM, DP, SDP, k

def plot(x, y, timestamps, xlabel, ylabel, title, extension):
	global flag
	plt.figure(flag)
	plt.plot(x, y, "k.")
	if(len(timestamps) > 0):
		for t in timestamps:
			plt.axvline(t, color ='r')
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.savefig(extension + title + ".png")
	flag += 1
	return 0

if __name__ == "__main__":
	extension = "D:\\KYRON\\Code\\sdp_sfm_comparison\\DATA\\Nasal Canula Data\\PK041021-G01\\Red\\"
	print("EXTENSION: " + extension)
	ch = input("")
	t, timestamps, r_f, SFM, DP, SDP, k = read_file(extension)
	print(t)
	print(SFM)
	plot(t, SFM, timestamps, "Time in sec", "Flow through SFM", "SFM vs Time", extension)
	plot(t, DP, timestamps, "Time in sec", "Differential Pressure", "Differential Pressure vs Time", extension)
	plot(t, SDP, timestamps, "Time in sec", "Prediction of flow", "Variation in prediction of flow with time and targets", extension)
	plot(t, k, timestamps, "Time in sec", "PWM (0 - 255)", "Variation in PWM with time and different targets", extension)
	plot(r_f, SFM, [], "Target", "Flow through SFM", "SFM vs Target", extension)
	plot(r_f, SDP, [], "Target", "Prediction of flow", "Variation in prediction of flow with targets", extension)
	plot(r_f, k, [], "Target", "PWM (0 - 255)", "Variation in PWM with different targets", extension)
	plt.show()