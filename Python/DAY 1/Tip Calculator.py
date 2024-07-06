#If the bill was $150.00, split between 5 people, with 12% tip. 


#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇



# 124.56

# 12

# 7
# 19.93

print("Welcome to the tip calculator!")
t_bill = float(input("What was the total bill? $ "))

tips = int(input("How much tip would you like to give? 10, 12, or 15? "))

total_tips_percentage = (float(tips / 100) * t_bill)

bill_plus_tip = total_tips_percentage + t_bill

split = int(input("How many people to split the bill? "))
split_by_person = bill_plus_tip / split

# final_bill = round(split_by_person, 2)
final_bill = "{:.2f}".format(split_by_person)

print(f"Each person should pay: ${final_bill}")