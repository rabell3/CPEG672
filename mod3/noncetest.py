import os, hashlib, binascii
#nonce = os.urandom(6)
nonce = "cc4304c09aee"
hexnonce = binascii.hexlify(nonce)
oursecret = 54321
concatenated_hex = hexnonce + format(oursecret, 'x')
even_length = concatenated_hex.rjust(len(concatenated_hex) + len(concatenated_hex) % 2, '0')
hexhash = hashlib.sha256(binascii.unhexlify(even_length)).hexdigest()
newseed = (int(hexhash, 16)) % 2**32

print newseed