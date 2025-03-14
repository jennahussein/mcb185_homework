#42ntcomp.py by Jenna Hussein

import sys
import sequence
import math
import mcb185

#write a program that calculates the composition of nucleotides in a FASTA file

#gc composition

#report GC per seq
total_gc = 0
total_nt = 0
gcs = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	total_gc += gc
	gcs.append(gc)
	total_nt += len(seq)
	length = len(gcs)
	print(name, gc/len(seq), total_gc, sum(gcs)/length) 
print(total_gc / total_nt)


#modified program to report avg gc over all seqs
total_gc = 0
total_seqs = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	names = defwords[0]
	print(names)
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	total_gc += gc
	total_seqs += 1
print(gc/len(seq), total_gc, total_seqs, total_gc/total_seqs)
"""
"""
#individual variable
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	for nt in seq:
		if   nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else:           N += 1
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))

#list variation, create a list to hold the counts
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
counts = [0, 0, 0, 0, 0] #A, C, G, T, N
for nt in seq:
	if   nt == 'A': counts[0] += 1
	elif nt == 'C': counts[1] += 1
	elif nt == 'G': counts[2] += 1
	elif nt == 'T': counts[3] += 1
	else:           counts[4] += 1
print(name, end=' ')
for n in counts: print(n/len(seq), end=' ')
print()

#indexing with str.find()
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
nts = 'ACGTN'
counts = [0] * len(nts)
for nt in seq:
	idx = nts.find(nt) #str.find() replaced the if-elif-else stack
	counts[idx] += 1
print(name, end=' ')
for n in counts: print(n/len(seq), end=' ')
print()


#each nt from the sequence is compared to the alphabet in nts. 
#if the letter is found, its index is returned
#if the letter is a G the index in 'ACGT' is 2 and the code does counts[2] += 1


#counting any letter
#alphabet contianer has to be a list (mutable) to count all letters

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
nts = []
counts = []
for nt in seq:
	if nt not in nts:
		nts.append(nt)
		counts.append(0)
	idx = nts.index(nt)
	counts[idx] += 1
print(name)
for nt, n in zip(nts, counts):
	print(nt, n, n/len(seq))
print()

#str.count() to count specific letters
#iterate thru alpha getting the counts for each. need to specify alpha before
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
print(name, end=' ')
for nt in 'ACGTN':
	print(seq.count(nt) / len(seq), end=' ')
print()

	