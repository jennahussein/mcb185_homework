# 10demo.py by Jenna Hussein

import math

print('hello, again') # greeting

"""
This is a
multi-line
comment
"""

print(1.5e-2)
print(1 + 1) 
print(1 - 1)
print(2*2)
print(1/2)
print(2**3)
print(pow(2, 3))
print(5//2)
print(5%2)
print(5*(2+1))
print(math.sqrt(64))
print(math.ceil(3.456))
print(math.floor(3.456))
print(0.1 * 1)
print(0.1 * 3)

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ',end='!\n')

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c

hyp = pythagoras(a, b)
print(hyp)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3, 4))

def pythagoras(a, b): return math.sqrt(a**2 + b**2)

a = 2
b = 3
if a == b:
	print('a equals b')
	
if a == b:
	print('a equals b')
print(a, b)

def is_even(x):
	if x % 2 == 0: return True
	return False
	
print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if a < b:
		print('a < b')
elif a > b:
		print('a > b')
else:
		print('a == b')
		
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

#the following shows that order matters. only the first true condition is executed
if	 a < b: print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print!')
		
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:		print('a == b')

print(abs(a-b))
if abs(a-b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

#this results in an error because they are two different types of values, doesn't make sense to compare them
#a = 1
#s = 'G'
#if a < s: print('a < s')

#def silly(m ,x, b):
	#y = m * x + b
	
#print(silly(2,3,4))

#Practice questions

s = 'hello world'
print(s, type(s))

#t= 32
#celsius = (t - 32) * 5/9

def temperature_in_celsius(t):
	celsius = (t - 32) * 5/9
	return celsius

#print(celsius)
print(temperature_in_celsius(60)) #calling the function i made in 126

def mph_to_kph(m):
	return m * 1.6 
	
print(mph_to_kph(5))

def arith_mean(a, b, c):
	sum = a+b+c
	return sum/3

print(arith_mean(1, 2, 4))

def geo_mean(a, b, c):
	return math.sqrt(a*b*c)

print(geo_mean(1, 2, 4))

def harmonic_mean(a, b, c):
	n = 3
	sum = (1/a) + (1/b) + (1/c)
	return n/sum
	
print(harmonic_mean(1, 2, 4))

def distance(x1, y1, x2, y2):
	x_distance = x2 - x1
	y_distance = y2 - y1
	return math.sqrt((x_distance ** 2) + (y_distance ** 2))
	
print(distance(1, 3, 6, 5))

def is_integer(n):
	if n % 2 == 0: return True
	return False

print(is_integer(4))
print(is_integer(3))

def valid_probability(n):
	if n >= 0 and n <= 1: return True
	return False

print(valid_probability(5))
print(valid_probability(0.2))

def molecular_weight(n):
	if   n == 'A': return 135.13
	elif n == 'C': return 111.1
	elif n == 'G': return 329.2
	elif n == 'T': return 126.11
	else:		   return None

print(molecular_weight('A'))
print(molecular_weight('B'))
print(molecular_weight('C'))
	
def complement(n):
	if   n == 'A': return 'T'
	elif n == 'C': return 'G'
	elif n == 'G': return 'C'
	elif n == 'T': return 'A'
	else: 		   return None
	
print(complement('A'))
print(complement('B'))
print(complement('C'))

def max_of_three(a, b, c):
	return (max(a, b, c))

print(max_of_three(31, 9, 7))

def sensitivity(tp, fn):
	return (tp)/(tp + fn)

print(sensitivity(1, 4))

def specificity(tn, fp):
	return (tn)/(tn + fp)

print(specificity(3, 9))

#f1 score is 2 x specificity (n) x sensitivity (m)
def formula1(tp, tn, fp, fn):
	spec = (tp)/(tp + fn)
	sens = (tn)/(tn + fp)
	return (2 * spec * sens)/(spec + sens)
	
print(formula1(6, 12, 9, 4))

def shannon_entropy(A, C, G, T):
	total = A + C + G + T
	if total == 0: return 0
	prob_A = A/total
	prob_C = C/total
	prob_G = G/total
	prob_T = T/total
	
	if   A > 0:	entropy = -prob_A * math.log2(prob_A)
	elif C > 0: entropy = -prob_C * math.log2(prob_C)
	elif G > 0: entropy = -prob_G * math.log2(prob_G)
	elif T > 0: entropy = -prob_T * math.log2(prob_T)
	else: print(0)
	return entropy 
	
print(shannon_entropy(3, 6, 9, 12))
print(shannon_entropy(10, 10, 10, 10))
print(shannon_entropy(0, 0, 0, 0))
print(shannon_entropy(30, 30, 0, 0))
