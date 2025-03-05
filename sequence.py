#sequence.py by Jenna Hussein

import sys
import mcb185

"""
str.replace() searches for substrings and converts them to other substrings
strings are immutable, str.replace returns a copy
"""

def transcribe(dna):
	return dna.replace('T', 'U') #bc mRNA uses A, C, G, U

def revcomp(dna):
	rc = [] #list to hold seq
	for nt in dna[::-1]: #goes backwards thru dna
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc) #return string version of the list
	
def translate(dna):
	aas = [] #initializes empty list for the amino acids
	for i in range(0, len(dna), 3): #step through indices by 3
		codon = dna[i:i+3] #creates a codon, 3 letter slice
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)
	
#alternate way to write the translation function
"""
def translate(dna):
	codons = ('ATG', 'TAA', 'TAG', 'TGA') #parallel containers that match codon to aa
	aminos = 'M***' #parallel container
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons: #ask if codon is in the tuple
			idx = codons.index(codon) #if codon in tuple, ask for index
			aa = aminos[idx] #once position in idx, retrieve aa from string
			aas.append(aa) #append aa to growing peptide
		else:
			aas.append('X')
	return ''.join(aas)
"""

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def g_count(seq):
	return(seq.count('G'))

def c_count(seq):
	return(seq.count('C'))
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def skew_new(c, g):
	if c + g == 0: return 0
	return (g - c) / (g + c)

def comp_new(c, g, s):
	return (c + g) / s
"""
#Sliding Window Algorithm

w = 10 #Set size of window, would be 3 for translation bc codons have length of 3
s = 1 #set step size. for translation it'd also be 3
for i in range(0, len(seq) -w +1, s): #moves window along the seq
	subseq = seq[i:i+w] #creates a subseq as a slice using current offset i and w
"""