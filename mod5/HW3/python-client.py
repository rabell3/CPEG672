#!/usr/bin/env python
# Python TCP Client A
# Socket code from: http://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
import socket, sys, os
from cry import *

netPort = 1672


#----------------------------------------------------------------------------
## Lets generate our keys
print "Generating keys..."
myp, myBase, myPubA, myPrivKey = genECCpriv()   # Our private key first
myPubKey = genECCpub(myPrivKey)   # Our public key seconmd
#print "private key: \t" , myPrivKey
#print "public Key:\t", myPubKey

#host = socket.gethostname()
host = sys.argv[1]
myname = os.uname()[1]

port = netPort
BUFFER_SIZE = 2000 
#MESSAGE = raw_input("tcpClientA: Enter message/ Enter exit:")
MESSAGE = "%s-pubkey:" % myname + str(myPubKey)

print MESSAGE
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.sendall(MESSAGE)     
    data_in = tcpClientA.recv(BUFFER_SIZE)
    print " ClientA received data:", data_in
    MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")

tcpClientA.close() 
