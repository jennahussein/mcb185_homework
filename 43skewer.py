#43skewer.py by Jenna Hussein

import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 4
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))