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


def life1():
    if life > 0:
        return True
    else:
        return False

print(f"your life has: {life}")
option = True
while option:
    user_in = input("Guess the Letter: ")[0].lower()
    print(f"you choose letter is : {user_in}")
    # print(f"your life has: {life}")


# user choose word is present in pc choose word or not
    if user_in in pc_choose:
        # to Find position
        for x in range(len(pc_choose)):
            if user_in == pc_choose[x]:
                # print(f"index position is: {x}")
                blank[x] = user_in
        print(f"Filled: {blank}")
        print(f"your life left: {life}")
       # option = int(input("Do you have life: 0 is out / 1 is In: "))
    else:
        life -= 1
        print(f"Oh No!! \nyour life left: {life}")
    if life < 0:
        option = False

print(f"Final result: {blank}")



