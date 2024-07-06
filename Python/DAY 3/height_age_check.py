print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Can Ride..")
    age = int(input("What's your age! "))
    if age < 12:
        print("you have to pay 5$ ")
    elif age >= 12 and age <= 18:
        print("you have to pay 7$ ")
    elif age > 18:
        print("you have to pay 12$ ")
else:
    print("Can't Ride..")