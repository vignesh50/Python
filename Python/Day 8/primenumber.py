# Write your code below this line 👇

def prime_checker(number):
    if number >= 0 and number <= 3:
        print(f"It's a prime number.")
    elif number > 3:
        number = number * number
        number -= 1
        if number % 24 == 0:
            print(f"It's a prime number.")
        else:
            print(f"It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)