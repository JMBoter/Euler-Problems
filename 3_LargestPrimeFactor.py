from math import sqrt
import util

number = 600851475142
i = int(sqrt(number)+1)
while i > 0:
    if (number %i == 0) and util.is_prime(i):
        #print ("Prime factor found: ", i)
        answer = i
        break
    else:
        i -= 1
else:
    print ("No prime factor found")
print (answer)

#print (find_factors(number))