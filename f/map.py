import math
def prime(num):
    for var in range(2,int(math.sqrt(num)+2)):
        if num%var==0:
            return False
    return True

n=list(map(int,input().split()))
k=map(prime,n)
for key,value in zip(n,k):
    print("{}={}".format(key,value))

l=filter(prime,n)
print(*l)



