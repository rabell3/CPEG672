import binascii
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

mygen = crand(54321)
rands = [mygen.next() for i in range(4)]
#plaintext = "andy rules!!"
ciphertext = "e5d8443c6ac32d3ee5c7398ecf7f9e03f619"

#hexplain = binascii.hexlify(plaintext)
cipherunh = binascii.unhexlify(ciphertext)
hexkey = "".join(map(lambda x: format(x, 'x')[-6:], rands))

print "hexkey :          " , hexkey
print "cipher hexed/orig:" , ciphertext , "\tCipher len: " , len(ciphertext)
print "cipher unhexed:   " , cipherunh
print "\n\n"
intciph = int(ciphertext,16)
print int(hexkey, 16)
print intciph
#print len(intciph)
print len(cipherunh)

### cipher_as_int = int(hexplain, 16) ^ int(hexkey, 16)
plain_as_int = int(cipherunh) ^ int(hexkey, 16)
### cipher_as_hex = format(cipher_as_int, 'x')
plain_as_hex = format(plain_as_int, 'x')