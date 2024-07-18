# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print(f"Welcome to Python Programing")
    print(f"Python is fun")
    print(f"I Love Programming")
    print('*'*25)

greet()

def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How do you do {name}?")
    print('*'*25)
greet_with_name("viky")

def greet_with_location(name, location):
    print(f"Hello, {name}")
    print(f"I am currently living in a {location}")
    print('*' * 25)
greet_with_location(location="Madurai", name="Viky")

greet_with_location("Saranya","Dindigul")