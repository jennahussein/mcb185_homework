#25deathsaves.py by Jenna Hussein

import math
import random

"""
health drops to <= 0 , unconscious and may die
roll d20, if roll is <10, record a failure
	3 failures = death
roll d20, if roll is >10, record a success
	3 success = stable but unconscious
roll d20, if you roll a 1, it counts as 2 failures
roll d20, if you roll a 20, gain 1 health and are revived
"""

trials = 100000
failed = 0
succeeded = 0
alive = 0
for i in range(trials):	
	failure = 0
	success = 0
	revived = 0 
	while success < 3 and failure < 3 and revived < 1:
		roll = random.randint(1, 20)
		if roll == 1:
			failure += 2
		elif roll <= 9: 
			failure += 1
		elif roll <= 19: 
			success += 1
		elif roll == 20:
			revived += 1
	if revived >= 1:
		alive += 1
	if success == 3:
		succeeded += 1
	if failure >= 3:
		failed += 1
	
print('failed', failed/trials, 'succeeded', succeeded/trials, 'alive', alive/trials)
	
