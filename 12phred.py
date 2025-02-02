#12phred.py by Jenna Hussein

import math

def char_to_prob(a):
	if ord(a) < 33 or ord(a) > 126: 
		return None
	score = ord(a) - 33
	return 10 ** (-score/10)

print(char_to_prob('F'))
print(char_to_prob('?'))


def prob_to_char(p):
	if 0 < p < 1:
		phred_score = -10 * math.log10(p)
		return chr(int(phred_score) + 33)
	return None

print(prob_to_char(0.30))
print(prob_to_char(0.0065))
	