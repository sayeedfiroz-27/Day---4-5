# Day 4 - Expanded Practice Notes

# Mini Project: Student Marks Management System

Ye expanded notes aap main Day 4 notes ke baad use kar sakte ho. Iska goal hai students ko project ka flow deeply samjhana: pehle data input hota hai, phir marks calculate hote hain, phir percentage nikalti hai, phir grade assign hota hai, aur last me report display hoti hai. Real life me school, coaching, college, online learning platform, aur training institute sab jagah result management system use hota hai. Isliye ye mini project beginner students ko programming ka practical meaning samjhata hai.

Teacher speaking flow: "Aaj hum Python ko sirf syntax ke form me nahi padhenge. Aaj hum dekhenge ki Python se ek real student report system kaise ban sakta hai. Jaise school me teacher marks enter karta hai aur system automatically total, percentage, grade, aur report bana deta hai, waise hi hum step by step apna basic system banayenge."

---

# 1. Student Data Input

Student data input ka matlab hai user se student ki basic information lena. Program khud se student ka naam ya roll number nahi jaanta. User keyboard se information deta hai, aur Python us information ko variables me store karta hai. Real project me input section bahut important hota hai, kyunki agar input galat hoga to final report bhi galat hogi. Isi wajah se students ko start me hi samjhana chahiye ki programming me data input first step hota hai.

## Practice Code 1.1 - Basic Student Profile

```python
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
student_class = input("Enter class name: ")

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Class:", student_class)
```

## Output

```text
Enter student name: Rahul
Enter roll number: 21
Enter class name: 10th
Student Name: Rahul
Roll Number: 21
Class: 10th
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = input("Enter student name: ")` | Ye line user se student ka naam leti hai. `input()` function keyboard se value receive karta hai. Jo value user type karta hai, wo string format me `student_name` variable me store hoti hai. Naam par calculation nahi hoti, isliye string format perfect hai. |
| 2 | `roll_number = input("Enter roll number: ")` | Roll number student ki identity ke liye use hota hai. Yahan hum roll number ko input ke through le rahe hain. Agar roll number par calculation nahi karni, to usko string ke form me store karna safe hai. |
| 3 | `student_class = input("Enter class name: ")` | Student ki class input hoti hai. Variable ka naam `student_class` rakha gaya hai kyunki `class` Python ka keyword hai. Python keywords ko variable name ki tarah use nahi karna chahiye. |
| 5 | `print("Student Name:", student_name)` | Ye line stored name ko label ke saath print karti hai. Label output ko readable banata hai. |
| 6 | `print("Roll Number:", roll_number)` | Ye line roll number print karti hai. Isse student ki identification clear hoti hai. |
| 7 | `print("Class:", student_class)` | Ye line class value ko output me show karti hai. Ab profile complete dikhti hai. |

## Practice Code 1.2 - Input With Section and City

```python
name = input("Enter name: ")
section = input("Enter section: ")
city = input("Enter city: ")

print(name, "belongs to section", section)
print(name, "is from", city)
```

## Output

```text
Enter name: Ayesha
Enter section: B
Enter city: Delhi
Ayesha belongs to section B
Ayesha is from Delhi
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = input("Enter name: ")` | Student ka naam input hota hai. Ye value baad me sentence banane me use hogi. |
| 2 | `section = input("Enter section: ")` | Section input hota hai. Real school me same class ke multiple sections ho sakte hain, isliye section useful detail hai. |
| 3 | `city = input("Enter city: ")` | Student ka city input hota hai. Ye example students ko dikhata hai ki `input()` sirf marks ke liye nahi, kisi bhi text data ke liye use hota hai. |
| 5 | `print(name, "belongs to section", section)` | Is line me comma ke through multiple values print ki gayi hain. Python comma ke beech automatic space add karta hai. |
| 6 | `print(name, "is from", city)` | Ye output ko natural sentence ki tarah print karta hai. Aise messages report ko friendly banate hain. |

