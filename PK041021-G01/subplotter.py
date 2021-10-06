import numpy as np
import matplotlib.pyplot as plt
import re
import os

flag = 1
subplot_num = int()
base_subplot_num = int()
till = int()

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
	global flag, subplot_num, base_subplot_num, till
	plt.figure(title)
	plt.subplot(subplot_num)
	plt.plot(x, y, "k.")
	if(len(timestamps) > 0):
		for t in timestamps:
			plt.axvline(t, color ='r')
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	name = str()
	if(base_subplot_num == 231):
		if(subplot_num == base_subplot_num):
			name = "SFM"
		elif(subplot_num == base_subplot_num + 1):
			name = "SFM + 30 cm tube"
		elif(subplot_num == base_subplot_num + 2):
			name = "SFM + 30 cm tube + #00"
		elif(subplot_num == base_subplot_num + 3):
			name = "SFM + 30 cm tube + #0"
		elif(subplot_num == base_subplot_num + 4):
			name = "SFM + 30 cm tube + #1"
		elif(subplot_num == base_subplot_num + 5):
			name = "SFM + 30 cm tube + #2"
	elif(base_subplot_num == 311):
		if(subplot_num == base_subplot_num):
			name = "SFM + 30 cm tube + Green Cannula"
		elif(subplot_num == base_subplot_num + 1):
			name = "SFM + 30 cm tube + Orange Cannula"
		elif(subplot_num == base_subplot_num + 2):
			name = "SFM + 30 cm tube + Red Cannula"
	plt.title(name)
	flag += 1
	if(subplot_num == base_subplot_num + till):
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
		fig.subplots_adjust(wspace=0.455, hspace=0.455)
		fig.suptitle(title, fontsize = 30)
		#fig.show()
		newpath = "D:\\KYRON\\Code\\DATA\\Nasal Cannula Data\\PK041021-G01\\REPORT\\" + str(base_subplot_num) + "\\"
		if not os.path.exists(newpath):
			os.makedirs(newpath)
		fig.savefig("D:\\KYRON\\Code\\DATA\\Nasal Cannula Data\\PK041021-G01\\REPORT\\" + str(base_subplot_num) + "\\" + title + ".png", dpi = 400)
	return 0

def manager(extension):
	global flag, subplot_num
	print(extension)
	t, timestamps, r_f, SFM, DP, SDP, k = read_file(extension)
	
	#include plotting commands here#
	plot(t, SFM, timestamps, "Time in sec", "Flow through SFM", "SFM vs Time", extension)
	plot(t, DP, timestamps, "Time in sec", "Differential Pressure", "Differential Pressure vs Time", extension)
	plot(t, SDP, timestamps, "Time in sec", "Prediction of flow", "Predicted Flow vs Time", extension)
	plot(t, k, timestamps, "Time in sec", "PWM (0 - 255)", "PWM vs Time", extension)
	plot(r_f, SFM, [], "Target", "Flow through SFM", "SFM vs Target", extension)
	plot(r_f, DP, [], "Target", "Differential Pressure", "Differential Pressure vs Target", extension)
	plot(r_f, SDP, [], "Target", "Prediction of flow", "Predicted Flow vs Target", extension)
	plot(r_f, k, [], "Target", "PWM (0 - 255)", "PWM vs Target", extension)
	
	#updates
	flag = 1
	update_cell_num()
	return 0

def initialize_subplot_num(r, c, ce, t):
	global subplot_num, base_subplot_num, till
	subplot_num = (r * 100) + (c * 10) + ce
	base_subplot_num = subplot_num
	till = t - 1
	return 0

def update_cell_num():
	global subplot_num
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
	initialize_subplot_num(2, 3, 1, 6)
	manager(extension + "Without tube\\")
	manager(extension + "With tube\\")
	manager(extension + "00\\")
	manager(extension + "0\\")
	manager(extension + "1\\")
	manager(extension + "2\\")
	
	initialize_subplot_num(3, 1, 1, 3)
	manager(extension + "Green\\")
	manager(extension + "Orange\\")
	manager(extension + "Red\\")