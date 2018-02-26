import random
from cpeglibs import *

def col_trans(plain):
    cols = random.randint(8,10)
    key = range(cols)
    random.shuffle(key)
    return "".join(plain[i::cols].lower() for i in key), key

engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')

ourstring = "theraininspainstaysmainlyintheplains"
print ourstring
print fitsenglish(ourstring,engsrc)
cipher, key = col_trans(ourstring)

print cipher
print key
print fitsenglish(cipher,engsrc)

cols=8
for i in key: 
    print cipher[i::cols]
print "p1"
#print fitsenglish(p1,engsrc)
cols=9
for i in key:
    print cipher[i::cols]
print "p2"
#print fitsenglish(p2,engsrc)
cols=10
for i in key:
    print cipher[i::cols]
print "p3"
#print fitsenglish(p3,engsrc)