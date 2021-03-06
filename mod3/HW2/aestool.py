import Image, os, hashlib, binascii, sys, argparse
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter


# -------------------------------------------------------------------
# --- General utility functions
# -------------------------------------------------------------------

def getIV(inIV,action):
    # Deal with IV status
    if (type(inIV) == type(None)) and action == "encrypt":
        ourIV = binascii.hexlify(os.urandom(AES.block_size))[:16]
    elif (type(inIV) == type(None)) and action == "decrypt":
        print "Can't decrypt without known IV."
        exit(1)
    else:
        ourIV = inIV
    print "Our IV: " , ourIV, "\tLen\t" , len(ourIV)
    return ourIV

def fixpadding(im_str):
    if len(im_str) % AES.block_size != 0:
        im_strln = len(im_str)
        padamt = AES.block_size - im_strln % AES.block_size
        im_str += padamt * "\0"
    else:
        print "No padding necessary."
    return im_str

# -------------------------------------------------------------------
# --- Encryption functions
# -------------------------------------------------------------------
def encryptECB(im_str, inkey):
    ouraes = AES.new(inkey, AES.MODE_ECB)
    im_enc = ouraes.encrypt(im_str)
    return im_enc

def encryptCTR(im_str, inkey):
    ctr = Counter.new(128)
    ouraes = AES.new(inkey, AES.MODE_CTR, counter=ctr)
    im_enc = ouraes.encrypt(im_str)
    return im_enc

def encryptCBC(im_str, inkey, inIV):
    ouraes = AES.new(inkey, AES.MODE_CBC, inIV)
    im_enc = ouraes.encrypt(im_str)
    return im_enc

def encryptOFB(im_str, inkey, inIV):
    ouraes = AES.new(inkey, AES.MODE_OFB, inIV)
    im_enc = ouraes.encrypt(im_str)
    return im_enc

def encryptCFB(im_str, inkey, inIV):
    ouraes = AES.new(inkey, AES.MODE_CFB, inIV)
    im_enc = ouraes.encrypt(im_str)
    return im_enc

# -------------------------------------------------------------------
# --- Decryption functions
# -------------------------------------------------------------------
def decryptECB(im_str, inkey):
    ouraes = AES.new(inkey, AES.MODE_ECB)
    im_dec = ouraes.decrypt(im_str)
    return im_dec

def decryptCTR(im_str, inkey):
    ctr = Counter.new(128)
    ouraes = AES.new(inkey, AES.MODE_CTR, counter=ctr)
    im_dec = ouraes.decrypt(im_str)
    return im_dec

def decryptCBC(im_str, inkey, inIV):
    ouraes = AES.new(inkey, AES.MODE_CBC, inIV)
    im_enc = ouraes.decrypt(im_str)
    return im_enc

def decryptOFB(im_str, inkey, inIV):
    ouraes = AES.new(inkey, AES.MODE_OFB, inIV)
    im_enc = ouraes.decrypt(im_str)
    return im_enc

def decryptCFB(im_str, inkey, inIV):
    ouraes = AES.new(inkey, AES.MODE_CFB, inIV)
    im_enc = ouraes.decrypt(im_str)
    return im_enc

# -------------------------------------------
# --- Main
# -------------------------------------------
parser = argparse.ArgumentParser(description='AES Encryption and Decryption tool')
parser.add_argument('-a','--action', help='Set action to encrypt or decrypt', required=True)
parser.add_argument('-m','--mode', help='Specify AES mode: ECB, CTR, CFB, CBC, OFB', required=True)
parser.add_argument('-p','--password', help='Specify a password', required=True)
parser.add_argument('-v','--iv', help='Specify an initialization vector, for CFB, CBC and OFB modes', required=False)
parser.add_argument('-I','--image-in', help='Specify the input image', required=True)
parser.add_argument('-O','--image-out', help='Specify the output image', required=False)
args = vars(parser.parse_args())

#print args

action = args['action']
aesmode = args['mode']
password = args['password']
inIV = args['iv']
imagein = args['image_in']
imageout = args['image_out']

im = Image.open(imagein)
im_arr = im.load()
im_str = im.tobytes()
im_x, im_y = im.size
im_size = im_x, im_y
im_mode = im.mode

ourkey = hashlib.sha256(password).digest()
print "Key: \t" , binascii.hexlify(ourkey)

if action == "encrypt":
    print "Encrypting..."
    im_str = fixpadding(im_str) 
    if aesmode == "ECB":
        print "ECB"
        processed = encryptECB(im_str, ourkey)
    elif aesmode == "CTR":
        print "CTR"
        processed = encryptCTR(im_str, ourkey)
    elif aesmode == "CFB":
        print "CFB"
        ourIV = getIV(inIV,action)
        processed = encryptCFB(im_str, ourkey, ourIV)
    elif aesmode == "CBC":
        print "CBC"
        ourIV = getIV(inIV,action)
        processed = encryptCBC(im_str, ourkey, ourIV)
    elif aesmode == "OFB":
        print "OFB"
        ourIV = getIV(inIV,action)
        processed = encryptOFB(im_str, ourkey, ourIV)
elif action == "decrypt":
    print "Decrypting..."
    im_str = fixpadding(im_str) 
    if aesmode == "ECB":
        print "ECB"
        processed = decryptECB(im_str, ourkey)
    elif aesmode == "CTR":
        print "CTR"
        processed = decryptCTR(im_str, ourkey)
    elif aesmode == "CFB":
        print "CFB"
        ourIV = getIV(inIV,action)
        processed = decryptCFB(im_str, ourkey, ourIV)
    elif aesmode == "CBC":
        print "CBC"
        ourIV = getIV(inIV,action)
        processed = decryptCBC(im_str, ourkey, ourIV)
    elif aesmode == "OFB":
        print "OFB"
        ourIV = getIV(inIV,action)
        processed = decryptOFB(im_str, ourkey, ourIV)
else:
    print "Action not defined."
    exit(1)

print "Saving to file %s..." % imageout
Image.frombytes(im_mode, im_size, processed).save(imageout)

showit = Image.open(imageout)
showit.show()