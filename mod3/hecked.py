import Image, os, hashlib, binascii, sys
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

aesmode = sys.argv[1]
crypmode = sys.argv[2]
password = sys.argv[3]
inIV = sys.argv[4]
imagein = sys.argv[5]
imageout = sys.argv[6]

def encryptit(im_str, aesmode, inkey):
    if aesmode == 'ECB':
        ouraes = AES.new(inkey, AES.MODE_ECB)
        im_enc =ouraes.encrypt(im_str)
    elif aesmode == 'CTR':
        ourIV = binascii.hexlify(os.urandom(AES.block_size))
        print "ourIV: " , ourIV
        ctr = Counter.new(128)
        ouraes = AES.new(inkey, AES.MODE_CTR, counter=ctr)
        im_enc = ourIV + ouraes.encrypt(im_str)
    return im_enc

def decryptit(im_str, aesmode, inIV, inkey):
    if aesmode == 'ECB':
        ouraes = AES.new(inkey, AES.MODE_ECB)
        im_dec = ouraes.decrypt(im_str)
    elif aesmode == 'CTR':
        ourIV = inIV
        print "ourIV: " , ourIV
        ctr = Counter.new(128)
        ouraes = AES.new(inkey, AES.MODE_CTR, counter=ctr)
        im_dec = ourIV + ouraes.decrypt(im_str)
    return im_dec
# -------------------------------------------
# ---
# -------------------------------------------

im = Image.open(imagein)
im_arr = im.load()
im_str = im.tobytes()
im_x, im_y = im.size
im_size = im_x, im_y
im_mode = im.mode
#print len(im_str)
#print AES.block_size
ourkey = hashlib.sha256(password).digest()
#print ourkey.hexdigest()
if crypmode == "e" or crypmode == "E":
    print "Encrypting..."
    encrypted = encryptit(im_str, aesmode, ourkey)
    Image.frombytes(im_mode, im_size, encrypted).save(imageout)
elif crypmode == "d" or crypmode == "D":
    print "Decrypting..."
    decrypted = decryptit(im_str, aesmode, inIV, ourkey)
    Image.frombytes(im_mode, im_size, decrypted).save(imageout)
else:
    print "Specify E|e to encrypt, D|d to decrypt."
    exit (1)

# Show it
showit = Image.open(imageout)
showit.show()