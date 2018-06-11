def factorial(num):
    if num==0:
        
        return 1
    elif num==1:
        
        return 1
    elif num==2:
        return 2
    elif num>2:
        s=1
        for var in range(num,0,-1):
            s=s*var
        return s


r=factorial(5)
print(r)
        
        
    
