#!/usr/bin/env python

import os, hashlib, binascii, sys, argparse, socket, random, pickle
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import ECC
from Crypto.Util import Counter
from Crypto.Util.number import *
from colorama import *
#from rosecode import *

srvPort = 1672

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
#    print "a (!!):\t" , a
#    print "p: \t" , p, "\n" , "base: \t" , base, "\n", "A: \t" , A
    privtup = p, base, A, a
    return privtup

def genECCpub(inprivkey):
    pubX = inprivkey * ourparams["Gener"][0]
    pubY = inprivkey * ourparams["Gener"][1]
    return pubX, pubY

def genSharedSecret(inprivkey, inpubkey):
    return inprivkey*inpubkey[0]   #returns x-coordinate only

def servermode(portIn, pubkey, inpriv):
    s = socket.socket()         # Create a socket object
#    host = socket.gethostname() # Get local machine name
    host = ''
    myname = os.uname()[1]
    port = portIn               # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
#        print(Fore.BLUE + 'Got connection from: '), (Fore.YELLOW + '%s') % addr
#        print 'Got connection from', addr
#        print c
        r_data = pickle.loads(c.recv(1024))
#        r_data =c.recv(1024)
        print(Fore.BLUE + 'Received: '), (Fore.YELLOW + '%s') % r_data
        r_pub = r_data
#        print "r_pub " , r_pub
#        print "r_pubX: " , r_pub[1]
    
        print "Sending public: %s" % str(pubkey)
        pkt_data = "pubkey" , pubkey[0], pubkey[1]
#        c.sendall(pickle.dumps(pkt_data))
        c.sendall(pkt_data)

        sharedkey = hashlib.sha256(inpriv*r_pub[0])
        print "Sharedkey: \t " , sharedkey


        print(Fore.BLUE + 'Sending: '), (Fore.YELLOW + '%s') % s_data
        c.send(s_data)
        c.send('Thank you for connecting to %s' % myname)
        c.close()                # Close the connection

def clientmode(portIn, hostIn, pubkey, inpriv):
    s = socket.socket()         # Create a socket object
    #host = socket.gethostname() # Get local machine name
    host = hostIn
    port = portIn                # Reserve a port for your service.

    s.connect((host, port))
    print "Sending public: %s" % str(pubkey)
    pkt_data = "pubkey" , pubkey[0], pubkey[1]
    s.send(pickle.dumps(pkt_data))
#    s.send(pkt_data)
#    r_data = pickle.loads(s.recv(1024))
    r_data =s.recv(1024)
    print(Fore.BLUE + 'Received: '), (Fore.YELLOW + '%s') % r_data
    r_pub = r_data

    sharedkey = hashlib.sha256(inpriv*r_pub[0])
    r_data = c.recv(1024)

    s.close                     # Close the socket when done
"""
def packet_processor(inConn, inPacket):
    if type == "init":
        blah
    elif type == "exch":
        blah
    elif type == "aes_sess":
        blah
    else:
        undefined
    return something
"""
# ------------------------------------------------------------------

mode = sys.argv[1]
server = sys.argv[2]
init(autoreset=True)
s = socket.socket()

myname = os.uname()[1]
## Lets generate our keys
print "Generating keys for %s..." % myname
myp, myBase, myPubA, myPrivKey = genECCpriv()       # Our private key first
myPubKey = genECCpub(myPrivKey)                     # Our public key seconmd
#print "private key: \t" , myPrivKey
#print "public Key:\t", myPubKey



if mode == 's':
    host = ''
    print(Fore.RED + 'Listening on: '), (Fore.BLUE + '%s') % srvPort
    servermode(srvPort, myPubKey, myPrivKey)
    """
    s.bind((host, srvPort))        # Bind to the port    
    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        pkt = c.recv(1024)
        print 'Got connection from', addr
        c.send('Thank you for connecting %s' %pkt)
        c.close()                # Close the connection
    """
elif mode == 'c':
    print(Fore.RED + 'Connecting to: '), (Fore.BLUE + '%s') % server
    clientmode(srvPort, server, myPubKey, myPrivKey)
    """
    s.connect((server, srvPort))
    s.sendall('Hello from %s' % myname)
    print s.recv(1024)
    s.close                     # Close the socket when done
    """

print('All done now.')