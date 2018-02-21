import hashlib
import bcrypt
import sys

bcrypt.gensalt()
mypassword=sys.argv[1]
#mysalt=bcrypt.gensalt()
mysalt=sys.argv[2]

print mypassword+mysalt

print hashlib.sha512(mypassword+mysalt).hexdigest()
