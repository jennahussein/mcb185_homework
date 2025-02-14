#20demo.py by Jenna Hussein

import math
import random


t = 1, 2

print(t)
print(type(t))

person = 'Steve', 21, 57891.50

print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y

print(midpoint(1, 2, 3, 4))

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
mz, ma = m
print(mx, my)
print(mz, ma)
print(m[0])
print(m[1])

#while True:
	#print('hello')
	
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
 
i = 0
while i < 3:
	i = i + 1
	print('hey', i)

i = 0
for i in range (10, 1, -2):
	print(i)

i = 0
loops = 0
while i < 10:
	print(i)
	loops = loops + 1
	i = i + 3
print('final value of i is', i)
print('number of loops', loops)


for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else:		   print(i, 'is odd')
	
for i in range(5):
	print(random.random())
	
for i in range(3):
	print(random.randint(1, 6))
	
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())


#Practice

def triangular_number(n):
	total = 0
	for i in range(1, n+1):
		total = total + i
	return total

print(triangular_number(70))
print(triangular_number(6))

def factorial_number(n):
	if n == 0: return 1
	total = 1
	for i in range(1, n+1):
		total = total * i
	return total

print(factorial_number(6))
print(factorial_number(12))

def poisson(n, k):
	return n**k * math.e**-n / factorial_number(k)

print(poisson(2, 3))

def nchoosek(n, k):
	return factorial_number(n) / (factorial_number(k) * factorial_number(n - k))

print(nchoosek(5, 2))

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial_number(n)
	return e
	
print(euler(8))

limit = 3


def nilakantha(limit):
	pi = 3
	
	for i in range(1, limit):
		sign = (-1) ** (i+1)
		n = 2 * i
		d = n * (n+1) * (n+2)
		pi = pi + (sign * 4) / d
	return pi
print(nilakantha(100000))


#greater than 1 outside the circle
#smalled than 1 inside the circle
#montypython
"""
ins = 0
tot = 0
for i in range(10):
	if (random.random()**2 + random.random()**2) ** 0.5 <= 1: ins +=1
	tot += 1
	print

while True:
	x = random.random()
	y = random.random()
	distance = math.sqrt((x**2) + (y**2)) 
	
	if distance <= 1: countin += 1
	if distance > 1: countout += 1
	print(distance)

print =(4 * (countin/ countin + countout))

ins = 0
tot = 0
while True:
	x = random.random()
	y = random.random()
	if math.sqrt(x**2 + y**2) < 1: ins += 1
	tot += 1
	print(4 * ins/tot)

def max_2d():
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	if r1 > r2: return r1
	return r2
	
n = 10000
total = 0
for i in range(n):
	r1 = max_2d
	r2 = max_2d
	r3 = max_2d
	total += r1 + r2 + r3
print(total / n)
"""

random.seed(5)
for i in range(10):
	print(random.random())
	
sign = -1
for i in range(10):
	sign = sign * -1
	print(sign)
	
toggle = True
for i in range(10):
	toggle = not toggle
	print(toggle)
	
for i in range(0, 10, 2):
	print(i)
	
for i in range(10):
	print(i)

limit = 10

for i in range(limit):
	sign = (-1)**(i+1) # start with -1 / subtraction
	signnn = (-1) ** i # start with +1 / addition
	print(sign, signnn)

def nilakantha(limit):
	pi = 3
	
	for i in range(1, limit):
		sign = (-1) ** (i+1)
		n = 2 * i
		d = n * (n+1) * (n+2)
		pi = pi + (sign * 4) / d
	return pi
print(nilakantha(100000))

