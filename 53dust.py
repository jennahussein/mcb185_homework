#53dust.py by Jenna Hussein

#idk how to soft mask it

import mcb185
import argparse
import sys
import math

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
parser.add_argument('--wrap', type=int, default=60)
arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):
	defwords = defline.split()
	name = defwords[0]
	mask = list(seq)
	for i in range(len(seq) - arg.size + 1):
		h = 0
		subseq = seq[i:i+arg.size]
		prob_a = subseq.count('A') / arg.size
		prob_c = subseq.count('C') / arg.size
		prob_g = subseq.count('G') / arg.size
		prob_t = subseq.count('T') / arg.size
		ind_probs = [prob_a, prob_c, prob_g, prob_t]
		for prob in ind_probs:
			if prob > 0:
				h -= prob * math.log2(prob)
		if h < arg.entropy:
			for j in range(i, i + arg.size):
				mask[j] = seq[j].lower()

print('>', defline, sep='')
masked_sequence = ''.join(mask)

for i in range(0, len(masked_sequence), arg.wrap):
	print(masked_sequence[i:i+arg.wrap])
	
for defline, seq in mcb185.read_fasta(arg.file):
	mask = list(seq)
	for i in range(len(seq) - arg.size + 1):
		window = seq[i:i+arg.size]
