from abc import ABCMeta,abstractmethod
from random import randint
class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self,name,initialDeposit):
        return 0
    @abstractmethod
    def authenticate(self,name,accountNumber):
        return 0
    @abstractmethod
    def withdraw(self,withdrawalAmount):
        return 0
    @abstractmethod
    def display(self):
        return 0
    @abstractmethod
    def deposit(self,depositAmount):
        return 0
    
class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccount={}
    def createAccount(self,name,initialDeposit):
        self.accountNumber=randint(10000,99999)
        self.savingsAccount[self.accountNumber]=[name,initialDeposit]
        print("Account Creation has been successful.Your Account Number is.",self.accountNumber)
    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0]== name:
                print('Authentication Successful')
                self.accountNumber=accountNumber
                return True
            else:
                print('Authenticatio Failed')
                return False
        else:
            print('Athentication Failed')
            return False
    def withdraw(self,withdrawalAmount):
        if withdrawalAmount> self.savingsAccount[self.accountNumber][1]:
            print ("Insufficient Balance")
        else:
            print("Withdrawal Successful")
            self.savingsAccount[self.accountNumber][1]-=withdrawalAmount
        self.display()
    def display(self):
        print("Availabla balance:",self.savingsAccount[self.accountNumber][1])
    def deposit(self,depositAmount):
        self.savingsAccount[self.accountNumber][1]+=depositAmount
        self.display()
savingsaccount=SavingsAccount()
while True:
    print("Enter 1 to create an account")
    print("Enter 2 to use an existing account")
    print("Enter 3 to exit")
    userChoice=int(input())
    if(userChoice==1):
        print("Enter your Name to create an account:")
        name=input()
        print("Enter the amount you want to deposit:")
        initialDeposit=int(input())
        savingsaccount.createAccount(name,initialDeposit)
    elif(userChoice==2):
        print("Enter your Name to access your account:")
        name=input()
        print("Enter your Account Number")
        accountNumber=int(input())
        authenticatestatus=savingsaccount.authenticate(name,accountNumber)
        if authenticatestatus is True:
            while True:
                print("Enter 1 to Withdraw")
                print("Enter 2. to Deposit")
                print("Enter 3. to Display Balance")
                print("Enter 4. to go back to previous Menu")
                userChoice=int(input())
                if (userChoice==1):
                    print("Enter the amount you want to Withdraw")
                    withdrawalAmount=int(input())
                    savingsaccount.withdraw(withdrawalAmount)
                elif (userChoice==2):
                    print("Enter the amount you want to deposit")
                    depositAmount=int(input())
                    savingsaccount.deposit(depositAmount)
                elif(userChoice==3):
                    savingsaccount.display()
                elif(userChoice==4):
                    break
    elif(userChoice==3):
        quit()
