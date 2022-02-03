import matplotlib.pyplot as plt
import sys

# Initializaing 
file_name = sys.argv[1]
user_name = sys.argv[2]
target_value = 0
threshold = 0
x = []
y = []

# open the logfile
fd = open("log.txt",'r')
lines = fd.readlines()

for i,line in enumerate(lines):
	if i == 0:
		_,threshold = line.split(":")
		threshold = int(threshold.strip())
	if i > 0:
		a,val = line.split(" ")
		x.append(i)
		y.append(int(val.strip()))

for i,each in enumerate(y):
	if each < 300:
		i = int(str(i),10)
		target_value = i
		print('- Target: '+str(i)+"(latency: "+str(each)+")")

# Set the figure's information 
plt.plot(x,y)
plt.hlines(threshold,0,250,color="red")
plt.xlabel("Probing value")
plt.ylabel("Time (Cycle)")

# Set the figure's title
title = '<Flush+Reload>\n - ' + user_name + "'s target_value is '" + str(target_value) +  "'\n - threshold is '" + str(threshold)+"'"
plt.title(title)

# Set the figure's size
plt.ylim([100,900])

# Save the figure
plt.savefig('./result.png')
plt.show()
