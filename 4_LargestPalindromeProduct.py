i = 999**2
answer = 0
while answer == 0 and i >= 100**2:
    to_check = str(i)
    reverse = to_check[::-1]
    if (to_check == reverse):
        #print ("Palindrome found: ",to_check)
        j = 999
        while j >= 99:
            if (i %j == 0) and (len(str(int(i/j))) == 3):
                #print ("Palindrome :", i, "Divider: ", j, "Rest: ", i%j, "Length: ", len(str(int(i/j))))
                answer = to_check
                break
            j -= 1
        else:
            i -= 1
    else:
        i -= 1

print (answer)