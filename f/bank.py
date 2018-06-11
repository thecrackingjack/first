from getpass import getpass
def signup():
    name=input("\nenter your name").lower()
    password=getpass.getpass()
    bal=int(input("enter the initial balance"))
    acc=bank['acc'][-1]+1
    bank['name'].append(name)
    bank['password'].append(password)
    bank['bal'].append(bal)
    bank['acc'].append(acc)
    print("\nyour account succesfully created")
    print("\nplease note down your new account number{}".format(acc))
    time.sleep(2)

def login():
    print("\n***welcome to login page****")
    accno=int(input("LOgin ID:"))
    password=getpass("password:")
    if accno in bank['acc']:
        i=bank['acc'].index(accno)
        if password==bank['password'][i]:
            choice(i)
        else:
            print("\nerror wrong password ..try again:")
    else:
        print("\nNO such account exist\n signup first....")
        main()
    
    




def main():
    bank={'name':['udit','prashant','alex','rock'],
          'acc':[1001,1002,1003,1004],
          'bal':[10000,80000,60000,3000],
          'password':['kuchbhi','python','firangi','black']
          }
    while input("\n press a key to continue"):
        print("\n******welcome to the Bank******")
        print("\n\n 1.login \n 2.signup\n3.exit")
        ch=int(input("enter your choice 1. 2. or 3."))
        if ch==1:
            pass
        elif ch==2:
            signup()
        elif ch==3:
            exit(0)
            main()
if __name__=="__main__":
    main()


    
