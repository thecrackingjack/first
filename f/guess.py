import random
while input("\n\n press any key to continue"):
    r=random.randint(1,51)
    c=1
    while c<=6:
        if c==6:
            print("you looser")
            break
        n=int(input("guess a number from 1 to 50"))
        if n>r:
            print("the number guessed is greater")
        elif n<r:
            print("the number is lesser ")
        else :
            print("you are the winner")
            break
    c=c+1
    
    
