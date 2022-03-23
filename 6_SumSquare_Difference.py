def summed_squares(x):
    result = (x*x*x)/3 + (x*x)/2 + x/6
    return int(result)

def sum_squared(x):
    result = (sum(range(x+1)))**2
    return int(result)

from datetime import datetime
startTime = datetime.now()

print (sum_squared(100) - summed_squares(100))
print ("It took {0} seconds to excecute this code.".format((datetime.now() - startTime)))