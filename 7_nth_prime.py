from math import sqrt

def nth_prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
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
    return primes[n-1]

from datetime import datetime
startTime = datetime.now()

print (nth_prime(10001))
print ("It took {0} to excecute this code.".format((datetime.now() - startTime)))