import hashlib, bcrypt, sys, binascii

mypassword=sys.argv[1]
myhashword=hashlib.sha256(mypassword).hexdigest()

print "Unhashed:\t" + mypassword
print "Hashed: \t" + myhashword
print "Hexified:\t"
print(binary, myhashword)