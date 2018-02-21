import hashlib
import bcrypt
import array

bcrypt.gensalt()
mypassword="crappy123"
#mypassword="pass1234"
mysalt=bcrypt.gensalt()
#mysalt="somesalt"
r=3

#print mypassword+mysalt
#print hashlib.sha256(mypassword).hexdigest()

x={}
x[0]="0"
for i in range(0,r):
    print i
    x[i+1] = hashlib.sha256(x[i] + mypassword + mysalt).digest()

print hashlib.sha256(x[i] + mypassword + mysalt).hexdigest()