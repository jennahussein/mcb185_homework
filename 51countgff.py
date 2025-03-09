#51countgff.py by Jenna Hussein

import gzip
import sys

count = {} #make empty dictionary. key = feature type value = number of times it's seen
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue #ignores comment lines
		f = line.split() 
		feature = f[2] #retrieve feature name from the lines
		if feature not in count: count[feature] = 0 #if feature not in dict, create a key
		count[feature] += 1 #count under the impression that the feature is in the table
for f, n in count.items(): print(f, n) #reports counts for each feature

"""
alt way to do lines 12 and 13:

if feature not in count: count[feature] = 1
else:                    count[feature] += 1
"""