import binascii, os, sys, hashlib

def msg2hex(message):
    return message.encode('hex')

def hex2int(message):
    return int(message, 16)

def int2hex(message):
    return format(message, 'x')

def hex2msg(message):
    evenpad = ('0' * (len(message) % 2)) + message
    return evenpad.decode('hex')

msg_in = sys.argv[1]
ourrand = str(os.urandom(9))

print "message1 \t" ,  msg_in
print "message2 \t" ,  ourrand
hexstr1 = msg2hex(msg_in)
hexstr2 = msg2hex(ourrand)
print "hexstr1 \t" , hexstr1
print "hexstr2 \t" , hexstr2
integer_m1 = hex2int(hexstr1)
integer_m2 = hex2int(hexstr2)
print "integer1 \t" , integer_m1
print "integer2 \t" , integer_m2

result = integer_m1 ^ integer_m2
hexed = str(hex2msg(int2hex(result)))

print hashlib.sha256(hexed).hexdigest()
