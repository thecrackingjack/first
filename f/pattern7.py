n=int(input("enter the rows"))
for row in range(n,0,-1):
    for col in range(0,n-row):
        print(" ",end=" ")
    for col in range(0,2*row-1):
        print("*",end=" ")
    
    print()


        
    
