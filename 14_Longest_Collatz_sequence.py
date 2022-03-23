from datetime import datetime

def Collatz(num):
    seq = [num]
    while num > 1:
        if num % 2 == 0:
            num = int(num/2)
        else:
            num = int(3*num+1)
        seq.append(num)
    return(seq)

startTime = datetime.now()

LengthLongestCollatz = 1
i = 1

while i < 1000000:
    collatz = Collatz(i)
    length = len(collatz)
    if length > LengthLongestCollatz:
        result = i
        LengthLongestCollatz = length
        LongestCollatz = collatz
    i += 1

print ("The longest Collatz sequence starts at {0},".format(result))
#print ("has a length of {0}".format(length))
#print ("and is given by {0}.".format(LongestCollatz))

print ("It took {0} to excecute this code.".format((datetime.now() - startTime)))