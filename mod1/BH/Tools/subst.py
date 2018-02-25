import sys, re, itertools, pickle, random, pprint
from collections import Counter
from cpeglibs import *

tolerance = 0.03

def attempt_break(message, key):
    cnt = 0
    print "message: " , message
    attempt = message
    while cnt <26:
        ri = chr(97+cnt)
        for j in key:
            rj = chr(97+j)
            swap_chars(message, rj, ri)
        cnt+=1
#    print attempt
    return attempt

def swap_chars(message, oldlet, newlet): 
    #for chars in message:
    #print "oldlet " , oldlet
    #print "newlet " , newlet
    message = message.replace(oldlet, newlet)
    print "tweaked: " , message
    return message

def newkey():
    letters = range(26)
    random.shuffle(letters)
#    letters = letters.replace(ord(chr('e')),ord(chr('e')))
    return letters

#------------------------------------------------------------------------------------------------------------
#----
#----
#------------------------------------------------------------------------------------------------------------

fh=sys.argv[1]
codedmessage=readfile(fh)
attempted_keys =[]

print "Encoded:\n" , codedmessage , "\n"
#rotateall(codedmessage)
attempt_score = 0

# Very basic stats
ourfreqs = findfreq(codedmessage)
ourcounts = lettercount(codedmessage)

p=0
while (attempt_score < 500):
    attempt_score = 0
    thiskey=newkey()

    thisattempt=attempt_break(codedmessage, thiskey)
#    print "Thisattempt:\n" , thisattempt , "\n"
    attempt_score = fitsenglish(thisattempt)
    attempted_keys.append(thiskey)
    p+=1
    print p , " \t" , attempt_score

print "Winner: \n" , thisattempt , "\nScore: \t " , attempt_score , "\nthis key: \n" , thiskey
message_stats(thisattempt)