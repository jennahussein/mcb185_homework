#47cdsfinder.py by Jenna Hussein

import mcb185
import sys
import sequence
import math

"""
to do:
	find proteins
	make sure proteins >= 100 aas
"""
dna = sys.argv[1]
min_length = int(sys.argv[2])

def cdsfinder(dna, min_length):
	for frame in range(3):
		proteins = 0
		translation = mcb185.translate(dna, frame)
		orfs = translation.split('*')
		for orf in orfs:
			if 'M' not in orf: continue
			idx = orf.index('M')
			protein = orf[idx:] + '*'
			if len(protein) >= min_length:
				print('>', defline, '-protein-', proteins, sep='')
				print(protein)
				proteins += 1
	
		
for defline, dna in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	reverse = sequence.revcomp(dna)
	print(cdsfinder(dna, min_length))
	print(cdsfinder(reverse, min_length))
