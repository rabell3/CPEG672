import os, hashlib, binascii, sys

def crand(seed):
    r=[]
    r.append(seed)
    for i in range(30):
        r.append((16807*r[-1]) % 2147483647)
        if r[-1] < 0:
            r[-1] += 2147483647
    for i in range(31, 34):
        r.append(r[len(r)-31])
    for i in range(34, 344):
        r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
    while True:
        next = r[len(r)-31]+r[len(r)-3] % 2**32
        r.append(next)
        yield (next >> 1 if next < 2**32 else (next - 2**32) >> 1)

def getnewseed(orig_seed, nonce):
    hexnonce = binascii.hexlify(nonce)
    oursecret = orig_seed
    concatenated_hex = hexnonce + format(oursecret, 'x')
    even_length = concatenated_hex.rjust(len(concatenated_hex) + len(concatenated_hex) % 2, '0')
    hexhash = hashlib.sha256(binascii.unhexlify(even_length)).hexdigest()
    newseed = (int(hexhash, 16)) % 2**32
    return newseed

def keygen(seed, num):
    #num = 4
    mygen = crand(seed)
    rands = [mygen.next() for i in range(num)]
    print rands
    return "".join(map(lambda x: format(x, 'x')[-6:], rands))

def encrypt(plaintext, key):
    hexplain = binascii.hexlify(plaintext)
    cipher_as_int = int(hexplain, 16) ^ int(key, 16)
    cipher_as_hex = format(cipher_as_int, 'x')
    return cipher_as_hex

def decrypt(enciphered, key):
    plain_as_int = int(enciphered, 16) ^ int(key, 16)
    plain_as_hex = format(plain_as_int, 'x')
    print "plain \t\t", plain_as_int
    print "hexed \t\t", plain_as_hex
    decrypted = binascii.unhexlify(plain_as_hex)
    return decrypted

# --------------------------------------------------------------------------------
# --
# --
# --------------------------------------------------------------------------------
mode = sys.argv[1]
inputted = sys.argv[2]
seedval = int(sys.argv[3])
#seedval = 1983

print inputted
print seedval

if mode == "e" and len(inputted) > 0:
    hexkey = keygen(seedval,'')
    print "Encrypting...\n"
    encoded = encrypt(inputted, hexkey)
    print "input:  \t" , inputted
    print "key:    \t" , hexkey
    print "encoded:\t" , encoded
    exit
elif mode == "d" and len(inputted) > 0:
    ournonce = inputted[0:12]
    ourcrypt = inputted[12:]
    ourcryptlen = len(ourcrypt)
#    print len(ourcrypt)
    ourseed = getnewseed(seedval,ournonce)
    hexkey = keygen(ourseed,ourcryptlen/4)
    print "Decrypting with nonce %s...\n" % ournonce
    decoded = decrypt(ourcrypt, hexkey)
    print "cipher:  \t" , ourcrypt
    print "key:    \t" , hexkey
    print "decoded:\t" , decoded
    exit

if len(inputted) <= 0:
    print "Enter text to encipher or decipher.\n"
