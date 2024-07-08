rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as r

choice = [rock,paper,scissors]
user_in = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user = choice[user_in]
print(f"You Chose \n {user}")

computer_in = r.randint(0,2)
pc = choice[computer_in]
print(f"Computer Chose \n {pc} ") 
                                       

if user_in == computer_in:
    print("Game Tie")
    
elif (user_in == 0 and computer_in == 2) or (user_in == 1 and computer_in == 0) or (user_in == 2 and computer_in == 1):
    print("You Win")

else:
    print("You lose")



# Extra try
# elif user_in == 2 and computer_in == 1:
#     print("You Win")
# elif user_in == 2 and computer_in == 0:
#     print("You lose")

# elif (user_in == 0 and computer_in == 1) or (user_in == 1 and computer_in == 2):
#     print("You lose")

# elif user_in == 1 and computer_in == 2:
