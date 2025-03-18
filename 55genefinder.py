#55genefinder.py by Jenna Hussein

import argparse
import mcb185
import sequence

"""
report coding genes in e. coli genome
report coordinates of each CDS
i = frame
"""
parser = argparse.ArgumentParser(description='Gene Finder.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-m','--min_length', type=int, default=300, help='minimum orf length')
arg = parser.parse_args()

seq = 'AACATGATGCGCTAACG'
stop_codons = ['TAA', 'TAG', 'TGA']
min_length = arg.min_length

def gene_finder(seq, name, min_length, strand = '+'):
	for frame in range(3): #check 3 frames starting at 0
		i = frame
		while i < len(seq) - 2:
			codon = seq[i:i+3] 
			if codon != 'ATG': #if codon not start, skip to next codon
				i += 3
				continue
			start = i #ATG found, look for stop, record beginning coord
			stop = None
			for j in range(i + 3, len(seq) - 2, 3):
				codon = seq[j:j+3]
				if codon in stop_codons:
					stop = j + 2
					if stop - start + 1 >= arg.min_length:
						if strand == '-':
							start = len(seq) - start
							stop = len(seq) - stop
						print(name, 'CDS', start + 1, stop  + 1, '.', strand, sep='\t')
					break
			i = j + 3
			
for defline, seq in mcb185.read_fasta(arg.file):
	defwords = defline.split()
	name = defwords[0]
	revseq = mcb185.anti_seq(seq)
	gene_finder(seq, defline, arg.min_length, strand='+')
	gene_finder(revseq, defline, arg.min_length, strand='-')
