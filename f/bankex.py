import filestore
import time
import datetime

def postbank():
    print ("Welcome to PostBank, We care for you\n")                                    
    prompt=int(input("""To open a new bank account, Press 1\n"""+                                       
                        """To access your existing account & transact press 2\n"""))    
    if prompt==1:                                                                       
        cus=BankAccount()                           
    elif prompt==2:                                                                     
        cus=ReturnCustomer()                              
    else:                                                                           
        print( "You have pressed the wrong key, please try again" )                       
        postbank()                                                                      

class BankAccount:
    """Class for a bank account"""
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore.cusaccountcheck()
        print ("Thank you %s, your account is set up and ready to use,\n a 100 pounds has been credited to your account" %self.username)
        time.sleep(2)
        self.userfunctions()



    def userfunctions(self):
        print("\n\nTo access any function below, enter the corresponding key")
        print ("""To:
check Balance, press B.
deposit cash,  press D.
withdraw cash, press W.
Delete account press X.
exit service,  press E\n
:"""),
        ans=raw_input("").lower()
        if ans=='b':
            
            self.passcheck()
            self.checkbalance()
        elif ans=='d':
            self.passcheck()
            self.depositcash()
        elif ans=='w':
            self.passcheck()
            self.withdrawcash()
        elif ans=='x':
            print ("%s, your account is being deleted"%self.username)
            time.sleep(1)
            print ("Minions at work")
            time.sleep(1)
            filestore.deleteaccount(self.username)
            print ("Your account has been successfuly deleted, goodbye")
        elif ans=='e':
            print ("Thank you for using PostBank Services")
            time.sleep(1)
            print ("Goodbye %s" %self.username)
            exit()

        else:
            print ("No function assigned to this key, please try again")
            self.userfunctions()

    def checkbalance(self):
        date=datetime.date.today()
        date=date.strftime('%d-%B-%Y')
        self.working()
        print ("Your account balance as at {} is {}").format(date, self.balance)
        self.transact_again()

    def withdrawcash(self):
        amount=float(raw_input("::\n Please enter amount to withdraw\n: "))
        self.balance-=amount
        self.working()
        print ("Your new account balance is %.2f" %self.balance)
        print ("::\n")
        filestore.balupdate(self.username, -amount)
        self.transact_again()

    def depositcash(self):
        amount=float(raw_input("::\nPlease enter amount to be deposited\n: "))
        self.balance+=amount
        self.working()
        print ("Your new account balance is %.2f" %self.balance)
        print ("::\n")
        filestore.balupdate(self.username, amount)
        self.transact_again()



    def transact_again(self):
        ans=raw_input("Do you want to do any other transaction? (y/n)\n").lower()
        self.working()
        if ans=='y':
            self.userfunctions()
        elif ans=='n':
            print ("Thank you for using PostBank we value you. Have a good day")
            time.sleep(1)
            print ("Goodbye {}").format(self.username)
            exit()
        elif ans!='y' and ans!='n':
            print( "Unknown key pressed, please choose either 'N' or 'Y'")
            self.transact_again()


    def working(self):
        print("working"),
        time.sleep(1)
        print ("..")
        time.sleep(1)
        print("..")
        time.sleep(1)


    def passcheck(self):
        """prompts user for password with every transaction and counterchecks it with stored passwords"""
        b=3
        while b>0:
            ans=raw_input("Please type in your password to continue with the transaction\n: ")
            if ans==self.userpassword:
                return True


            else:
                print ("That is the wrong password")
                b-=1
                print ("%d more attempt(s) remaining" %b)

        print ("Account has been freezed due to three wrong password attempts,\n contact your bank for help, bye bye")
        time.sleep(1)
        print ("...")
        time.sleep(1)
        print("...")
        time.sleep(1)

        exit()


class ReturnCustomer(BankAccount):
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore.oldcuscheck()
        self.userfunctions()

postbank() 

