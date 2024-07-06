print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Can Ride..")
    age = int(input("What's your age! "))
    if age >= 18:
        print("you have to pay 17$ ")
    else:
        print("you have to pay 7$ ")
else:
    print("Can't Ride..")