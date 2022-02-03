import matplotlib.pyplot as plt
import sys
import cpuinfo

file_name = sys.argv[1]
user_name = sys.argv[2]
target_value = 0
fd = open("log.txt",'r')
lines = fd.readlines()

x = []
y = []

for i,line in enumerate(lines):
	a,val = line.split(" ")
	x.append(i)
	y.append(int(val.strip()))

for i,each in enumerate(y):
	if each < 300:
		i = int(str(i),10)
		target_value = i
		print(str(i)+":"+str(each))
plt.plot(x,y)
plt.xlabel("Probing value")
plt.ylabel("Time (Cycle)")
try: info_cpu = cpuinfo.get_cpu_info()['brand_raw']
except: info_cpu = cpuinfo.get_cpu_info()['brand']
title = 'Flush+Reload\n' + user_name + "'s target_value is " + str(target_value) +  '\n(in ' + info_cpu  + ')'
plt.title(title)
plt.ylim([100,900])
plt.savefig('./result.png')
plt.show()
