import util

i = 11
found = False
while (found == False):
    found = True
    for j in range(1,11):
        if i %j != 0:
            found = False
            break
    i += 1
#print (i-1)

def smallest_multiple_upto(x):
    n = 1
    for i in range(1,x+1):
        n = util.lcm(n,i)
    return (n)

print (smallest_multiple_upto(20))