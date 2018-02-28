def gcd(a,b):
    global counter
    counter+=1
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

counter = 0
print "gcd" , gcd(56,42)
print "count: ", counter
counter = 0
print "gcd" , gcd(8,13)
print "count: ", counter
counter = 0
print "gcd" , gcd(1071,462)
print "count: ", counter
print "gcd" , gcd(222232244629420445529739893461909967206666939096499764990979600,137347080577163115432025771710279131845700275212767467264610201)
print "count: ", counter