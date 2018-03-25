#!/usr/bin/env python
# From: http://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
import socket
from cry import *
from threading import Thread
from SocketServer import ThreadingMixIn

netPort = 1672

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True :
            data_in = conn.recv(2048)
            print "Server received data:", data_in
            MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            conn.sendall(MESSAGE)  # echo

#----------------------------------------------------------------------------
## Lets generate our keys
print "Generating keys..."
myp, myBase, myPubA, myPrivKey = genECCpriv()   # Our private key first
myPubKey = genECCpub(myPrivKey)   # Our public key seconmd
#print "private key: \t" , myPrivKey
#print "public Key:\t", myPubKey

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = netPort
BUFFER_SIZE = 2000  # Usually 1024, but we need quick response ** Changed to match client.

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    print "Multithreaded Python server : Waiting for connections from TCP clients..."
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
