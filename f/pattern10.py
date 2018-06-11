n=int(input("enter the number of rows"))
for row in range(0,n):
    #for col in range(0,row):
       #print(" ",end='')
    for col in range(0,n-row):
        print("*",end='')
    for col in range(0,row):
        print(" ",end=' ')
    for col in range(0,n-row):
        print("*",end='')

    print()

    
for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end='')
    for col in range(1,n-row+1):
        print(" ",end='')
    for col in range(1,n-row+1):
        print(" ",end='')
    for col in range(1,row+1):
        print("*",end='')
    print() 



