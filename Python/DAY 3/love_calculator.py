print("The Love Calculator is calculating your score...")
name1 = "Angela Yu" # What is your name?
name2 = "Jack Bauer" # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combine_name = name1 + name2
combine_name_lower = combine_name.lower()
t = combine_name_lower.count('t')
r = combine_name_lower.count('r')
u = combine_name_lower.count('u')
e = combine_name_lower.count('e')
count_true = t + r + u + e
print(f"True Count: {count_true}")
# print(count_true)
l = combine_name_lower.count('l')
o = combine_name_lower.count('o')
v = combine_name_lower.count('v')
e = combine_name_lower.count('e')
count_love = l + o + v + e
# print(count_love)
print(f"LOVE Count: {count_love}")
love_score = str(count_true) + str(count_love)
love_score = int(love_score)
print(type(love_score))
print(f"Your score is {love_score}")