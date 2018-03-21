#!/usr/bin/env python

import os, hashlib, binascii, sys, argparse, socket

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from colorama import *

unsecPort = 1651
encryPort = 1672


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


print('All done now.')

