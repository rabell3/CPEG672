#from Crypto.Cipher import AES
#import binascii, Crypto


from Crypto.Cipher import AES
from Crypto import Random

key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')

print msg


#AES.new(secret_key)
#print binascii.unhexlify('000102030405060708090a0b0c0d0e0f')
#print binascii.unhexlify('00112233445566778899aabbccddeeff')