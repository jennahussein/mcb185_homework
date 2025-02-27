#33birthday.py by Jenna Hussein

import random
import sys

shared = int(sys.argv[1])
trials = int(sys.argv[2])
size = int(sys.argv[3])

for t in range(trials):
	bdays = [] #empty list of students birthdays
	for i in range(size):
		bday = random.randint(0, 364)
		if bday in bdays:
			shared += 1
			break
		else:
			bdays.append(bday)
			
print(shared/trials)


shared = int(sys.argv[1])
trials = int(sys.argv[2])
size = int(sys.argv[3])

for t in range(trials):
	bdays = []
	for n in range(size):
		bday = random.randint(0, 364)
		if bday in bdays:
			shared += 1
			break
		else:
			bdays.append(bday)
			
print(shared/trials)
			
	



















