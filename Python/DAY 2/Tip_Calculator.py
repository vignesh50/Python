print("Welcome to the tip calculator!")
t_bill = float(input("What was the total bill? $ "))

tips = int(input("How much tip would you like to give? 10, 12, or 15? "))

total_tips_percentage = float(tips / 100)

total_tip = total_tips_percentage * t_bill
bill_plus_tip = t_bill + total_tip 

split = int(input("How many people to split the bill? "))
split_by_person = bill_plus_tip / split

final_bill = round(split_by_person, 2)

print(f"Each person should pay: ${final_bill}")