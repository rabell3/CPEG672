import sys

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
num_in = int(sys.argv[2])

print "message1 \t" ,  msg_in
print "message2 \t" ,  num_in
hexstr1 = msg2hex(msg_in)
#hexstr2 = int2hex(num_in)
print "hexstr1 \t" , hexstr1
#print "hexstr2 \t" , hexstr2
integer_m1 = hex2int(hexstr1)
#integer_m2 = hex2int(hexstr2)
print "integer1 \t" , integer_m1
#print "integer2 \t" , integer_m2

result = integer_m1 ^ num_in

print hex2msg(int2hex(result))


"""
back2hex = int2hex(integer_m)
back2hex = int2hex(integer_m)
print "back2hex \t" , back2hex
print "back2hex \t" , back2hex
plaintext = hex2msg(back2hex)
plaintext = hex2msg(back2hex)
print "orig msg \t" , plaintext
"""