from math import sqrt

def SumPrimes(n):
    primes = [2]
    i = 3
    while i < n:
        for j in primes:
            is_prime = True
            if j > sqrt(i):
                break
            elif i %j == 0:
                is_prime = False
                break
        if is_prime == True:
             primes.append(i)
        i += 2
    return sum(primes)

from datetime import datetime
startTime = datetime.now()

print (SumPrimes(2000000))
print ("It took {0} to excecute this code.".format((datetime.now() - startTime)))