import hashlib, bcrypt, array, sys


#bcrypt.gensalt()
mypassword=sys.argv[1]
#mypassword="pass1234"
#mysalt=bcrypt.gensalt()
mysalt=sys.argv[2]
r=int(sys.argv[3])

#print mypassword+mysalt
#print hashlib.sha256(mypassword).hexdigest()

x={}
x[0]="0"
for i in range(0,r):
#    print i
    x[i+1] = hashlib.sha256(x[i] + mypassword + mysalt).digest()

print hashlib.sha256(x[i] + mypassword + mysalt).hexdigest()