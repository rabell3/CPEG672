import sys, re
from collections import Counter

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

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

def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))

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

def findkey(message):
    frequency = {}
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
        if abs(sum_f_sqr - .065) < .005:
            return_key = possible_key
            print "Key is probably: ", possible_key, " f_sqr is ",sum_f_sqr
    return return_key

#def procmsgs(message)
#
#    return return_msg

fh=sys.argv[1]
keyshift=int(sys.argv[2])
codedmessage=readfile(fh)

keymessages={}

print codedmessage
#for i in range (0, len(codedmessage)):
#        if i % 10 == 0:
#            print codedmessage[i] #+ "\n\n"
##print "Freq b4 key shift: " , str(findfreq(codedmessage))
##print "Shift amount: " , keyshift
##shifted=codedmessage[::keyshift]
#print codedmessage[2]
##print shifted + "\n\n   "
#print shifted[2]
##print "Freq aFt key shift: " , str(findfreq(shifted))
##print Counter(shifted)
##print "length: ", len(shifted)
##ourkey=findkey(shifted)
##print ourkey
##print chr(ourkey+97)
#print "Plaintext: ", rotate(shifted)


for i in range (0, keyshift):
    newstring = []
    workit = codedmessage
    workit = workit[i::keyshift]
    keymessages[i] = workit
    ourkey=findkey(keymessages[i])
    for ltr in keymessages[i]:
        newstring.append(shiftBy(chr(ourkey), ord(ltr)))
    print chr(ourkey+97)
    print keymessages[i], "# ", len(keymessages[i])

print len(keymessages)
#print keymessages