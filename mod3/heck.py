import Image, os, hashlib, binascii, sys
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

aesmode = sys.argv[1]
password = sys.argv[2]
imagein = sys.argv[3]
imageout = sys.argv[4]

im = Image.open(imagein)
#im = Image.open('mathcat.png')
im_arr = im.load()
im_str = im.tobytes()
im_x, im_y = im.size
im_size = im_x, im_y
im_mode = im.mode
#print len(im_str)
#print AES.block_size

ourkey = hashlib.sha256(password).digest()
#print ourkey.hexdigest()


if len(im_str) % AES.block_size != 0:
    print "hereIam"
    im_strln = len(im_str)
    print im_strln
    im_strpad = AES.block_size - im_strln % AES.block_size
    print im_strpad
    im_str += im_strpad * "~"


if aesmode == 'ECB':
    ouraes = AES.new(ourkey, AES.MODE_ECB)
    im_enc =ouraes.encrypt(im_str)
elif aesmode == 'CTR':
#    ourIV = binascii.hexlify(os.urandom(AES.block_size))
#    print "ourIV: " , ourIV
    ctr = Counter.new(128)
    ouraes = AES.new(ourkey, AES.MODE_CTR, counter=ctr)
    im_enc = ouraes.encrypt(im_str)
else:
    print "I don't speak spanish.\n"
    exit (1)

Image.frombytes(im_mode, im_size, im_enc).save(imageout)

#print im_enc
#print im_str
##print im_mode
##print im_x, im_y

#print im_enc

#for xrang in range(im_x):
#    for yrang in range(im_y):
#        print im_arr[xrang, yrang]


encim = Image.open(imageout)
encim.show()
#decr= ouraes.decrypt(im_enc)
