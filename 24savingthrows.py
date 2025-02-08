#24savingthrows.py by Jenna Hussein

import math
import random

"""
if advantage, roll two d20, take max roll, if greater than dc success
	otherwise, fail
if disadvantage, roll two d20, take min roll, if greater than dc success
	otherwise, fail
write a program that simulates throws against DCs of 5, 10, and 15
"""

def advantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 > r2: return r1
	return r2
	
def disadvantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1,20)
	if r1 < r2: return r1
	return r2
	
trials = 1000000
dc = 5
sides = 20

for dc in range(1, 20, 1):
	nor = 0
	adv = 0
	dis = 0
	for i in range(trials):
		r1 = random.randint(1, sides)
		r2 = random.randint(1, sides)
		if r1 >= dc: nor += 1
		if r1 >= dc and r2 >= dc: dis +=1
		if r1 >= dc or r2 >= dc: adv +=1
	print(dc, 'pn', nor/trials, 'pd', dis/trials, 'pa', adv/trials)

		
	
	

