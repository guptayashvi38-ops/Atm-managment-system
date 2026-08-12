class ATM:
    def __init__(self):
        self.__pin=2314
        self.__balance=310000

    def check_balance(self):
        print("Available Balance:",self.__balance)

    def deposit_balance(self,amount):
        self.__balance+=amount
        print("Amount deposited successfully.")

    def withdraw_balance(self,amount):
        if amount <=self.__balance:
            self.__balance-=amount
            print("Please collect your cash.")
        else:
            print("Insufficient Balance.")

atm=ATM()

running=True

while running:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    try:
        user=int(input("Enter your choice:"))

        if user==1:
            atm.check_balance()

        elif user==2:
            atm.deposit_balance(5000)
            atm.check_balance()
            
        elif user==3:
            atm.withdraw_balance(700)
            atm.check_balance()
            
        elif user==4:
            print("Thankyou")
            running=False
        else:
            print("Invalid choice.")

    except:
        print("Please enter numbers only.")