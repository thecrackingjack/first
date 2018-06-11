import random
t=["rock","paper","scissors"]
c=t[random.randint(0,2)]
p=False
while p==False:
    while input("press a key to continue"):
        p=input("enter rock paper or scissors to play").lower()
        if p==c:
            print("its a draw")
        elif p=="rock":
            if c=="paper":
                print("you loose",c,"covers",p)
            else:
                print("you win",p,"smashed",c)
        elif p=="paper":
            if c=="scissors":
                print("you loose",c,"cuts",p)
            else:
                print("you win",p,"covers",c)
        elif p=="scissors":
            if c=="rock":
                print("you loose",c,"smashed",p)
            else:
                print("you win",p,"cuts",c)
        else:
            print("invalid choice")
        
        c=t[random.randint(0,2)]

