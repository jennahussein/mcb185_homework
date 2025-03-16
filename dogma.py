#dogma.py by Jenna Hussein

def oligo_tm(seq):
	count_a = seq.count('A')
	count_c = seq.count('C')
	count_g = seq.count('G')
	count_t = seq.count('T')
	total = count_a + count_c + count_g + count_t
	tm_short = (2 * (count_a + count_t)) + (4 * (count_c + count_g))
	tm_long = 64.9 + (41 * (count_g + count_c - 16.4))/ (total)