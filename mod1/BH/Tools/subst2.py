import sys, re, itertools, pickle, random, pprint, os
from collections import Counter,OrderedDict
from cpeglibs import *

def replaceit(nc):
    oldchar = chr(nc) #old letter
#        while newchar in listchars:
    return chr(random.randint(97,122))

def findourstats(codedmessage):
    codefreq = findfreq(codedmessage)
    normfreq = normal_freqs

    for key, value in sorted(normal_freqs.iteritems(), key=lambda (k,v): (v,k),reverse=True):
        print "%s: %s" % (key, value)

    for key, value in sorted(codefreq.iteritems(), key=lambda (k,v): (v,k),reverse=True):
        print "%s: %s" % (key, value)

    normfreq=sorted(normfreq.iteritems(), key=lambda (k,v): (v,k),reverse=True)
    codefreq=sorted(codefreq.iteritems(), key=lambda (k,v): (v,k),reverse=True)

    print normfreq
    print codefreq
    return

#------------------------------------------------------------------------------------------------------------
#----
#----
#------------------------------------------------------------------------------------------------------------
engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
fh=sys.argv[1]
codedmessage=readfile(fh)

normfreq = normal_freqs
codefreq = findfreq(codedmessage)

normfreq=sorted(normfreq.iteritems(), key=lambda (k,v): (v,k),reverse=True)
codefreq=sorted(codefreq.iteritems(), key=lambda (k,v): (v,k),reverse=True)

#findourstats(codedmessage)

letters = range(26)
random.shuffle(letters)

print codedmessage

for i in range(26):
    oldc, cstat = codefreq[i]
    newc, nstat = normfreq[i]
    print oldc , " -> " , newc
    decoded = codedmessage.replace(oldc, newc)

print decoded
