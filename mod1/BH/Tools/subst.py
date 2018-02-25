import sys, re, itertools, pickle, random, pprint
from collections import Counter
from cpeglibs import *

tolerance = 0.001

def attempt_break(message, key, engsrc):
    cnt = 0
#    print "message: " , message
    attempt = message
    while cnt <26:
        ri = chr(97+cnt)
        for j in key:
            rj = chr(97+j)
            swap_chars(message, rj, ri)
        cnt+=1
#    print attempt
    print "a"
    score = fitsenglish(attempt, engsrc)
    results = attempt, score
    return results

def swap_chars(message, oldlet, newlet): 
    message = message.replace(oldlet, newlet)
    return ''.join(message)

def twiddle_key(key, oldlet, newlet):
    key = key.replace(oldlet, newlet,1)
    key = key.replace(newlet, oldlet,1)
    return ''.join(key)

def newkey():
    letters = range(26)
    random.shuffle(letters)
    return letters

def get_val(dictin, key):
    for k, v in dictin.items():
        if k==key:
            return value

def seedkey(message):
    ourfreqs = findfreq(message)
    ourcounts = lettercount(codedmessage)

    d1 = normal_freqs
    d2 = ourfreqs

    #print set(d1.items())
    #print set(d2.items())

    for i, j in d1.items():
        for k, l in d2.items():
            if (abs(float(j)-float(l)) <= tolerance):
                print "awyeah" , i ,  j , " " , k , l
            else:
                print "oh man"

#            print d1[key]
#            print d2[key]
#            if d1[value] == d2[value]:
#                print "something"
#                result_dictionary[key] = d1[key]

    #for index in range(26):
    #    print d1.values(index)
    #    print d2.values(index)
    return ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#------------------------------------------------------------------------------------------------------------
#----
#----
#------------------------------------------------------------------------------------------------------------
engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
fh=sys.argv[1]
codedmessage=readfile(fh)
bestkey=[]

print "Encoded:\n" , codedmessage , "\n"
#rotateall(codedmessage)
attempt_score = 0

# Very basic stats
ourfreqs = findfreq(codedmessage)
ourcounts = lettercount(codedmessage)

bestkey=''.join(seedkey(codedmessage))
bestkey=twiddle_key(bestkey,'z','a')
print bestkey

p=0
# seed thiskey before loop
#thiskey=newkey()
lastscore = 0
thiscore = 0
#print thiskey
"""
while (thiscore < 500):
    thiskey=newkey()
    
#    print thiskey
    #thiskey=swap_chars(thiskey, randChar(), randChar())

    thisattempt, thiscore = attempt_break(codedmessage, thiskey, engsrc)

#    print "Thisattempt:\n" , thisattempt , "\n"
#    thiscore = fitsenglish(thisattempt, engsrc)
    if (thiscore > lastscore):
        bestkey = thiskey
        print "bestkey " , bestkey
    p+=1
    print p , " \t score \t" , thiscore

print "Winner: \n" , thisattempt , "\nScore: \t " , thiscore , "\nthis key: \n" , thiskey
message_stats(thisattempt)
"""