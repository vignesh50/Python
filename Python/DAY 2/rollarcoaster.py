print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
photo_cost = 3

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Child tickets are ${bill}.")
  elif age <= 18:
    bill = 7
    print(f"Youth tickets are ${bill}.")
  else:
    bill = 12
    print(f"Adult tickets are ${bill}.")
  photo = input("Do you want photo! Type Y or N ")

  if photo == "Y" or photo == "y":
    t_bill = bill + photo_cost
    print(f"Your total bill is ${t_bill}")
    
else:
  print("Sorry you have to grow to ride.")