
c=0

for var in range(0,100):
    var=var//10
    c=c+1

s=0
for var in range(0,100):
    r=var%10
    var=var//10
    s=s+r**c
    n=var
if s==n:
    print("number is armstrong")
else:
    print("not armstrong")
