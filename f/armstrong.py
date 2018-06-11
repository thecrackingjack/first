for n in range(0,10000):
    c=0
    num=n
    while n>0:
        n=n//10
        c=c+1

    n=num
    s=0
    while n:
        r=n%10
        n=n//10
        s=s+r**c
    if s==num:
        print("number is armstrong")
    else:
        print("not armstrong")   
