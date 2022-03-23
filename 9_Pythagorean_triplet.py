from datetime import datetime
startTime = datetime.now()

a = 0
b = 0
c = 0

for m in range(2,50):
    for n in range(1,m):
        #print("m is {0}.".format(m))
        #print("n is {0}.".format(n))
        HalfSum = m**2+m*n
        #print(HalfSum)
        if HalfSum == 500:
            a = m**2-n**2
            b = 2*m*n
            c = m**2+n**2
            break
    if a > 0:
        break
product = a*b*c

print(product)

print ("It took {0} to excecute this code.".format((datetime.now() - startTime)))