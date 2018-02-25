import sys, re, itertools, pickle, random, pprint
from collections import Counter
from cpeglibs import *

def swap_chars(message, oldlet, newlet): 
    message = message.replace(oldlet, newlet)
    return ''.join(message)

# -----------------------------------------------------------------------------------------------------
engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
fh=sys.argv[1]
codedmessage=readfile(fh)

print codedmessage
print fitsenglish(codedmessage,engsrc)
newmesg= swap_chars(codedmessage, 'o', 'f')
print newmesg
print fitsenglish(newmesg,engsrc)