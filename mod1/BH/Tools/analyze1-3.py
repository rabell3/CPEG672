import sys, re, itertools, pickle, random
from collections import Counter
from cpeglibs import *

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}
tolerance = .01
engsrc = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')

def readfile(handle):
    f1=file(handle, 'r')
    words = [word.strip() for word in f1]
    f1.close()

    i=0
    mobytext = {}
    for word in words:
        mobytext[i] =  word
        i=i+1
        #print word

    mobytext = str(mobytext).replace(" ", "")
    mobytext = re.sub(r'[^a-zA-Z ]', '', mobytext)
    return mobytext

def findfreq(message):
    frequency = {}
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(message.count(chr(ascii)))/len(message)

    sum_freqs_squared = 0.0
    for ltr in frequency:
        sum_freqs_squared += frequency[ltr]*frequency[ltr]
    return sum_freqs_squared

def rotate(message):
    for all in range (1, 27):
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
    return outputed

def findstripkey(message):
    frequency = {}
    return_key = 0
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(message.count(chr(ascii)))/len(message)

    sum_freqs_squared = 0.0
    for ltr in frequency:
        sum_freqs_squared += frequency[ltr]*frequency[ltr]

    everykey = []

    for possible_key in range(1, 26):
        sum_f_sqr = 0.0
        for ltr in normal_freqs:
            caesar_guess = shiftBy(ltr, possible_key)
            sum_f_sqr += normal_freqs[ltr]*frequency[caesar_guess]
        if abs(sum_f_sqr - .065) < tolerance:
            return_key = possible_key
            everykey.append(possible_key)
            print "Key is probably: ", possible_key, " f_sqr is ",sum_f_sqr
    return everykey

def findallkeys(message):
    strip={}
    ourkey = []
    keyshift = 9
    keys = []

    while (ourkey==[]) and (9 <= keyshift <= 21):
        for i in range (0, keyshift):
            strip[i] = codedmessage[i::keyshift]
            ourkey=findstripkey(strip[i])
            #print "ourkey " , ourkey
            if ourkey != []:
                keys.append(ourkey)
        keyshift+=1
    return keys

def elmsearch(thislist,offset):
    #print thislist[offset]
    return thislist[offset]


def decode(keys, message):
    decoded = []
    winner = message
    bigscore = 0
    for posskey in keys:
        #for i in range (0, keyshift):
        #    strip[i] = codedmessage[i::keyshift]
        #    ourkey=findkey(strip[i])
        #    if ourkey != 0:
        #        keys.append(ourkey)            
        ##print keys
        count = 0
        posdecoded = []
        while count < len(codedmessage):
            c = codedmessage[count]
            n = ord(posskey[count%len(posskey)])
            #n = 26 - posskey[count%len(posskey)]
            shifted = shiftBy(c, n)
            posdecoded.append(shifted)
            count+=1
        #keyshift+=1
        #print keys
        posdecoded=''.join(posdecoded)
#        print posdecoded
        thisscore = fitsenglish(posdecoded,engsrc)
        if bigscore < thisscore:
            winner = posdecoded
            bigscore = thisscore
    #print "score " ,  bigscore , "winner \n" , winner
    winnertuple = winner , bigscore
    return winnertuple

#----------------------------------------------------------------
#---
#---  Main function
#---
#----------------------------------------------------------------
fh=sys.argv[1]
#keyshift=int(sys.argv[2])
codedmessage=readfile(fh)


#print codedmessage

ourscore = fitsenglish(codedmessage,engsrc)
posskeys = findallkeys(codedmessage)

#    count = 0
#    allkeys = []
#    if len(keys) != 0:
#        while count < len(codedmessage):
#            shifted=shiftBy(codedmessage[count], 26 - keys[count%len(keys)])
#            allkeys.append(shifted)
#            count+=1
#    keyshift+=1
    #print keys
#    print ''.join(allkeys)
print "keys " , posskeys
multicount = 0
for i in range(len(posskeys)):
    if len(posskeys[i]) > 1:
        multicount+=1
print "multicount: " , multicount
allkeys = []

for p_cnt in range(multicount**multicount):
    #print p_cnt
    permu = []
    for i in range(len(posskeys)):
        if len(posskeys[i]) == 1:
            #print posskeys[i]
            permu.append(chr(elmsearch(posskeys[i],0)+97))
        else:
            flip = random.randint(0,1)
            #print flip
#            for j in range(len(posskeys[i])):
#                copy = permu[:]
#                copy.append(chr(elmsearch(posskeys[i],j)+97))
                #multicount+=1
                #print elmsearch(posskeys[i],0)
            permu.append(chr(elmsearch(posskeys[i],flip)+97))
    #            print elmsearch(posskeys[i],1)
#                permu = copy
    key = ''.join(permu)
    print key
    allkeys.append(key)

print len(allkeys)
unique = reduce(lambda l, x: l.append(x) or l if x not in l else l, allkeys, [])

print "Unique " , unique , "\t " , len(unique)

#decryptors = []
#pos=1
#for i in range(len(posskeys)):
#    print "i: " , posskeys[i]
#    for j in range(len(posskeys[i])):
#        print "j: " , posskeys[i]
        #decryptors[pos].append([posskeys[i]])
        #pos+=1
        #decryptors[pos].append[i]

#print "decryptors: " , decryptors

#for rows in posskeys:
#    for cols in posskeys:
#        for elements in cols:
#            print "r :" , rows, "e :" , elements

print "English score: " , ourscore

winner, bigscore =decode(unique, codedmessage)
print "score " ,  bigscore , "\nwinner \n" , winner