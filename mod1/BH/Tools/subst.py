import sys, re, itertools, pickle, random
from collections import Counter
from cpeglibs import *

def rotateall(message):
    for all in range(26):
        i=0
        shift = all
        outputed=[]
        while i < len(message):
            #print inputed[i]
            x = ord(message[i])
            if x == 32:
                outputed.append(chr(x))
            else:
                outputed.append(chr(97 +(x + shift) %26))
        #    print outputed[i]
            i=i+1
        print all, ":\t" , ''.join(outputed)

def newkey():
    letters = range(26)
    random.shuffle(letters)
    return letters

def attempt_break(message):
    p=0
    shuffle_crap = []
    shuffle_crap=newkey()
    while (any(shuffle_crap in crap_keys for shuffle_crap in crap_keys)) or p==1:
        p=1
        print shuffle_crap

    attempt = message
#    print attempt
#    print letters
    for i in shuffle_crap:
        pt = chr(97+i)
        attempt = attempt.replace(pt, chr(97+letters[i]))
#    print attempt
    return attempt, shuffle_crap

fh=sys.argv[1]
codedmessage=readfile(fh)

print codedmessage
#rotateall(codedmessage)
attempt_score = 0
crap_keys=[]
p=0
while (attempt_score < 1000):   
    attempt , shuffle_crap =attempt_break(codedmessage)
    crap_keys.append(shuffle_crap)
    attempt_score = fitsenglish(attempt)
    p+=1
#    print attempt
    print p , " \t" , attempt_score

print "Winner: \n" , attempt , "\nScore: \t " , attempt_score