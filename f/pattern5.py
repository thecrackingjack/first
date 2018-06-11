n=int(input("enter the rows"))
c=64
for row in range(1,n+1):
    for col in range(1,row+1):
    
        print(chr(c+col),end='')
        
    for col in range(1,n-row+2):
        print(" ",end='')
    print()            
        

        
