def welcome_student():
    print("Welcome to Python Day 5 class")


welcome_student()


def student_intro(name, course):
    print("Student name is", name)
    print("Course name is", course)


student_intro("Aman", "Python")


def calculate_total(math_marks, science_marks, english_marks):
    total = math_marks + science_marks + english_marks
    return total


student_total = calculate_total(85, 90, 80)
print("Total marks:", student_total)


square = lambda number: number * number
print("Square:", square(6))


student_name = "Rahul Sharma"
print(student_name)
print(student_name.upper())
print(student_name.lower())
print(len(student_name))


skills = ["Python", "SQL", "Excel"]
skills.append("Power BI")
print(skills)
print(skills[0])


student_info = ("Aman", 21, "Python")
print(student_info)
print(student_info[2])


student = {
    "name": "Neha",
    "age": 22,
    "course": "Data Science"
}
print(student["name"])
print(student["course"])


unique_skills = {"Python", "SQL", "Python", "Excel"}
print(unique_skills)
print("Python" in unique_skills)
