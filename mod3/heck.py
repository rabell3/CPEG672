import Image, os, hashlib, binascii, sys
from Crypto import Random
from Crypto.Cipher import AES

im = Image.open('heckert_gnu.png')
#im = Image.open('mathcat.png')
im_arr = im.load()
im_x, im_y = im.size
im_mode = im.mode

print AES.block_size

ourkey = hashlib.sha256('password').digest()
#print ourkey.hexdigest()
ourIV = os.urandom(AES.block_size)
ouraes = AES.new(ourkey, AES.MODE_ECB, ourIV)
msg = ourIV + ouraes.encrypt(b'holybananahamock')

print msg
print im_arr
print im_mode
print im_x, im_y

#for xrang in range(im_x):
#    for yrang in range(im_y):
#        print im_arr[xrang, yrang]



#im.show()
print ouraes.decrypt(msg)