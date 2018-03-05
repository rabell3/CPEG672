import time
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

seed=int(time.time())
#mygen = crand(seed)
mygen = crand(1983)
#print "Seed: " , seed, "\nmygen: " , mygen
firstfour = [mygen.next() for i in range(4)]
print firstfour

temp = mygen.next()
temp1 = temp % 2**8
temp2 = (temp >> 8) % 2**8
temp3 = (temp >> 16) % 2**8
temp4 = (temp >> 24) % 2**8

print temp
print temp1
print temp2
print temp3
print temp4
