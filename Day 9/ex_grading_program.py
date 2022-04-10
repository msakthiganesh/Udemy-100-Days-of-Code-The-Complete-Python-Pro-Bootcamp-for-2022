student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for name, score in student_scores.items():
    if score >= 91:
        student_grades[name] = "Outstanding"
    elif score >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif score>=71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)