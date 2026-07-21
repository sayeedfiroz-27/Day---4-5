# Day 4 - Mini Project 1

# Project: Student Marks Management System

## Project Features

Student Data Input, Marks Calculation, Percentage Calculation, Grade Assignment, Result Display, and Basic Report Generation.

Day 4 ka goal hai ki Day 1, Day 2, and Day 3 ke concepts ko ek real mini project mein combine karna. Ab tak learners ne variables, input, output, type casting, arithmetic operators, relational operators, and if-elif-else conditions seekhe. Is project mein ye sab concepts ek saath use honge.

Story type samjho: maan lo ek teacher ke paas students ke marks hain. Teacher ko har student ka naam, roll number, marks, total, percentage, grade, and final result banana hai. Agar manually calculate karein to time lagega and mistakes ho sakti hain. Python se hum ek simple marks management system bana sakte hain jo input lega, calculation karega, grade assign karega, and report print karega.

---

# 1. Student Data Input

## Topic Samjho

Student data input ka matlab hai user se student ki details lena. Is project mein hum student ka naam, roll number, and subject marks input lenge. Real school/college systems mein bhi pehle student data enter hota hai, phir calculation and report generation hoti hai.

## Kyu Use Karte Hain?

Har student ka data different hota hai. Agar program fixed values ke saath chalega to sirf ek student ke liye useful hoga. Input use karne se program dynamic ban jaata hai. Har baar user different student ka data enter kar sakta hai.

## Fayda

Input se program real-world jaisa behave karta hai. Teacher ya admin student ka naam and marks enter karega, and program uske according result generate karega.

## Practice Code 1 - Basic Student Input

```python
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

print("Student Name:", student_name)
print("Roll Number:", roll_number)
```

## Output

```text
Enter student name: Rahul
Enter roll number: 101
Student Name: Rahul
Roll Number: 101
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = input("Enter student name: ")` | Is line mein program user se student ka naam poochta hai. User jo naam type karega, woh `student_name` variable mein store ho jayega. Name text hota hai, isliye type casting ki zaroorat nahi hai. |
| 2 | `roll_number = input("Enter roll number: ")` | Roll number input liya ja raha hai. Roll number number jaisa dikh sakta hai, but agar uspar calculation nahi karni to string form mein store karna okay hai. |
| 4 | `print("Student Name:", student_name)` | Ye line label ke saath student ka naam print karti hai. Label output ko readable banata hai. |
| 5 | `print("Roll Number:", roll_number)` | Ye line roll number print karti hai. Output mein user ka entered roll number show hota hai. |

---

# 2. Marks Calculation

## Topic Samjho

Marks calculation ka matlab hai different subjects ke marks ko add karke total marks nikalna. Example: Math, Science, and English ke marks add karke total marks generate karna.

## Kyu Use Karte Hain?

Result banane ke liye total marks zaroori hota hai. Agar marks manually add karenge to mistake ho sakti hai. Python automatically accurate total calculate kar sakta hai.

## Fayda

Marks calculation fast, accurate, and reusable ho jaati hai. Agar subjects badal bhi jaayein, formula update karke program use kiya ja sakta hai.

## Practice Code 2 - Total Marks Calculation

```python
math_marks = float(input("Enter Math marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

total_marks = math_marks + science_marks + english_marks

print("Total Marks:", total_marks)
```

## Output

