fibonacci = [1, 2]

i = 0
while fibonacci[i+1] < 4000000:
    next = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(next)
    i += 1
    
#print (fibonacci)

sum_even = 0
for i in range (0,len(fibonacci)-1):
    if fibonacci[i] %2 == 0:
        sum_even += fibonacci[i]

print (sum_even)