import sys, re, urllib2, itertools, pprint, random
from collections import Counter

#bi- and tri-gram frequencies from https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html#Most_common_bigrams_.28in_order.29
normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}
bigram_freqs = {'th': 0.03882543, 'he': 0.03681391, 'in': 0.02283899, 'er': 0.02178042, 'an': 0.02140460, 're': 0.01749394, 'nd': 0.01571977, 'on': 0.01418244, 'en': 0.01383239, 'at': 0.01335523, 'ou': 0.01285484, 'ed': 0.01275779, 'ha': 0.01274742, 'to': 0.01169655, 'or': 0.01151094, 'it': 0.01134891, 'is': 0.01109877, 'hi': 0.01092302, 'es': 0.01092301, 'ng': 0.01053385}
trigram_freqs = {'the': 0.03508232, 'and': 0.01593878, 'ing': 0.01147042, 'her': 0.00822444, 'hat': 0.00650715, 'his': 0.00596748, 'tha': 0.00593593, 'ere': 0.00560594, 'for': 0.00555372, 'ent': 0.00530771, 'ion': 0.00506454, 'ter': 0.00461099, 'was': 0.00460487, 'you': 0.00437213, 'ith': 0.00431250, 'ver': 0.00430732, 'all': 0.00422758, 'wit': 0.00397290, 'thi': 0.00394796, 'tio': 0.00378058} 
quadgram_freqs = {'that': 0.00761242, 'ther': 0.00604501, 'with': 0.00573866, 'tion': 0.00551919, 'here': 0.00374549, 'ould': 0.00369920, 'ight': 0.00309440, 'have': 0.00290544, 'hich': 0.00284292, 'whic': 0.00283826, 'this': 0.00276333, 'thin': 0.00270413, 'they': 0.00262421, 'atio': 0.00262386, 'ever': 0.00260695, 'from': 0.00258580, 'ough': 0.00253447, 'were': 0.00231089, 'hing': 0.00229944, 'ment': 0.00223347}

def readfile(handle):
    f1=file(handle, 'r')
    words = [word.strip() for word in f1]
    f1.close()

    i=0
    filecontent = {}
    for word in words:
        filecontent[i] =  word
        i=i+1

    filecontent = str(filecontent).replace(" ", "")
    filecontent = re.sub(r'[^a-zA-Z ]', '', filecontent)
    return filecontent

def findfreq(message):
    frequency = {}
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(message.count(chr(ascii)))/len(message)
    return frequency

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
        if abs(sum_f_sqr - .065) < .005:
            return_key = possible_key
            print "Key is probably: ", possible_key, " f_sqr is ",sum_f_sqr
    return return_key

def lettercount(message):
    counts = {}
    for ascii in range(ord('a'), ord('a')+26):
        counts[chr(ascii)] = message.count(chr(ascii))
    return counts

def sumfreqs(message):
    frequency = findfreq(message)
    sum_freqs_squared = 0.0
    for ltr in frequency:
        sum_freqs_squared += frequency[ltr]*frequency[ltr]
    return sum_freqs_squared

def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))

def randChar():
    return chr(random.randint(97, 122))

def swap_chars(message, oldlet, newlet): 
    message = message.replace(oldlet, newlet)
    return ''.join(message)

def message_stats(message):
    pprint.pprint(normal_freqs)
    ourfreqs = findfreq(message)
    ourcounts = lettercount(message)

    pprint.pprint(ourfreqs)
    pprint.pprint(ourcounts)
    bicount , tricount, quadcount = findngrams(message)
    print "bi-grams:\t" , bicount
    print "tri-grams:\t" , tricount
    print "quad-grams:\t" , quadcount
    return

def findngrams(message):
    for key in bigram_freqs:
        bicount = message.count(key)
    for key in trigram_freqs:
        tricount = message.count(key)
    for key in quadgram_freqs:
        quadcount = message.count(key)
    ngramtuple = bicount, tricount, quadcount
#    print ngramtuple
    return ngramtuple

def fitsenglish(message, engsrc):
    words = engsrc.read().split()
    
#    print "len before any:       \t" , len(message)

    ourscore = 0

    shortwords = filter(lambda x: 4 >= len(x) > 2, words)
    longerwords = filter(lambda x: 8 >= len(x) > 5, words)
    bigwords = filter(lambda x: len(x) > 9, words)

    bi_pts = 2
    tri_pts = 3
    quad_pts = 4
    short_pts = 5
    long_pts = 15
    big_pts = 100

    bicount , tricount, quadcount = findngrams(message)
    biscore = bicount*bi_pts
    triscore = tricount*tri_pts
    quadscore = quadcount*quad_pts

    ourscore = biscore + triscore + quadscore

#    print message
    for word in bigwords:
        thiscount = message.count(word)
        if thiscount > 0:
            ourscore+=thiscount*big_pts
        message=message.replace(word, '')
        if thiscount != 0:
            print word , " - " , thiscount
#    print "len after big cut:    \t" , len(message)

    for word in longerwords:
        thiscount = message.count(word)
        if thiscount > 0:
            ourscore+=thiscount*long_pts
        message=message.replace(word, '')
        if thiscount != 0:
            print word , " - " , thiscount
#    print "len after longer cut: \t" , len(message)

    for word in shortwords:
        thiscount = message.count(word)
        if thiscount > 0:
            ourscore+=thiscount*short_pts
        message=message.replace(word, '')
        if thiscount != 0:
            print word , " - " , thiscount
#    print "len after short cut: \t" , len(message)
    return ourscore
