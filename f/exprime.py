while input("\n\ntype soemthing to continue"):
    n=int(input("enter a number "))
    c=2
    while(c<=100):
        if(n%c==0):
            print("not prime")
            break
        elif c==n-1:
            print("prime")
        else:
            pass
        c=c+1
