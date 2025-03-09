#32stats.py by Jenna Hussein

import math
import sys

"""
write a program that reports stats for numbers on the command line
report the following values:
	num of values
	min and max values
	mean and stdev
	median
"""

vals = []
for arg in sys.argv[1:]:
	f = float(arg)
	vals.append(f)

total = 0
for val in vals: 
	total += val
print(total)

numofvals = len(vals)

print(numofvals) #this works

for val in range(len(vals)):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
print(mini)


for val in range(len(vals)):
	maxi = vals[0]
	for val in vals[1:]:
		if val > maxi: maxi = val
print(maxi)	

for val in range(len(vals)):
	total = 0
	for val in vals: total += val
	mean = total / len(vals)
print(mean)
	
vals.sort()
median = vals[numofvals // 2]
print(median)
	
variance_tot = 0
for val in vals:
	variance_tot += (val - mean) ** 2
variance = variance_tot/len(vals)
stdev = math.sqrt(variance)
print(f'{stdev:.4f}') 

half_length = total / 2
totalsum = 0

for val in vals:
	totalsum += val
	if half_length <= totalsum:
		n50 = val
		print(n50)
		break
