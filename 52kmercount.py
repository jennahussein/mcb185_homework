#52kmercount.py by Jenna Hussein

import sys
import mcb185
import itertools

k = int(sys.argv[2])

kcount = {} #empty dictionary to hold key:value pairs
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1): #windowing algo
		kmer = seq[i:i+k] #create a variable
		if kmer not in kcount: kcount[kmer] = 0 #if kmer not in dict, make it
		kcount[kmer] += 1 #increase counts of observed k-mer
for kmer, n in kcount.items(): print(kmer, n)

for nts in itertools.product('ACGT', repeat=k):
	kmer = ''.join(nts) #joins the tuple nts into a string so we can index it
	if kmer in kcount: print(kmer, kcount[kmer])
	else:              print(kmer, 0)

#python3 52kmercount.py ecoli.fa.gz 7 | sort -nk2 | head
#kmers that aren't found will be reported with 0 counts