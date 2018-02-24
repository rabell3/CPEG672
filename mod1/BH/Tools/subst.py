import sys, re, itertools, pickle, random, pprint
from collections import Counter
from cpeglibs import *

tolerance = 0.03

def findkey(message):
    frequency = {}
    return_key = 0
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(message.count(chr(ascii)))/len(message)

    sum_freqs_squared = 0.0
    for ltr in frequency:
        sum_freqs_squared += frequency[ltr]*frequency[ltr]

    for possible_key in range(1, 26):
        sum_f_sqr = 0.0
        for ltr in normal_freqs:
            caesar_guess = shiftBy(ltr, possible_key)
            sum_f_sqr += normal_freqs[ltr]*frequency[caesar_guess]
        if abs(sum_f_sqr - .065) < tolerance:
            return_key = possible_key
            print "Key is probably: ", possible_key, " f_sqr is ",sum_f_sqr
    return return_key

def attempt_break(message, key):
    print "message: -- \m" , message
    attempt = message
    for i in range(len(message)):
        #print ord(message[i])
        ri = chr(ord(message[i]))
        #print "ri " , ri
        for j in key:
            rj = chr(97+j)
            #print "rj " , rj
            attempt = attempt.replace(ri, rj)
            #attempt = attempt.replace(pt, message[i])
    #print attempt
    return attempt

def newkey():
    letters = range(26)
    random.shuffle(letters)
#    letters = letters.replace(ord(chr('e')),ord(chr('e')))
    return letters

fh=sys.argv[1]
codedmessage=readfile(fh)
attempted_keys =[]

print codedmessage
#rotateall(codedmessage)
attempt_score = 0

pprint.pprint(normal_freqs)
ourfreqs = findfreq(codedmessage)
ourcounts = lettercount(codedmessage)
pprint.pprint(ourfreqs)
pprint.pprint(ourcounts)


#thiskey=newkey()
#thisattempt=attempt_break(codedmessage, thiskey)

thiskey =[]
#print attempt_break(codedmessage, thiskey)
p=0
while (attempt_score < 500):
    thiskey=newkey()
    attempt_score = 0
#    print thiskey
#    thiskey = [2, 9, 13, 17, 4, 3, 19, 23, 11, 8, 10, 14, 18, 0, 6, 24, 25, 20, 15, 1, 12, 21, 16, 5, 22, 7]
    #thiskey = [18, 21, 8, 12, 19, 1, 14, 10, 3, 23, 22, 0, 9, 4, 15, 11, 24, 17, 6, 13, 16, 5, 2, 7, 20, 25]

    thisattempt=attempt_break(codedmessage, thiskey)
    attempt_score = fitsenglish(thisattempt)
    attempted_keys.append(thiskey)
    p+=1
    print thisattempt
    print p , " \t" , attempt_score

print "Winner: \n" , thisattempt , "\nScore: \t " , attempt_score , "\nthis key: \n" , thiskey