## Practice Code 1.3 - Marks Input With Type Casting

```python
student_name = input("Enter student name: ")
math_marks = int(input("Enter Math marks: "))

print(student_name, "got", math_marks, "marks in Math")
print("Data type of marks:", type(math_marks))
```

## Output

```text
Enter student name: Neha
Enter Math marks: 88
Neha got 88 marks in Math
Data type of marks: <class 'int'>
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = input("Enter student name: ")` | Student ka naam string ke form me store hota hai. Name ko number me convert karne ki need nahi hoti. |
| 2 | `math_marks = int(input("Enter Math marks: "))` | `input()` pehle marks ko text form me leta hai. `int()` us text ko integer number me convert karta hai. Marks ko integer banana important hai because later total and percentage calculation karni hoti hai. |
| 4 | `print(student_name, "got", math_marks, "marks in Math")` | Ye line name and marks ko readable sentence me print karti hai. Isse student ko pata chalta hai ki input values program ke andar successfully store ho gayi hain. |
| 5 | `print("Data type of marks:", type(math_marks))` | `type()` function variable ka data type check karta hai. Output `<class 'int'>` prove karta hai ki marks ab number format me hain. |

---

# 2. Marks Calculation

Marks calculation project ka calculation engine hai. Jab student ke multiple subjects ke marks available hote hain, to program unko add karke total marks nikalta hai. Total marks se hi percentage aur grade decide hote hain. Isliye students ko yahan ye samjhana zaroori hai ki arithmetic operators real project me data processing ke liye use hote hain.

## Practice Code 2.1 - Three Subjects Total

```python
math = 85
science = 90
english = 80

total = math + science + english

print("Total Marks:", total)
```

## Output

```text
Total Marks: 255
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `math = 85` | Math subject ke marks variable me store kiye gaye hain. Variable ka naam meaningful hai, isliye code padhne me easy hai. |
| 2 | `science = 90` | Science marks separate variable me store hain. Har subject ko separate variable dena beginner ke liye clear approach hai. |
| 3 | `english = 80` | English marks store kiye gaye hain. Ab program ke paas three numeric values available hain. |
| 5 | `total = math + science + english` | Addition operator `+` three subjects ko add karta hai. Result `total` variable me store hota hai. Ye line project ke calculation part ka base hai. |
| 7 | `print("Total Marks:", total)` | Final total label ke saath display hota hai. Label user ko batata hai ki printed value ka meaning kya hai. |

## Practice Code 2.2 - Five Subjects Total

```python
hindi = 76
english = 82
math = 91
science = 88
computer = 95

total = hindi + english + math + science + computer

print("Five Subjects Total:", total)
```

## Output

```text
Five Subjects Total: 432
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1-5 | `hindi`, `english`, `math`, `science`, `computer` | Five subjects ke marks alag-alag variables me store kiye gaye hain. Real report card me multiple subjects hote hain, isliye ye example practical hai. |
| 7 | `total = hindi + english + math + science + computer` | Ye line all subject marks ko add karti hai. Agar marks numeric hain, to `+` operator mathematical addition karta hai. |
| 9 | `print("Five Subjects Total:", total)` | Ye final total display karta hai. Heading me "Five Subjects" likhne se output ka context clear hota hai. |

## Practice Code 2.3 - Total Using User Input

```python
subject1 = int(input("Enter first subject marks: "))
subject2 = int(input("Enter second subject marks: "))
subject3 = int(input("Enter third subject marks: "))

total_marks = subject1 + subject2 + subject3

print("Your total marks are:", total_marks)
```

## Output

