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

def find_nth_frequent_ltr(freqs, num):
    sortedfreq=sorted(freqs.iteritems(), key=lambda (k,v): (v,k),reverse=True)
    return sortedfreq[num]

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
def attempt_break(message, key):
    for i in range(26):
        newlet, nfreq = find_nth_frequent_ltr(normal_freqs,i)
        oldlet, oldfreq = find_nth_frequent_ltr(findfreq(message),i)
        message = swap_chars(message, oldlet, key[i])
    return message

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
#####for i in range(26):
#####    print find_nth_frequent_ltr(normal_freqs, i)
#####    print find_nth_frequent_ltr(findfreq(codedmessage), i)
#####thisscore = 301
while thisscore < 500 and p<1000000:
    c=0
    #thiskey = bestkey
    #thiskey=twiddle_key(bestkey, oc, nc)
    print "Attempting..."
    thisattempt = attempt_break(str(codedmessage), thiskey)
    attemptedkeys.append(thiskey)
    print "Num attempted keys: " , len(attemptedkeys)
    print "thisattempt : " , thisattempt
    thisscore = fitsenglish(thisattempt, engsrc)

    print "Best score: \t" , bestscore , "This score: \t" , thisscore
#    print crapletters
    if thisscore >= bestscore:
#        print thiskey
#        print bestkey
        bestscore = thisscore
        bestkey = thiskey
#        codedmessage = thisattempt
        print " ** New bestkey ** " , bestkey
    else:
        #while thiskey in attemptedkeys:
        c+=1
        thiskey=twiddle_key(bestkey)
#            print thiskey
#            print "Dupe: " , c
#        print "Aw"
    thiskey=twiddle_key(bestkey)
#    print thiskey
#    print attemptedkeys
#    codedmessage = thisattempt
    p+=1



print "seedkey: " , bestkey
print "decoded: " , codedmessage
