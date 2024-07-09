# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_value = 0

for x in student_scores:
    if x > max_value:
        max_value = x

print(f"The highest score in the class is: {max_value}")