```text
Enter first subject marks: 70
Enter second subject marks: 80
Enter third subject marks: 90
Your total marks are: 240
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `subject1 = int(input("Enter first subject marks: "))` | First subject marks user se liye ja rahe hain. `int()` conversion marks ko number banata hai. |
| 2 | `subject2 = int(input("Enter second subject marks: "))` | Second subject marks same process se input hote hain. Har marks ko integer banana calculation ke liye required hai. |
| 3 | `subject3 = int(input("Enter third subject marks: "))` | Third subject marks variable me store hote hain. Ab total calculate karne ke liye data ready hai. |
| 5 | `total_marks = subject1 + subject2 + subject3` | Ye line three subjects ka total calculate karti hai. |
| 7 | `print("Your total marks are:", total_marks)` | User ko final total dikhaya jaata hai. Ye output project ka first calculated result hai. |

---

# 3. Percentage Calculation

Percentage student ke performance ko standard format me dikhati hai. Total marks se hume pata chalta hai student ne kitne marks laaye, but percentage batati hai ki maximum marks ke comparison me performance kitni hai. Percentage formula hota hai: `(obtained marks / maximum marks) * 100`.

## Practice Code 3.1 - Basic Percentage

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
| 1 | `total_marks = 255` | Student ke obtained marks store hain. Ye numerator ka kaam karta hai. |
| 2 | `maximum_marks = 300` | Total possible marks store hain. Ye denominator ka kaam karta hai. |
| 4 | `percentage = (total_marks / maximum_marks) * 100` | Pehle obtained marks ko maximum marks se divide kiya jaata hai. Phir result ko 100 se multiply karke percentage banayi jaati hai. |
| 6 | `print("Percentage:", percentage)` | Calculated percentage output me show hoti hai. |

## Practice Code 3.2 - Rounded Percentage

```python
total = 432
maximum = 500

percentage = (total / maximum) * 100
rounded_percentage = round(percentage, 2)

print("Rounded Percentage:", rounded_percentage)
```

## Output

```text
Rounded Percentage: 86.4
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `total = 432` | Student ke total obtained marks store hain. |
| 2 | `maximum = 500` | Five subjects ke liye maximum marks 500 assume kiye gaye hain. |
| 4 | `percentage = (total / maximum) * 100` | Ye percentage formula apply karta hai. Division ka result decimal ho sakta hai. |
| 5 | `rounded_percentage = round(percentage, 2)` | `round()` decimal points ko control karta hai. Reports me rounded percentage clean lagti hai. |
| 7 | `print("Rounded Percentage:", rounded_percentage)` | Rounded value final output me print hoti hai. |

## Practice Code 3.3 - Percentage From User Input

```python
obtained = float(input("Enter obtained marks: "))
maximum = float(input("Enter maximum marks: "))

percentage = (obtained / maximum) * 100

print("Your percentage is:", percentage)
```

## Output

```text
Enter obtained marks: 450
Enter maximum marks: 500
Your percentage is: 90.0
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `obtained = float(input("Enter obtained marks: "))` | User obtained marks enter karta hai. `float()` use kiya gaya hai taaki decimal marks bhi accept ho sakein. |
| 2 | `maximum = float(input("Enter maximum marks: "))` | User maximum marks enter karta hai. Isse program flexible ho jaata hai. |
| 4 | `percentage = (obtained / maximum) * 100` | Formula user input values ke basis par percentage calculate karta hai. |
| 6 | `print("Your percentage is:", percentage)` | Final percentage display hoti hai. |

---

# 4. Grade Assignment

Grade assignment me program percentage ke basis par category decide karta hai. Ye condition statements ka practical use hai. School me teacher rules set karta hai: 90+ means A+, 75+ means A, 60+ means B. Python me ye rules `if`, `elif`, and `else` ke through implement hote hain.

## Practice Code 4.1 - Pass or Fail

```python
percentage = 38

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Result:", result)
```

## Output

```text
Result: Fail
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `percentage = 38` | Percentage value set ki gayi hai. Program isi value ke basis par pass/fail decide karega. |
| 3 | `if percentage >= 40:` | Condition check karti hai ki percentage 40 ya usse zyada hai ya nahi. |
| 4 | `result = "Pass"` | Agar condition true hoti, to result Pass hota. |
| 5 | `else:` | Jab `if` false hota hai tab `else` block run hota hai. |
| 6 | `result = "Fail"` | 38 less than 40 hai, isliye result Fail set hota hai. |
| 8 | `print("Result:", result)` | Final result display hota hai. |

