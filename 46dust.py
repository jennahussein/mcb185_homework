#46dust.py by Jenna Hussein

import mcb185
import sys
import math

"""
mask low complexity sequence to prevent finding meaningless alignments
input: multi-FASTA file of DNA
output: input with low complexity regions masked
change low complexity regions to 'N'
provide window size and entropy thresholds
"""

w = int(sys.argv[2]) #window size
et = float(sys.argv[3]) #entropy threshold
wrap = 60

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	mask = list(seq)
	for i in range(len(seq) -w + 1):
		h = 0
		subseq = seq[i:i+w]
		prob_a = subseq.count('A') / w
		prob_c = subseq.count('C') / w
		prob_g = subseq.count('G') / w
		prob_t = subseq.count('T') / w
		ind_probs = [prob_a, prob_c, prob_g, prob_t]
		for prob in ind_probs:
			if prob > 0:
				h -= prob * math.log2(prob)
		if h < et:
			for j in range(i, i + w):
				mask[j] = 'N'

print('>', defline)
masked_sequence = ''.join(mask)

for i in range(0, len(masked_sequence), wrap):
	print(masked_sequence[i:i+wrap])				