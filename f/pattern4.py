n=int(input("enter the rows"))
c=65
for row in range(1,n+1):
    for col in range(1,row+1):
    
        print(chr(c),end='')
        c=c+1
    for col in range(1,n-row+2):
        print(" ",end='')
    print()            
        

        
