#34birthday.py by Jenna Hussein

import sys
import random
 
trial= int(sys.argv[1])
size = int(sys.argv[2])
calendar = 365*[0]

for t in range(size):
	bday = random.randint(0, 364)
	calendar[bday] += 1
	if calendar[bday] > 1: 
		print(bday, 'MATCH')
		break

print(calendar)
