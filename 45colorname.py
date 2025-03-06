#45colorname.py by Jenna Hussein

import sys

#write a program that provides the closes official color name given some RGB
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

initial = R, G, B

#measure distance 
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

with open(colorfile, 'rt') as fp:
	closest_color = None
	mini = 10000
	for line in fp:
		words = line.split()
		color_name = words[0]
		rgb = words[2]
		channels = rgb.split(',')
		r = int(channels[0])
		g = int(channels[1])
		b = int(channels[2])
		final = r, g, b
		distance = dtc(initial, final)
		if distance < mini: 
			mini = distance
			closest_color = color_name
print(closest_color)
