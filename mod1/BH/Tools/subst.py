import sys, re, itertools, pickle, random, pprint, os
from collections import Counter
from cpeglibs import *

tolerance = 0.0003

def attempt_break(message, key, engsrc):
    cnt = 0
#    print "message: " , message
    attempt = message
    listchars=[]
    newchar = ''
    while cnt <26:
        oldchar = chr(cnt+97) #old letter
        while newchar in listchars:
            newchar = chr(random.randint(97,122))
#        print newchar
        #for j in key:
        #    rj = chr(97+j) #key / new letter
        #    print "ri " , ri
        #    print "rj " , rj
        swap_chars(message, oldchar, newchar)
        cnt+=1
        listchars.append(newchar)
#    print attempt
#    print "a"
    score = fitsenglish(attempt, engsrc)
    results = attempt, score
    return results

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

    print d1.items()
    print d2.items()

    pprint.pprint(d2)

    for i, j in d1.items():         # normal iterator
        for k, l in d2.items():     # our iterator
            if ((float(l)-j)/j)*100 <=tolerance:
                print i, k
            """
            if (abs(float(j)-float(l)) <= tolerance):
                print "awyeah" , i ,  j , " " , k , l
                True
            else:
                #print "oh man"
                False
            """

#            print d1[key]
#            print d2[key]
#            if d1[value] == d2[value]:
#                print "something"
#                result_dictionary[key] = d1[key]
    bestkey = "hello"
    #for index in range(26):
    #    print d1.values(index)
    #    print d2.values(index)
    return bestkey

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

#bestkey=''.join(seedkey(codedmessage))
#bestkey=twiddle_key(bestkey,'z','a')
print bestkey

p=0
# seed thiskey before loop
#thiskey=newkey()
lastscore = 0
thiscore = 0
#print thiskey

thiskey = str(newkey())
thisattempt = codedmessage
oc = 0
nc = 0

while thiscore < 500 and p<1000:
    #os.system('clear')
#    thiskey=newkey()
#    print thiskey
    pprint.pprint(normal_freqs)
    ourfreqs = findfreq(codedmessage)
    pprint.pprint(ourfreqs)

    oc = chr(random.randint(0,26)+97)
    nc = chr(random.randint(0,26)+97)
    print oc
    print nc
    thiskey=twiddle_key(thiskey, oc, nc)

    thisattempt = swap_chars(thisattempt,oc,nc)
    #thisattempt, thiscore = attempt_break(thisattempt, thiskey, engsrc)
    print "Thisattempt:\n" , thisattempt , "\n"
#    thiscore = fitsenglish(thisattempt, engsrc)
    if (thiscore > lastscore):
        bestkey = thiskey
        #print "bestkey " , bestkey
    p+=1
    thisattempt = thisattempt
    #print p , " \t score \t" , thiscore

print "Winner: \n" , thisattempt , "\nScore: \t " , thiscore , "\nthis key: \n" , thiskey
#message_stats(thisattempt)
