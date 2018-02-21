import sys
import hashlib

f1=file(sys.argv[1], 'r')
words = [word.strip() for word in f1]
f1.close()

f2=file(sys.argv[2], 'r')
mysecret = f2.readline()
print(mysecret)
f2.close()

#i = 0
for word in words:
#    i=i+1
#    print(i)
    word_hash = hashlib.sha512(word).hexdigest() 
#    print(word_hash)
    if word_hash == mysecret:
        print("word_hash: ", word_hash, "\t", "word: ", word, "\n")
