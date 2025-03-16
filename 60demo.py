#60demo.py by Jenna Hussein

import sys
import math
import dogma
import json

print(sys.argv)
print(sys.argv[0])

print(sys.argv[0][3])

d = [
	'hello',
	(3.14, 'pi'),
	[-1, 0, 1],
	{'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])

#arrays are linear containers, all elements are the same type
#matrices are multi-dimensional arrays, rectangular, all elements same type

#record for sequencing oligo. record = data type with multiple fields
oligo = {
		'Name': 'S0116',
		'Length': 18,
		'Sequence': 'ATTTAGGTGACACTATAG',
		'Description': 'SP6 promoter sequencing primer'
}

#catalog is a list of records

catalog = []
catalog.append(oligo)

#how to read a csv into a list of records
"""
def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp: 
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
					 'Name': name,
					 'Length': length,
					 'Sequence': seq,
					 'Description': desc
			}
			catalog.append(record)
	return catalog

catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])
"""	
for primer in catalog:
	primer['Tm'] = dogma.oligo_tm(primer['Sequence'])
print(catalog)

#tells us locations of each kmer
seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = [] #new empty list with each new dict key
	kloc[kmer].append(i)
print(kloc)

"""
JSON differences:
double quotes only
true/ false instead of True/ False
commas not allowed on last block element
no comments
"""

truc = {
	'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is_complete': False,
}
print(json.dumps(truc, indent=4))