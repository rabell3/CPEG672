def c2i(character):
    return ord(character)-ord('A')

def i2c(encoded):
    return chr(ord('a') + encoded)
    
def hill_enc(plain):
    found = False
    a=1
    b=1
    c=1
    d=1
    while not found:
        a,b,c,d = [random.randint(0,25) for i in range(4)]
        det = (a*d - b*c) % 26
        det2 = ((a-1)*d - b*(c-1)) % 26
        if (det % 2 != 0 )and (det % 13 != 0) and (det2 % 26 != 0):
            found = True
    secret = ''
    for i in range(0, len(plain), 2):
        i1 = c2i(plain[i])
        i2 = c2i(plain[i+1])
        c1 = (i1*a + i2*b) % 26
        c2 = (i1*c + i2*d) % 26
        secret += i2c(c1) + i2c(c2)
    return secret, [a,b,c,d]

def hill_dec(cipher):
    found = False
    a=1
    b=1
    c=1
    d=1
    while not found:
        a,b,c,d = [random.randint(0,25) for i in range(4)]
        det = (a*d - b*c) % 26
        det2 = ((a-1)*d - b*(c-1)) % 26
        if (det % 2 != 0 )and (det % 13 != 0) and (det2 % 26 != 0):
            found = True