## Practice Code 4.2 - Grade With Multiple Conditions

```python
percentage = 82

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
else:
    grade = "Needs Improvement"

print("Grade:", grade)
```

## Output

```text
Grade: A
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `percentage = 82` | Ye student ki percentage hai. |
| 3 | `if percentage >= 90:` | Highest grade condition pehle check hoti hai. 82 is condition ko satisfy nahi karta. |
| 5 | `elif percentage >= 75:` | Ye condition true hai because 82 greater than 75 hai. |
| 6 | `grade = "A"` | Grade A assign hota hai. Python baaki lower conditions skip kar deta hai. |
| 7-10 | `elif` and `else` | Ye alternate conditions hain. Current case me run nahi hoti. |
| 12 | `print("Grade:", grade)` | Final grade print hota hai. |

## Practice Code 4.3 - Grade With Message

```python
percentage = 92

if percentage >= 90:
    grade = "A+"
    message = "Excellent performance"
else:
    grade = "B"
    message = "Keep practicing"

print("Grade:", grade)
print("Message:", message)
```

## Output

```text
Grade: A+
Message: Excellent performance
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `percentage = 92` | Percentage 92 hai, jo high score category me aata hai. |
| 3 | `if percentage >= 90:` | Program check karta hai ki percentage 90 ya zyada hai ya nahi. |
| 4 | `grade = "A+"` | Condition true hai, isliye A+ grade assign hota hai. |
| 5 | `message = "Excellent performance"` | Grade ke saath motivational message bhi assign hota hai. |
| 6-8 | `else` block | Ye block tab run hota jab percentage 90 se kam hoti. Current example me ye skip hota hai. |
| 10-11 | `print(...)` | Grade aur message dono output me show hote hain. |

---

# 5. Result Display

Result display ka kaam final calculated values ko clean format me user tak pahunchana hai. Agar calculation correct hai but display messy hai, to project incomplete feel hota hai. Student report me labels, separators, and headings output ko professional banate hain.

## Practice Code 5.1 - Simple Result Card

```python
name = "Aman"
total = 255
percentage = 85.0
grade = "A"

print("----- Result Card -----")
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
```

## Output

```text
----- Result Card -----
Name: Aman
Total: 255
Percentage: 85.0
Grade: A
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1-4 | `name`, `total`, `percentage`, `grade` | Ye final report values store karte hain. Report display karne se pehle data ready hona chahiye. |
| 6 | `print("----- Result Card -----")` | Heading report ko clear start deti hai. |
| 7 | `print("Name:", name)` | Name label ke saath print hota hai. |
| 8 | `print("Total:", total)` | Total marks display hote hain. |
| 9 | `print("Percentage:", percentage)` | Percentage show hoti hai. |
| 10 | `print("Grade:", grade)` | Final grade output me aata hai. |

## Practice Code 5.2 - Result Using f-string

```python
name = "Neha"
percentage = 91.5
grade = "A+"

print(f"{name} got {percentage}% and achieved grade {grade}.")
```

## Output

```text
Neha got 91.5% and achieved grade A+.
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Neha"` | Student name variable me store hai. |
| 2 | `percentage = 91.5` | Percentage float value hai because decimal score possible hai. |
| 3 | `grade = "A+"` | Grade string value hai. |
| 5 | `print(f"{name} got {percentage}% and achieved grade {grade}.")` | F-string variables ko sentence ke andar directly place karne ka easy way hai. `{name}`, `{percentage}`, and `{grade}` real values se replace ho jaate hain. |

## Practice Code 5.3 - Display With Alignment

