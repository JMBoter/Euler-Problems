from datetime import datetime
startTime = datetime.now()

size = 20
paths = (size+1)*[(size+1)*[1]]

for i in range(1,size+1):
    for j in range(1,size+1):
        paths[i][j] = paths[i-1][j] + paths[i][j-1]

print(paths[size][size])

print ("It took {0} to excecute this code.".format((datetime.now() - startTime)))