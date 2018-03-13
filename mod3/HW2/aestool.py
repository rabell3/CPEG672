import Image, os, hashlib, binascii, sys, argparse
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter


# -------------------------------------------------------------------
# --- General utility functions
# -------------------------------------------------------------------

def filetomemst(filein):
    im = Image.open(filein)
    return im.tobytes()

def memstrtofile(filein, fileout):
    filein, im_mode, im_size
    im = Image.open(filein)
    Image.frombytes(im_mode, im_size, filein).save(fileout)
    return True

def fixpadding(im_str):
    if len(im_str) % AES.block_size != 0:
        #print "hereIam"
        im_strln = len(im_str)
        #print im_strln
        padamt = AES.block_size - im_strln % AES.block_size
        #print padamt
        im_str += padamt * "\0"
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
    im_enc = inIV + ouraes.encrypt(im_str)
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

# -------------------------------------------
# ---
# -------------------------------------------
parser = argparse.ArgumentParser(description='AES Encryption and Decryption tool')
parser.add_argument('-a','--action', help='Set action to encrypt or decrypt', required=True)
parser.add_argument('-m','--mode', help='Specify AES mode: ECB, CTR, CFB, CBC, OFB', required=True)
parser.add_argument('-p','--password', help='Specify a password', required=True)
parser.add_argument('-v','--iv', help='Specify an initialization vector', required=False)
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

if action == "encrypt":
    print "Encrypting..."

#    # Deal with padding/block_size issues
#    if len(im_str) % AES.block_size != 0:
#        #print "hereIam"
#        im_strln = len(im_str)
#        #print im_strln
#        padamt = AES.block_size - im_strln % AES.block_size
#        #print padamt
#        im_str += padamt * "*"
    im_str = fixpadding(im_str) 
    if aesmode == "ECB":
        print "ECB"
#        im_str = fixpadding(im_str)
        processed = encryptECB(im_str, ourkey)
    elif aesmode == "CTR":
        print "CTR"
#        im_str = fixpadding(im_str)
        processed = encryptCTR(im_str, ourkey)
    elif aesmode == "CFB":
        print "CFB"
    elif aesmode == "CBC":
        print "CBC"
#        im_str = fixpadding(im_str) 
        # Deal with IV status
        if type(inIV) == type(None):
            ourIV = binascii.hexlify(os.urandom(AES.block_size))[:16]
        else:
            ourIV = inIV
        print "Our IV: " , ourIV, "\tLen\t" , len(ourIV)
        processed = encryptCBC(im_str, ourkey, ourIV)
    elif aesmode == "OFB":
        print "OFB"
        # Deal with IV status
        if type(inIV) == type(None):
            ourIV = binascii.hexlify(os.urandom(AES.block_size))[:16]
        else:
            ourIV = inIV
        print "Our IV: " , ourIV, "\tLen\t" , len(ourIV)
#        im_str = fixpadding(im_str)
        processed = encryptOFB(im_str, ourkey, ourIV)
elif action == "decrypt":
    print "Decrypting..."
#    # Deal with padding/block_size issues
#    if len(im_str) % AES.block_size != 0:
#        #print "hereIam"
#        im_strln = len(im_str)
#        #print im_strln
#        padamt = AES.block_size - im_strln % AES.block_size
#        #print padamt
#        im_str += padamt * "*"
    im_str = fixpadding(im_str) 

    if aesmode == "ECB":
        print "ECB"
        processed = decryptECB(im_str, ourkey)
    elif aesmode == "CTR":
        print "CTR"
        processed = decryptCTR(im_str, ourkey)
    elif aesmode == "CFB":
        print "CFB"
    elif aesmode == "CBC":
        print "CBC"
#        im_str = fixpadding(im_str) 
        # Deal with IV status
        if type(inIV) == type(None):
            print "Can't decrypt without known IV."
            exit(1)
        else:
            ourIV = inIV
        processed = decryptCBC(im_str, ourkey, ourIV)
    elif aesmode == "OFB":
        print "OFB"
#        im_str = fixpadding(im_str)
        # Deal with IV status
        if type(inIV) == type(None):
            print "Can't decrypt without known IV."
            exit(1)
        else:
            ourIV = inIV
        processed = decryptOFB(im_str, ourkey, ourIV)

print "Saving to file %s..." % imageout
Image.frombytes(im_mode, im_size, processed).save(imageout)

showit = Image.open(imageout)
showit.show()