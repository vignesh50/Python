# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
# print(student_heights)
# print(type(student_heights))

# Find lenght
t_len = 0
t_height = 0
for x in student_heights:
    t_height += int(x) 
    t_len += 1
print(f"Total lenght of list: {t_len}")
print(f"Total Height: {t_height}")

Avg = t_height / t_len

print(f"Average height is {Avg}")