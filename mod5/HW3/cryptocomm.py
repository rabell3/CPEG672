#!/usr/bin/env python

import os, hashlib, binascii, sys, argparse, socket

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from colorama import *

unsecPort = 1651
encryPort = 1672

ourparams = {'Gener': (2909726711393360238997027325079981094903293083416277207163191533186952179846948691035435651273252692731060457249729605513129233502615507099213961913121214831097565254790425L, 3366174731810125753087813209708676894833150358595778752145226712858102783612277607950241452090192525005883890170639174605150394168627448707126811848455102037101825665712475L), 'B': 2853329245261343535560086964181551296889298776106832980891560850944180011701123307905326019642652653533003482753023669016842884108172514870944140611113679225347419720217210L, 'Polyn': 7729075046034516689390703781863974688597854659412869997314470502903038284579120849072387533163845155924927232063004354354730157322085975311485817346934161497393961629647909L, 'Order': 3864537523017258344695351890931987344298927329706434998657235251451519142289560424536143999389415773083133881121926944486246872462816813070234528288303332411393191105285703L}

def genECCpriv(inBits):
    return os.urandom(inBits*)

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

if mode == 's':
    servermode(unsecPort)
elif mode == 'c':
    clientmode(unsecPort, server)

print ourparams

print('All done now.')

