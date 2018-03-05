import binascii, sys

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

def keygen(seed):
    mygen = crand(seed)
    rands = [mygen.next() for i in range(4)]
    return "".join(map(lambda x: format(x, 'x')[-6:], rands))


def encrypt(plaintext, key):
    hexplain = binascii.hexlify(plaintext)
    
    cipher_as_int = int(hexplain, 16) ^ int(key, 16)
    cipher_as_hex = format(cipher_as_int, 'x')
    return cipher_as_hex

def decrypt(enciphered, key):
    plain_as_int = int(enciphered, 16) ^ int(key, 16)
    plain_as_hex = format(plain_as_int, 'x')

    print plain_as_int
    print plain_as_hex

    return binascii.unhexlify(plain_as_hex)
# --------------------------------------------------------------------------------
# --
# --
# --------------------------------------------------------------------------------
mode = sys.argv[1]
phired = sys.argv[2]
seedval = int(sys.argv[3])
#seedval = 1983
hexkey = keygen(seedval)

if mode == "e" and len(phired) > 0:
    print "Encrypting...\n"
    encoded = encrypt(phired, hexkey)
    print "input:  \t" , phired
    print "key:    \t" , hexkey
    print "encoded:\t" , encoded
    exit
elif mode == "d" and len(phired) > 0:
    print "Decrypting...\n"
    decoded = decrypt(phired, hexkey)
    print "input:  \t" , phired
    print "key:    \t" , hexkey
    print "decoded:\t" , decoded
    exit

if len(phired) <= 0:
    print "Enter text to encipher or decipher.\n"
