# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# You are not allowed to use len(list_name) or sum(list_name)
total_height, count = 0, 0
for height in student_heights:
    total_height += height
    count += 1

print(round(total_height/count))



