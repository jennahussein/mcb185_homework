#54missingkmers.py by Jenna Hussein

import argparse
import itertools
import mcb185

parser = argparse.ArgumentParser(description='Kmer Finder')
parser.add_argument('file', type=str, help='name of fasta file')
arg = parser.parse_args()

k = 0
missing_kmer = 0
missing_kmers = []
kcount = {}

def kmers(seq, k):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1

while missing_kmer == 0:
	k += 1
	kcount = {}
	for defline, seq in mcb185.read_fasta(arg.file):
		rev_strand = mcb185.anti_seq(seq)
		kmers(seq, k)
		kmers(rev_strand, k)
	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts)
		if kmer not in kcount:
			missing_kmer += 1
			missing_kmers.append(kmer)

print(missing_kmers, len(missing_kmers), k)