import sys, re, itertools, pickle, random, pprint
from collections import Counter
from cpeglibs import *

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

# -----------------------------------------------------------------------------------------------------
engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
fh=sys.argv[1]
codedmessage=readfile(fh)
listchars=[]

print codedmessage
print fitsenglish(codedmessage,engsrc)
newchar=""
#findourstats(codedmessage)

newmesg = codedmessage

for ltr in str(range(26)):
    #newchar =''
    oldchar = ltr
    
    c=0
    i=0
    while newchar in listchars:
        newchar = chr(random.randint(97,122))


    listchars.append(newchar)
    newmesg = swap_chars(newmesg, oldchar, newchar)
    print newmesg
    print listchars

    bicount, tricount, quadcount = findngrams(newmesg)
    print bicount
    print tricount

#    print fitsenglish(newmesg,engsrc)
