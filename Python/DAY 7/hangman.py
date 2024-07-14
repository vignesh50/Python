import random

word_list = ["aardvark", "baboon", "camel"]

pc_choose = random.choice(word_list)

life = 6
lenOfWord = len(pc_choose)
print(f"PC Choose a: {pc_choose}")

# blank_word = "_" * lenOfWord
# print(blank_word)
blank = []
for x in range(lenOfWord):
    blank.append("_")


def life():
    if life > 0:
        return True
    else:
        return False


user_in = input("Guess the Letter: ")[0]
print(f"you choose letter is : {user_in}")

option = int(input("Do you have life: 0 is out / 1 is In: "))

while option:
# to Find position
    for x in range(len(pc_choose)):
        if user_in == pc_choose[x]:
            print(f"index position is: {x}")
            blank[x] = user_in


print(f"Final result: {blank}")



