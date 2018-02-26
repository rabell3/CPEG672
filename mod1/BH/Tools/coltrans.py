import sys, re, itertools, pickle, random, pprint, os
import numpy as np
from collections import Counter,OrderedDict
from cpeglibs import *

def col_trans(plain):
    cols = random.randint(8,10)
    key = range(cols)
    random.shuffle(key)
    return "".join(plain[i::cols].lower() for i in key), key

def ciph_trans(cipher):
    #cols = random.randint(8,10)
    cols = 8
    key = range(cols)
    random.shuffle(key)
    return "".join(cipher[i::cols].lower() for i in key), key

#------------------------------------------------------------------------------------------------------------
#----
#----
#------------------------------------------------------------------------------------------------------------
engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
fh=sys.argv[1]
codedmessage=readfile(fh)

#print ciph_trans(codedmessage)

# Crutch: https://stackoverflow.com/questions/3636344/read-flat-list-into-multidimensional-array-matrix-in-python
"""
>>> data = [0, 2, 7, 6, 3, 1, 4, 5]
>>> col = 4  # just grab the number of columns here

>>> [data[i:i+col] for i in range(0, len(data), col)]
[[0, 2, 7, 6],[3, 1, 4, 5]]

>>> # for pretty print, use either np.array or np.asmatrix
>>> np.array([data[i:i+col] for i in range(0, len(data), col)]) 
array([[0, 2, 7, 6],
       [3, 1, 4, 5]])
"""
data = codedmessage
col = 8
print np.array([data[i:i+col] for i in range(0, len(data), col)])
col = 9
print np.array([data[i:i+col] for i in range(0, len(data), col)])
col = 10
print np.array([data[i:i+col] for i in range(0, len(data), col)])