```python
name = "Rahul"
roll = "15"
grade = "B"

print("Name  :", name)
print("Roll  :", roll)
print("Grade :", grade)
```

## Output

```text
Name  : Rahul
Roll  : 15
Grade : B
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1-3 | `name`, `roll`, `grade` | Ye variables report ke display data ko store karte hain. |
| 5 | `print("Name  :", name)` | Label ke baad spaces use kiye gaye hain taaki colon align lage. |
| 6 | `print("Roll  :", roll)` | Roll number same format me print hota hai. |
| 7 | `print("Grade :", grade)` | Grade display hota hai. Alignment output ko neat banati hai. |

---

# 6. Basic Report Generation

Basic report generation complete mini project ka final stage hai. Is step me input, calculation, condition, and output sab combine hote hain. Student ko yahan feel hota hai ki alag-alag concepts milkar real project banate hain.

## Practice Code 6.1 - Report With Remarks

```python
name = "Rahul"
percentage = 86.4
grade = "A"

if percentage >= 75:
    remarks = "Good job, keep improving"
else:
    remarks = "Practice more and revise basics"

print("========== Report ==========")
print("Name:", name)
print("Percentage:", percentage)
print("Grade:", grade)
print("Remarks:", remarks)
print("============================")
```

## Output

```text
========== Report ==========
Name: Rahul
Percentage: 86.4
Grade: A
Remarks: Good job, keep improving
============================
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1-3 | `name`, `percentage`, `grade` | Ye report ke important values hain. Inhi ke basis par final output banega. |
| 5 | `if percentage >= 75:` | Program performance check karta hai. 75 ya usse zyada ko good performance maana gaya hai. |
| 6 | `remarks = "Good job, keep improving"` | Condition true hone par positive remarks assign hote hain. |
| 7-8 | `else` block | Agar condition false hoti to improvement remarks assign hote. |
| 10-16 | `print(...)` | Ye complete report format display karta hai. Separator lines report ko clean banati hain. |

## Practice Code 6.2 - Complete Report From User Input

```python
name = input("Enter student name: ")
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = math + science + english
percentage = (total / 300) * 100

if percentage >= 80:
    grade = "A"
else:
    grade = "B"

print("Student:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
```

## Output

```text
Enter student name: Ayesha
Enter Math marks: 90
Enter Science marks: 85
Enter English marks: 80
Student: Ayesha
Total: 255
Percentage: 85.0
Grade: A
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = input("Enter student name: ")` | User se student name input hota hai. Ye report me identity ke liye use hota hai. |
| 2-4 | `math`, `science`, `english` inputs | Marks input hote hain aur `int()` se number me convert hote hain. Without conversion calculation correct nahi hogi. |
| 6 | `total = math + science + english` | Three subjects ka total calculate hota hai. |
| 7 | `percentage = (total / 300) * 100` | Percentage formula apply hota hai. Maximum marks 300 assume kiye gaye hain. |
| 9-12 | `if` and `else` | Percentage ke basis par grade decide hota hai. |
| 14-17 | `print(...)` | Final report values output me show hoti hain. |

## Practice Code 6.3 - Report With Pass Status

```python
name = "Karan"
percentage = 58

if percentage >= 40:
    status = "Pass"
else:
    status = "Fail"

print("Name:", name)
print("Percentage:", percentage)
print("Status:", status)
```

## Output

```text
Name: Karan
Percentage: 58
Status: Pass
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Karan"` | Student ka naam store hai. |
| 2 | `percentage = 58` | Student ki percentage value store hai. |
| 4 | `if percentage >= 40:` | Program pass condition check karta hai. |
| 5 | `status = "Pass"` | 58 greater than 40 hai, so status Pass hota hai. |
| 6-7 | `else` block | Ye tab run hota jab percentage 40 se kam hoti. |
| 9-11 | `print(...)` | Name, percentage, and status final output me display hote hain. |
