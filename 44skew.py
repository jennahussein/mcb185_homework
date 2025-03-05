#44skew.py by Jenna Hussein

import sequence
import sys
import mcb185


#problem with 43skew is that each window is counted then forgotten.
#write a program that uses a sliding window algo to compute gc comp and skew 

 
w = 10
s = 1

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	g = sequence.g_count(seq[0:w])
	c = sequence.c_count(seq[0:w])
	gc_comp = sequence.comp_new(g, c, w)
	gc_skew = sequence.skew_new(g, c)
	for i in range(0, len(seq) - w):
		codon = seq[i:i+3]
		on = seq[i+w]
		off = seq[i]
		if   on == 'G': g += 1
		elif on == 'C': c += 1
		if   off == 'G': g -= 1
		elif off == 'C': c -= 1
		gc_comp = sequence.comp_new(g, c, w)
		gc_skew = sequence.skew_new(g, c)
		print(i, gc_comp, gc_skew)
		
"""
for i in range(w): #this loop counts the initial window
	if   seq[i] == 'C': c += 1
	elif seq[i] == 'G': g += 1

for i in range(0, len(seq) - w):
	on = seq[i+w]
	off = seq[i]
"""	