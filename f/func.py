def cal_c(num1,num2,ch):
    if ch=='+':
        return num1+num2
    elif ch=='-':
        return num1-num2
    elif ch=='*':
        return num1*num2
    elif ch=='/':
        return nm1/num2
while input("\n\n press a key to continue"):
    num1=int(input("enter the numbers ",num1))
    num2=int(input("enter the numbers ",num2))
    ch=int(input("enter the numbers ",ch))
    result=cal_c(num1,num2,ch)
    print("your result",result)
    

    