```text
Enter Math marks: 85
Enter Science marks: 90
Enter English marks: 80
Total Marks: 255.0
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `math_marks = float(input("Enter Math marks: "))` | Math marks user se input liye ja rahe hain. `input()` value string form mein leta hai, isliye `float()` use karke marks ko decimal number mein convert kiya gaya. |
| 2 | `science_marks = float(input("Enter Science marks: "))` | Science marks input liye gaye and float mein convert kiye gaye. Float use karne ka fayda hai ki 89.5 jaise decimal marks bhi accept honge. |
| 3 | `english_marks = float(input("Enter English marks: "))` | English marks input liye ja rahe hain. Ye bhi calculation mein use honge, isliye numeric type mein convert karna zaroori hai. |
| 5 | `total_marks = math_marks + science_marks + english_marks` | Ye line teeno subjects ke marks add karti hai. Addition operator `+` use hua hai. Result `total_marks` variable mein store hota hai. |
| 7 | `print("Total Marks:", total_marks)` | Ye final calculated total marks print karta hai. Label output ko clear banata hai. |

---

# 3. Percentage Calculation

## Topic Samjho

Percentage calculation ka matlab hai obtained marks ko total maximum marks ke respect mein percentage mein convert karna. Agar three subjects hain and each subject 100 marks ka hai, total maximum marks 300 honge.

Formula:

```text
percentage = (obtained marks / maximum marks) * 100
```

## Kyu Use Karte Hain?

Percentage result comparison ke liye useful hota hai. Total marks se pata chalta hai student ne kitne marks score kiye, but percentage se performance ka standard view milta hai.

## Fayda

Percentage se different exams ya students ko compare karna easy hota hai. Grade assignment bhi percentage ke basis par kar sakte hain.

## Practice Code 3 - Percentage Calculation

```python
total_marks = 255
maximum_marks = 300

percentage = (total_marks / maximum_marks) * 100

print("Percentage:", percentage)
```

## Output

```text
Percentage: 85.0
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `total_marks = 255` | Student ke obtained marks store kiye gaye hain. Ye marks subjects ke total se aaye hain. |
| 2 | `maximum_marks = 300` | Maximum marks store kiye gaye hain. Agar 3 subjects hain and har subject 100 marks ka hai, maximum marks 300 honge. |
| 4 | `percentage = (total_marks / maximum_marks) * 100` | Ye line percentage formula apply karti hai. Pehle obtained marks ko maximum marks se divide kiya jaata hai, phir result ko 100 se multiply kiya jaata hai. |
| 6 | `print("Percentage:", percentage)` | Ye final calculated percentage print karta hai. Output 85.0 aata hai. |

---

# 4. Grade Assignment

## Topic Samjho

Grade assignment ka matlab hai percentage ke basis par grade decide karna. Example: 90 se zyada A, 75 se zyada B, 60 se zyada C, 40 se zyada D, warna Fail.

## Kyu Use Karte Hain?

Students ko result samajhne mein grade helpful hota hai. Sirf percentage dekhna enough nahi hota. Grade performance category show karta hai.

## Fayda

Grade assignment se report professional lagti hai. Program automatically grade decide karta hai, so manual checking ki zaroorat nahi hoti.

## Practice Code 4 - Grade Assignment

```python
percentage = 85

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
```

## Output

```text
Grade: B
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `percentage = 85` | Percentage variable mein value 85 store hai. Python isi value ke basis par grade decide karega. |
| 3 | `if percentage >= 90:` | Pehli condition check karti hai ki percentage 90 ya usse zyada hai. Agar true hota to grade A assign hota. |
| 4 | `grade = "A"` | Ye line tab run hoti jab first condition true hoti. Yahan percentage 85 hai, so ye line skip hogi. |
| 5 | `elif percentage >= 75:` | Python next condition check karta hai. 85 greater than 75 hai, so ye condition true hoti hai. |
| 6 | `grade = "B"` | Since condition true hai, grade variable mein `"B"` store hota hai. |
| 7-10 | `elif ...` | Ye lower grade conditions hain. Python inhe skip kar deta hai kyunki grade B already decide ho gaya. |
| 11 | `else:` | Else tab run hota jab koi bhi condition true nahi hoti. |
| 14 | `print("Grade:", grade)` | Final assigned grade print hota hai. Output B hai. |

---

# 5. Result Display

## Topic Samjho

Result display ka matlab hai calculated information ko clean format mein user ko show karna. Report readable honi chahiye taaki student, teacher, ya admin easily samajh sake.

## Kyu Use Karte Hain?

Calculation ke baad result ko properly display karna important hai. Agar output messy hai, user confuse ho sakta hai. Labels and separators use karne se output professional lagta hai.

## Fayda

Clean result display se project complete and useful lagta hai. User ko student name, marks, percentage, grade sab clear dikhta hai.

## Practice Code 5 - Result Display

```python
student_name = "Rahul"
total_marks = 255
percentage = 85.0
grade = "B"

