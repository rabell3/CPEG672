#import itertools

def msg2hex(message):
    return message.encode('hex')

def hex2int(message):
    return int(message, 16)

def int2hex(message):
    return format(message, 'x')

def hex2msg(message):
    evenpad = ('0' * (len(message) % 2)) + message
    return evenpad.decode('hex')

a=[0b10110,
0b01010,
0b10001,
0b11011,
0b10000,
0b01100,
0b11001,
0b11100,
0b01011,
0b10001,
0b10101,
0b11111,
0b00001,
0b11101,
0b10111,
0b11110,
0b01110,
0b01001,
0b01000,
0b01101,
0b11101,
0b01111,
0b11000,
0b10100,
0b10011,
0b11010,
0b10001,
0b10001,
0b10010]



def lookup(bin_in):
    ourdict={0b00000 : "a",
    0b00001 : "b",
    0b00010 : "c",
    0b00011 : "d",
    0b00100 : "e",
    0b00101 : "f",
    0b00110 : "g",
    0b00111 : "h",
    0b01000 : "i",
    0b01000 : "j",
    0b01001 : "k",
    0b01010 : "l",
    0b01011 : "m",
    0b01100 : "n",
    0b01101 : "o",
    0b01110 : "p",
    0b01111 : "q",
    0b10000 : "r",
    0b10001 : "s",
    0b10010 : "t",
    0b10011 : "u",
    0b10100 : "v",
    0b10101 : "w",
    0b10110 : "x",
    0b10111 : "y",
    0b11000 : "z"}
    return ourdict.get(bin_in, "na")


#print len(a)
for key in range(0,32):
    for i in range(len(a)):
        ###print "1st \t " , bin(a[i])
        newstring = []
        #print i , "\t" , int(a[i],2)
        #cipher = hex2int(int2hex(int(a[i],2)))
        cipher = a[i]
        ###print "2nd \t " , bin(key)
        #print cipher
        #print key #key = bin('10101')
        deciphered = cipher ^ key
        ###print "3rd \t " , bin(deciphered)
        #ourbyte = hex2msg(int2hex(deciphered))
        ourbyte = deciphered
        if lookup(ourbyte) != "na":
            newstring.append(lookup(ourbyte))
        print newstring
    print "Key ", key , "\n" , ''.join(newstring) , "-------------------\n"