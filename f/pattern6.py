n=int(input("enter the rows"))
for row in range(0,n):
    for col in range(0,n-row):
        print(" ",end=" ")
    for col in range(0,2*row+1):
        print("*",end=" ")
    
    print()


        
    
