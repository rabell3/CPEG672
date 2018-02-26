import sys, re, itertools, pickle, random, pprint, os
from collections import Counter,OrderedDict
from cpeglibs import *

def seedkey(message):
    normfreq = normal_freqs
    codefreq = findfreq(codedmessage)
    normfreq=sorted(normfreq.iteritems(), key=lambda (k,v): (v,k),reverse=True)
    codefreq=sorted(codefreq.iteritems(), key=lambda (k,v): (v,k),reverse=True)
    newkey=[]
    newchar=''

    for i in range(10):
        oldc, cstat = codefreq[i]
        newc, nstat = normfreq[i]
        newkey.append(newc)
    while len(newkey) < 26:
        newchar = chr(random.randint(97,122))
        if newchar not in newkey:
            newkey.append(newchar)
    return ''.join(newkey)

def attempt_break(message, key, engsrc):
    cnt = 0
    attempt = message
    listchars=[]
    newchar = ''
    while cnt <26:
        oldchar = chr(cnt+97) #old letter
        while newchar in listchars:
            newchar = chr(random.randint(97,122))
        swap_chars(message, oldchar, newchar)
        cnt+=1
        listchars.append(newchar)
    score = fitsenglish(attempt, engsrc)
    results = attempt, score
    return results

#------------------------------------------------------------------------------------------------------------
#----
#----
#------------------------------------------------------------------------------------------------------------
engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
fh=sys.argv[1]
codedmessage=readfile(fh)

bestkey=seedkey(codedmessage)
thisattempt = []
thisscore = 0
bestscore = 0
p=0 # number of passes through the whole shebang

print "encoded: " , codedmessage
decoded = codedmessage

while thisscore < 500 and p<10000:
    thiskey = bestkey
    thisattempt,thisscore = attempt_break(str(decoded), thiskey, engsrc)

#    print "thisattempt : " , thisattempt
#    print thisscore

    if thisscore > bestscore:
        print thiskey
        print bestkey
        bestscore = thisscore
        bestkey = thiskey
        decoded = thisattempt
#        print "hi"
    else:
        oc = chr(random.randint(0,25)+97)
        nc = chr(random.randint(0,25)+97)
#        print oc
#        print nc
#        print "Aw"
        thiskey=twiddle_key(bestkey, oc, nc)

#    decoded = thisattempt
    p+=1



print "seedkey: " , bestkey
print "decoded: " , decoded
