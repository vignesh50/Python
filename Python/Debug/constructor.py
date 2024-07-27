import random

class College:
    base_fees = 1000 

    def __init__(self,id_):
        self.studid = id_
        print(f"My roll number is: {self.studid}")


rand_roll_no = random.randint(0,5)

SRM = College(rand_roll_no)
print(f"SRM Object: {SRM.base_fees}")

Mepco = College(rand_roll_no)
Mepco.base_fees=2000
print(f"Mepco Object: {Mepco.base_fees}")

