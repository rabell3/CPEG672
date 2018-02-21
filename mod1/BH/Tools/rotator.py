import sys

inputed = sys.argv[1]
#shift = int(sys.argv[2])
print "0:\t" , inputed
i = 0
#outputed=[]

for all in range (0, 26):
    i=0
    shift = all
    outputed=[]
    while i < len(inputed):
        #print inputed[i]
        x = ord(inputed[i])
        if x == 32:
            outputed.append(chr(x))
        else:
            outputed.append(chr(97 +(x + shift) %26))
    #    print outputed[i]
        i=i+1
    print all, ":\t" , ''.join(outputed)