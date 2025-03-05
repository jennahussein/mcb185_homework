#40cdslength by Jenna Hussein

import gzip
import sys


#create a program that reports the length of protein coding genes in the ecoli genome

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line[0] != '#': #skip over comment lines
			words = line.split()
			if words[2] == 'CDS': #find CDS features
				beg = int(words[3]) #covert coordinate to integer
				end = int(words[4]) #^
				print(end - beg + 1) #report the length

				
				
				
				