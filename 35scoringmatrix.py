#35scoringmatrix.py by Jenna Hussein

import sys

"""
write a program that prints out a match mismatch scoring matrix
the alphabet, match and missmatch are all command line parameters
"""

alphabet = sys.argv[1]
matches = sys.argv[2]
mismatch = sys.argv[3]

print('   ', end='')
for nt in alphabet: print(nt, end='  ')
print()

for nt1 in alphabet: 
	print(nt1, end=' ')
	for nt2 in alphabet:
		if nt1 == nt2: print(matches, end=' ')
		else:          print(mismatch, end=' ')
	print()
