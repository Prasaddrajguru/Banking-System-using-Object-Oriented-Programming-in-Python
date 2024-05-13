
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ₹{self.balance:.2f}"
            )
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ₹{self.balance:.2f}")

    def deposit(self,amount):
        self.balance += amount
        print(f"\nDeposit Complete.")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ₹{self.balance:.2f}"
            )
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self,amount,account):
        try:
            print("\n**********\n\nBegining Transfer...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

class InterestRewardsAcct(BankAccount):
    
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit Complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self,initialAmount,acctName):
        super().__init__(initialAmount,acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\n Withdraw Completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

def main():
    Dave = BankAccount(1000,"Dave")
    Sara = BankAccount(2000,"Sara")


    Dave.getBalance()
    Sara.getBalance()

    Sara.deposit(500)

    Dave.withdraw(10000)
    Dave.withdraw(10)


    Dave.transfer(10000,Sara)
    Dave.transfer(100,Sara)


    Jim = InterestRewardsAcct(1000,"Jim")
    
    Jim.getBalance()
    Jim.deposit(100)
    Jim.transfer(100,Dave)

    Blaze = SavingsAcct(1000, "Blaze")

    Blaze.getBalance()
    Blaze.deposit(100)
    Blaze.transfer(1000,Sara)

if __name__ == "__main__":
    main()