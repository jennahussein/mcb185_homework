#11oligo.py by Jenna Hussein

import math

def oligo_mt(A, C, G, T):
	tm_short = (2 * (A + T)) + (4 * (G + C))
	tm_long = 64.9 + (41 * (G + C - 16.4))/ (A + T + C + G)
	total = A + C + G + T
	
	if total <= 13: return tm_short
	else:		return tm_long
	
print (oligo_mt(1, 2, 3, 4))
print(oligo_mt(5, 7, 3, 4))
print(oligo_mt(13, 23, 33, 43))
print(oligo_mt(0, 0, 2, 3))