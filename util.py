def test():
    print ("Test succes!")
    
from math import sqrt

def is_prime(num):
    result = True
    i = 2
    while ((num == 1) or i < ((num/2)+1)) and (result == True):
        if (num %i == 0) or (num == 1):
            result = False
        else:
            i += 1
    return result

def find_factor(num):
    i = int(sqrt(num)+1)
    while i > 0:
        if (num %i == 0) and is_prime(i):
            answer = int(i)
            break
        else:
            i -= 1
    else:
        answer = int(num)
    return (answer)

def find_factors(num):
    i = num
    factors = []
    while i != 1:
        new_factor = find_factor(i)
        factors.append(new_factor)
        i /= new_factor
    return factors

def gcd(x,y):
    i = max(x,y)
    j = min(x,y)
    while j != 0:
        remainder = i % j
        i = j
        j = remainder
    return int(i)
    
def lcm(x,y):
    if x != 0 and y != 0:
        return int(abs(x*y)/gcd(x,y))

def divisors(num):
    limit = int(sqrt(num))
    divisors_list = []
    for i in range(1,limit):
        if num % i == 0:
            divisors_list.append(i)
            if i != num/i:
                divisors_list.append(num/i)
    return len(divisors_list)