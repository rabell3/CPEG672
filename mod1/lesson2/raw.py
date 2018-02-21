import hashlib, bcrypt, sys, binascii

mypassword=sys.argv[1]
myhashword=hashlib.sha256(mypassword).hexdigest()

print "Unhashed: " + mypassword
print "Hashed:   " + myhashword

print binascii.b2a_qp(mypassword)

"""
hexascii = myhashword
realhex = hashlib.sha256(mypassword).digest()

binary_for_hexascii = ""
binary_for_realhex = ""

for character in hexascii:
	binary_for_hexascii += bin(ord(character))[2:].zfill(8)
for character in realhex:
	binary_for_realhex += bin(ord(character))[2:].zfill(8)

print binary_for_hexascii
print binary_for_hexascii.count('0'), binary_for_hexascii.count('1')

print binary_for_realhex
print binary_for_realhex.count('0'), binary_for_realhex.count('1')

print binascii.b2a_qp(mypassword)
"""