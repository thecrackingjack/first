for row in range(0,13):
    for col in range(0,13):
        if(row<13//2):
            if(col<13//2):
                if(col==0):
                    print("*",end='')
                else:
                    print(" ",end='')
            elif(col==13//2):
                    print("*",end='')
            else :
                if(row==0):
                    print("*",end='')
            
        elif(row==13//2):
            print("*",end='')
        else:
            if(col==13//2 or col==13-1):
                 print("*",end='')
            elif(row==13-1):
                if(col<=13//2 or col==0):
                     print("*",end='')
                else:
                     print(" ",end='')
            else:
             print(" ",end='')
    print()             
            
