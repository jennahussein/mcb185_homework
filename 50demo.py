import random
import sys
import itertools
import mcb185


s = {'A', 'C', 'G'} #Curly brackets  = set. elements not in same order each time
s.add('T') #adds items to a set
s.add('A') #Adding the same element doesn't do anything
		   #print(s[2]) is an error since there is no order
print(s)

#Dictionaries

#two ways to make empty dictionaries
d = {}
d = dict()

d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

if 'dog' in d: print(d['dog'])

for key in d: print('f{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

for thing in d.items(): print(thing[0], thing[1])

print(d.keys(), d.values(), list(d.values()))

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
    
#Dictionaries can be used to categorize new info not just look up old info

#Another way to count letters with a dictionary


count = {}
"""
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
"""
	
#sorting by keys
for k in sorted(count): print(k, count[k])

#sorting by values
for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)
	
def by_value(tuple):
	return tuple[1]

for k, v in sorted(count.items(), key = by_value):
	print(k, v)
	
k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
for kmer, n in kcount.items(): print(kmer, n)

for nts in itertools.product('ACGT', repeat=2):
	print(nts)
