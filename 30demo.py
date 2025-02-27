#30demo.py by Jenna Hussein

import math
import random
import sys

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

print(f'{math.pi}')

print(f'{math.pi:.3f}')

print(f'{1e6 * math.pi:e}')

print(f'{"hello world":>20}')

print(f'{"hello world":.>20}')

print(f'{20:<10} {10}')

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
#Indexes
seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq:
	print(nt, end = '')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
grades = 'ABCDF'

for grade in grades:
	print(grade, end='')

#difference between a list and a tuple is that a list has [] and a tuple has ()


s = 'GAATTC'
container = []

for nt in s:
	container.append(nt)

container[4] = 'X'
print(container)

seq = []
for i in range(1000):
	nt = random.choice('ATCG')
	seq.append(nt)

print(seq)

dna = ''.join(seq)

print(dna)
print(dna[0:20])

#Slices

s= 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])

print(s[0:5], s[:5])

print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1]) #s[::-1] prints the string backwards

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	
tax = ('Homo', 'sapiens', 9606)

print(tax)
print(tax[0])
print(tax[::-1])

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenosine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

nts.copy()

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day           to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

alph = 'ABCDEFGHI'

print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))

alpha = 'Gaza'
print('find G?', alpha.find('G'))
print('find Z?', alpha.find('Z'))

# if thing in list: idx = list.index(thing) to search a list or tuple
	#use if you dont know if the element is in the list
	
#Practice Problems

vals = 43, 12, 5, 23, 96

def minimum(vals):
	mini = vals[0] #sets minimum to the first value
	for val in vals[1:]: #check every val in vals
		if val < mini: mini = val # if val < mini, that val becomes the new mini
	return mini

print(minimum(vals))

#another way

def mini(vals):
	return min(vals)

print(mini(vals))

def minmax(vals):
	mini = vals[0]
	maxx = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxx: maxx = val
	return mini, maxx
	
print(minmax(vals))

#another way

def minmaxx(vals):
	minimum = min(vals)
	maximum = max(vals)
	return minimum, maximum
	
print(minmax(vals))

def avg(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
print(avg(vals))

def average(vals):
	total = sum(vals)
	mean = total/ len(vals)
	return mean

print(average(vals))

probs = 0.2, 0.5, 0.8, 0.1, 0.7

def entropy(probs):
	h = 0
	for prob in probs:
		h -= prob * math.log2(prob)
	return h

print(entropy(probs))


def kullback(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1] #defined as a list
p2 = (0.1, 0.3, 0.4, 0.2) #defined as a tuple
#it's okay that p1 and p2 are list and tuple because they'll be zipped in parallel
print(kullback(p1, p2))
	
print(sys.argv)

i = int('42')
x = float('0.61803')
print(i * x)

#x = float('hello')
#print(x)

sys.exit() #to provide a custom error message

#for i in range(0, len(list)):
	#for j in range(X, len(list))

"""
change X to get the 3 different pairwise comparisons
X = 0: all combinations
X = i: half matrix w/ diagonal
X = i+1: half matrix w/o diagonal
"""

#class demo 2/18

things = ['socks', 'pants', 'shirt', 'hat', 'gloves'] #tuple bc of ()
print(things)

things.append('scarf')
print(things)

#index

print(things[0:2]) #end before you get to the second index
print(things[0:4:2])
print(things[4::-2])
print(things[::-1])
print(things[0][1]) #goes into thing 0 of things (socks) and gives the 1st index "o"

position = int(sys.argv[1])
frame = int(sys.argv[2])
codon = sys.argv[3]

seq = 'ATGCTGTAA'
for frame in range(3):
	for i in range(frame, len(seq)-2, 3):
		position = i + 1
		codon = seq[i:i+3]
		