print("Student Result")
print("--------------")
print("Name:", student_name)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
```

## Output

```text
Student Result
--------------
Name: Rahul
Total Marks: 255
Percentage: 85.0
Grade: B
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = "Rahul"` | Student ka naam variable mein store kiya gaya hai. |
| 2 | `total_marks = 255` | Calculated total marks store hain. |
| 3 | `percentage = 85.0` | Calculated percentage store hai. |
| 4 | `grade = "B"` | Assigned grade store hai. |
| 6 | `print("Student Result")` | Report ka heading print hota hai. |
| 7 | `print("--------------")` | Separator line output ko clean banati hai. |
| 8-11 | `print(...)` | Ye lines student ki details and result values labels ke saath print karti hain. |

---

# 6. Basic Report Generation

## Topic Samjho

Basic report generation ka matlab hai final output ko complete report ke form mein dikhana. Isme student data, subject marks, total marks, percentage, grade, and status sab included hote hain.

## Kyu Use Karte Hain?

Mini project ka final goal report generate karna hai. Real systems mein data input ke baad final report hi user ko value deti hai.

## Fayda

Report generation se project real-world jaisa lagta hai. Ye teacher ke liye useful output banata hai.

## Final Project Code - Student Marks Management System

```python
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

math_marks = float(input("Enter Math marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

total_marks = math_marks + science_marks + english_marks
maximum_marks = 300
percentage = (total_marks / maximum_marks) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("")
print("Student Marks Report")
print("--------------------")
print("Name:", student_name)
print("Roll Number:", roll_number)
print("Math Marks:", math_marks)
print("Science Marks:", science_marks)
print("English Marks:", english_marks)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
```

## Output

```text
Enter student name: Rahul
Enter roll number: 101
Enter Math marks: 85
Enter Science marks: 90
Enter English marks: 80

Student Marks Report
--------------------
Name: Rahul
Roll Number: 101
Math Marks: 85.0
Science Marks: 90.0
English Marks: 80.0
Total Marks: 255.0
Percentage: 85.0
Grade: B
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = input("Enter student name: ")` | User se student ka naam input liya gaya hai. Ye report mein display hoga. |
| 2 | `roll_number = input("Enter roll number: ")` | Student ka roll number input liya gaya hai. Ispar calculation nahi karni, so string form okay hai. |
| 4 | `math_marks = float(input("Enter Math marks: "))` | Math marks input liye and float mein convert kiye. Calculation ke liye numeric type zaroori hai. |
| 5 | `science_marks = float(input("Enter Science marks: "))` | Science marks input liye and decimal number mein convert kiye. |
| 6 | `english_marks = float(input("Enter English marks: "))` | English marks input liye and float mein convert kiye. |
| 8 | `total_marks = math_marks + science_marks + english_marks` | Teeno subjects ke marks add karke total calculate hota hai. |
| 9 | `maximum_marks = 300` | Maximum marks fixed kiye gaye hain. 3 subjects x 100 marks = 300. |
| 10 | `percentage = (total_marks / maximum_marks) * 100` | Percentage formula apply hota hai. Obtained marks ko maximum marks se divide karke 100 se multiply karte hain. |
| 12 | `if percentage >= 90:` | Grade A ke liye condition check hoti hai. |
| 14 | `elif percentage >= 75:` | Agar A condition false hai, to B grade condition check hoti hai. |
| 16 | `elif percentage >= 60:` | C grade condition check hoti hai. |
| 18 | `elif percentage >= 40:` | D grade condition check hoti hai. |
| 20 | `else:` | Agar percentage 40 se kam hai, to Fail assign hota hai. |
| 23 | `print("")` | Blank line report se pehle spacing ke liye hai. |
| 24 | `print("Student Marks Report")` | Report heading print hota hai. |
| 25 | `print("--------------------")` | Separator line output ko clean banati hai. |
| 26-34 | `print(...)` | Final report ki saari values labels ke saath print hoti hain. |

