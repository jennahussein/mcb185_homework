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

for i in range(len(alphabet)): 
	print(alphabet[i], end=' ')
	for j in range(i, len(alphabet)):
		if alphabet[i] == alphabet[j]: print(matches, end=' ')
		else:          print(mismatch, end=' ')
	print()
