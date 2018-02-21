import hashlib, bcrypt, array, time, sys

hashtuple = (0,0,0)

def create_tuple(inpass):
    # define vars
    mysalt=bcrypt.gensalt()
    r=0
    i=0
    x={}
    x[0]="0"
    starttime = time.clock()
    thistime = 0
    while (thistime - starttime) < 1:
        r=r+1
        x[r] = hashlib.sha256(x[i] + mypassword + mysalt).digest()
        thistime = time.clock()
    myhash = hashlib.sha256(x[i] + mypassword + mysalt).hexdigest()
    hashtuple = mysalt, r, myhash
    return hashtuple

mypassword=sys.argv[1]

mysalt, r, myhash = create_tuple(mypassword)
print "mypass: " , mypassword , "\nmysalt: " , mysalt , "\nr val: " , r , "\nmyhash: " , myhash
