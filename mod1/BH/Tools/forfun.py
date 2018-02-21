import urllib2, re
from cpeglibs import *

res = urllib2.urlopen('http://www.gutenberg.org/files/100/100-0.txt')
englishtest = res.read().split()

englishtest = str(englishtest).replace(" ", "")
englishtest = re.sub(r'[^a-zA-Z ]', '', englishtest)
englishtest = englishtest.lower()

#print englishtest
ourscore = fitsenglish(englishtest)
print "English score: " , ourscore