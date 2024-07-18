# Write your code below this line 👇

def prime_checker(number):
    if number % 2 == 0:
        print("It's not a Prime number.")
    else:
        print("It's a Prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)