from art import logo
import os
 

print(logo)

participant = {}

option = True
while option:
    name = input("What's your name: ")
    cost = int(input("What's your Bid?: "))

    participant[name] = cost

    # For Linux and macOS
    
    option = int(input("Are there any other bidders? Type 0-> No, 1-> Yes: "))
    os.system('clear')

max = 0
for key in participant:

    if participant[key] > max:
        max = participant[key]
    else:
        max = 0 + max

#print(participant)


max = 0
win = ""
for key in participant:
    if participant[key] > max:
        max = participant[key]       
    else:
        max = 0 + max

for name, cost in participant.items():
    if cost == max:
        print(f"The Winner is {name} with a bid of ${cost}")