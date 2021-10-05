import numpy as np
import matplotlib.pyplot as plt
import re

flag = 1
subplot_num = 231

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
				#print(extr)
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
	print("\aDone")
	return t, timestamps, r_f, SFM, DP, SDP, k

def plot(x, y, timestamps, xlabel, ylabel, title, extension):
	global flag, subplot_num
	plt.figure(title)
	plt.subplot(subplot_num)
	plt.plot(x, y, "k.")
	if(len(timestamps) > 0):
		for t in timestamps:
			plt.axvline(t, color ='r')
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	if(subplot_num == 231):
		name = "SFM"
	elif(subplot_num == 232):
		name = "SFM + 30 cm tube"
	elif(subplot_num == 233):
		name = "SFM + 30 cm tube + #00"
	elif(subplot_num == 234):
		name = "SFM + 30 cm tube + #0"
	elif(subplot_num == 235):
		name = "SFM + 30 cm tube + #1"
	elif(subplot_num == 236):
		name = "SFM + 30 cm tube + #2"
	plt.title(name)
	flag += 1
	if(subplot_num == 236):
		plot_backend = plt.get_backend()
		mng = plt.get_current_fig_manager()
		if plot_backend == 'TkAgg':
			mng.resize(*mng.window.maxsize())
		elif plot_backend == 'wxAgg':
			mng.frame.Maximize(True)
		elif plot_backend == 'Qt4Agg':
			mng.window.showMaximized()
		fig = plt.gcf()
		fig.set_size_inches(32, 18)
		fig.subplots_adjust(wspace=0.455, 
						hspace=0.455)
		fig.show()
		fig.savefig("D:\\KYRON\\Code\\DATA\\Nasal Cannula Data\\PK041021-G01\\REPORT\\" + title + ".png", dpi = 500)
	return 0

def manager(extension):
	global flag, subplot_num
	print(extension)
	t, timestamps, r_f, SFM, DP, SDP, k = read_file(extension)
	
	plot(t, SFM, timestamps, "Time in sec", "Flow through SFM", "SFM vs Time", extension)
	plot(t, DP, timestamps, "Time in sec", "Differential Pressure", "Differential Pressure vs Time", extension)
	plot(t, SDP, timestamps, "Time in sec", "Prediction of flow", "Variation in prediction of flow with time and targets", extension)
	plot(t, k, timestamps, "Time in sec", "PWM (0 - 255)", "Variation in PWM with time and different targets", extension)
	plot(r_f, SFM, [], "Target", "Flow through SFM", "SFM vs Target", extension)
	plot(r_f, SDP, [], "Target", "Prediction of flow", "Variation in prediction of flow with targets", extension)
	plot(r_f, k, [], "Target", "PWM (0 - 255)", "Variation in PWM with different targets", extension)
	flag = 1
	subplot_num += 1
	return 0

if __name__ == "__main__":
	extension = "D:\\KYRON\\Code\\DATA\\Nasal Cannula Data\\PK041021-G01\\"
	'''
	1. extract data from a particular text file
	2. plot in figures consisting of subplots 
	3. update the subplot number (for the next data)
	4. reset the global figure flag back to 1.
	5. change the directory
	6. Go to step 1
	'''
	manager(extension + "Without tube\\")
	manager(extension + "With tube\\")
	manager(extension + "00\\")
	manager(extension + "0\\")
	manager(extension + "1\\")
	manager(extension + "2\\")