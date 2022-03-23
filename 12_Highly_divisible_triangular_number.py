from math import sqrt
from util import divisors
from datetime import datetime

def IsTriangular(n):
    a = 0.5*(sqrt(8*n+1)-1)
    remainder = a % int(a)
    return remainder == 0

def LastTerm(n):
    if IsTriangular(n) == True:
        a = 0.5*(sqrt(8*n+1)-1)
        return int(a)
    else:
        return None

startTime = datetime.now()

#First number with 500 divisors
check = 2**4 * 3**4 * 5**4 * 7 * 11

#Find first bigger number that is triangular
while not IsTriangular(check):
    check += 1

#Find last term of this triangular number
SeriesLastTerm = LastTerm(check)

#Check for number of factors and go to the next triangular number
while divisors(check) <= 500:
    check += (SeriesLastTerm + 1)
    SeriesLastTerm += 1
    
print(check)

print ("It took {0} to excecute this code.".format((datetime.now() - startTime)))