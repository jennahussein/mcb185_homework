#48transmembrane.py by Jenna Hussein

import mcb185
import sequence
import sys

"""
seq = E. coli sequence
s = length of the sequence
kdt = kyte-doolittle hydrophobicity threshhold
"""

def hydrophobic(seq, s, kdt, beg, end):
	subseq = seq[beg:end + 1]
	for i in range(0, len(subseq) - s + 1):
		p = subseq[i:i+s]
		score = 0
		if 'P' in p: continue
		for aa in p:
			if   aa == 'I': score += 4.5
			elif aa == 'V': score += 4.2
			elif aa == 'L': score += 3.8
			elif aa == 'F': score += 2.8
			elif aa == 'C': score += 2.5
			elif aa == 'M': score += 1.9
			elif aa == 'A': score += 1.8
			elif aa == 'G': score -= 0.4
			elif aa == 'T': score -= 0.7
			elif aa == 'S': score -= 0.8
			elif aa == 'W': score -= 0.9
			elif aa == 'Y': score -= 1.3
			elif aa == 'H': score -= 3.2
			elif aa == 'E': score -= 3.5
			elif aa == 'Q': score -= 3.5
			elif aa == 'D': score -= 3.5
			elif aa == 'N': score -= 3.5
			elif aa == 'K': score -= 3.9
			elif aa == 'R': score -= 4.5
		avg_kd = score / s
		if avg_kd >= kdt:
			return p
			break	

counts = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal_pep = hydrophobic(seq, 8, 2.5, 0, 30)
	transmembrane_pep = hydrophobic(seq, 11, 2.0, 31, len(seq))
	if signal_pep and transmembrane_pep != None:
		counts += 1
		print(defline) 
print(counts)