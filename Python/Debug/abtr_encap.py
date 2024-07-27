class SBAccount:
    bank_name = "TMB"
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debt(self,debamount):
        self.balance = self.balance - debamount
        print(f"rs.{debamount} was debited and remain rs.{self.get_balance()}")

    def credit(self,credamount):
        self.balance = self.balance + credamount
        print(f"rs.{credamount} was credited and remain rs.{self.get_balance()}")
        
    def get_balance(self):
        return self.balance

person_1 = SBAccount(25_000,101)
print(f"Welcome to {person_1.bank_name} Bank")
print(f"Your current balance is : {person_1.balance}")

person_1.debt(1000)
person_1.credit(2000)

print(f"Current Balance is: {person_1.get_balance()}")
