n=int(input("enter the rows"))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(" ",end='')
    for col in range(1,n-row+2):
        print(row,end='')
    print()            
        

        
