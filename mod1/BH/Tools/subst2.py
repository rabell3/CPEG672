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
"""
def attempt_break(message, key, engsrc):
    cnt = 0
    attempt = message
    listchars=[]
    newchar = ''
    while cnt <26:
        oldchar = chr(cnt+97) #old letter
        while newchar in listchars:
            newchar = chr(random.randint(97,122))
        attempt=swap_chars(attempt, oldchar, newchar)
        cnt+=1
        listchars.append(newchar)
    score = fitsenglish(attempt, engsrc)
    results = attempt, score
    return results
"""
def attempt_break(message, key, engsrc):
    cnt=0
    listchars=[]
#    key=twiddle_key(bestkey, oc, nc)
    while cnt<26:
        for letter in key:
            #if (letter in listchars) or (oldchar in listchars):
            oldchar = chr(random.randint(97,122))
            #for letter in key:
            attempt=swap_chars(message, oldchar, letter)
        cnt+=1
    score = fitsenglish(attempt, engsrc)
    results = attempt, score
    return results

def twiddle_key(key):
    crapletters=['']
    oldlet=newlet=''

#    print "HIYATHERE"
#    print crapletters
    if oldlet in crapletters:
#        print "hi"
        oldlet = chr(random.randint(0,25)+97)
        crapletters.append(oldlet)
    if newlet in crapletters:
#        print "hello"
        newlet = chr(random.randint(0,25)+97)
        crapletters.append(newlet)

    key = key.replace(oldlet, newlet,1)
    key = key.replace(newlet, oldlet,1)
    return ''.join(key)



#------------------------------------------------------------------------------------------------------------
#----
#----
#------------------------------------------------------------------------------------------------------------
engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
fh=sys.argv[1]
codedmessage=readfile(fh)

bestkey=thiskey=seedkey(codedmessage)
thisattempt = []
thisscore = 0
bestscore = 0
attemptedkeys = ['']
p=0 # number of passes through the whole shebang

print "encoded: " , codedmessage
#decoded = codedmessage

##crapletters=['']
##oc=''
##nc=''
while thisscore < 300 and p<10000:
    #thiskey = bestkey
    #thiskey=twiddle_key(bestkey, oc, nc)
    thisattempt, thisscore = attempt_break(str(codedmessage), thiskey, engsrc)

    print "thisattempt : " , thisattempt
    print thisscore
    print thiskey
#    print crapletters
    attemptedkeys.append(thiskey)
    if thisscore >= bestscore:
#        print thiskey
#        print bestkey
        bestscore = thisscore
        bestkey = thiskey
        codedmessage = thisattempt
        print " ** New bestkey ** " , bestkey
    else:
        while thiskey in attemptedkeys:
            thiskey=twiddle_key(bestkey)
#        print oc
#        print nc
#        print "Aw"
    
#    print attemptedkeys
#    codedmessage = thisattempt
    p+=1



print "seedkey: " , bestkey
print "decoded: " , codedmessage
