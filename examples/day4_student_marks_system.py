student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

math_marks = int(input("Enter Math marks: "))
science_marks = int(input("Enter Science marks: "))
english_marks = int(input("Enter English marks: "))

total_marks = math_marks + science_marks + english_marks
percentage = (total_marks / 300) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n========== Student Result Report ==========")
print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Math Marks:", math_marks)
print("Science Marks:", science_marks)
print("English Marks:", english_marks)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
print("===========================================")
