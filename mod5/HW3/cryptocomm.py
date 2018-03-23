#!/usr/bin/env python

import os, hashlib, binascii, sys, argparse, socket, random
import numpy
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import *
from colorama import *

unsecPort = 1651
encryPort = 1672

#ourparams = {'Gener': (2909726711393360238997027325079981094903293083416277207163191533186952179846948691035435651273252692731060457249729605513129233502615507099213961913121214831097565254790425L, 3366174731810125753087813209708676894833150358595778752145226712858102783612277607950241452090192525005883890170639174605150394168627448707126811848455102037101825665712475L), 'A': 1 , 'B': 2853329245261343535560086964181551296889298776106832980891560850944180011701123307905326019642652653533003482753023669016842884108172514870944140611113679225347419720217210L, 'Polyn': 7729075046034516689390703781863974688597854659412869997314470502903038284579120849072387533163845155924927232063004354354730157322085975311485817346934161497393961629647909L, 'Order': 3864537523017258344695351890931987344298927329706434998657235251451519142289560424536143999389415773083133881121926944486246872462816813070234528288303332411393191105285703L}
ourparams = {'Prime': 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151L, 'A': 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057148L, 'Gener': (2661740802050217063228768716723360960729859168756973147706671368418802944996427808491545080627771902352094241225065558662157113545570916814161637315895999846L, 3757180025770020463545507224491183603594455134769762486694567779615544477440556316691234405012945539562144444537289428522585666729196580810124344277578376784L), 'B': 1093849038073734274511112390766805569936207598951683748994586394495953116150735016013708737573759623248592132296706313309438452531591012912142327488478985984L, 'Order': 6864797660130609714981900799081393217269435300143305409394463459185543183397655394245057746333217197532963996371363321113864768612440380340372808892707005449L}


def genECCpriv():
    thisgcd = 0
    while thisgcd != 1:
        p = ourparams["Prime"]
        a = getRandomRange(2, ourparams["Order"])
        thisgcd = GCD(a, p-1)
        sys.stdout.write('.')
        #loop until you get a GCD of 1 with p-1
    sys.stdout.flush()
    print thisgcd
    base = 2
    A = pow(base, a, p)
    print "a (!!):\t" , a
    print "p: \t" , p, "\n" , "base: \t" , base, "\n", "A: \t" , A
    return a


def calcpower(b, p):
    """
    From https://stackoverflow.com/questions/1019740/speed-of-calculating-powers-in-python
    Calculates b^p
    Complexity O(log p)
    b -> double
    p -> integer
    res -> double
    """
    res = 1

    while p:
        if p & 0x1: res *= b
        b *= b
        p >>= 1

    return res





#def genECCpriv():
#    return random.randrange(0,ourparams["Order"])

def servermode(portIn):
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = portIn               # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        c.send('Thank you for connecting')
        c.close()                # Close the connection

def clientmode(portIn, hostIn):
    s = socket.socket()         # Create a socket object
    #host = socket.gethostname() # Get local machine name
    host = hostIn
    port = portIn                # Reserve a port for your service.

    s.connect((host, port))
    print s.recv(1024)
    s.close                     # Close the socket when done

# ------------------------------------------------------------------

mode = sys.argv[1]
server = sys.argv[2]

init(autoreset=True)
print(Fore.RED + 'Connecting to: '), (Fore.BLUE + '%s') % server

#if mode == 's':
#    servermode(unsecPort)
#elif mode == 'c':
#    clientmode(unsecPort, server)

#for key in ourparams:
#    print key ," -> ", ourparams[key]
da = genECCpriv()
#da = os.urandom(random.randrange(ourparams["Order"]))
print da
print "pubKey:\t", numpy.dot(da,ourparams["Gener"])
print('All done now.')

