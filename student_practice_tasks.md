# Student Practice Tasks - Day 4 and Day 5

Ye document students ke practice ke liye alag banaya gaya hai. Aap class me pehle `Task` section read karke students ko try karne do. Jab students attempt kar lein, tab `Solution Code`, `Output`, aur `Detailed Code Explanation` ke through har line explain karo.

---

# Day 4 - Student Marks Management System

## 1. Student Data Input

### Practice Task 1.1 - Basic Student Profile

#### Task

Student se name, roll number, aur class input lo. Phir output me student profile clean labels ke saath print karo.

#### Solution Code

```python
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
student_class = input("Enter class name: ")

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Class:", student_class)
```

#### Output

```text
Enter student name: Rahul
Enter roll number: 21
Enter class name: 10th
Student Name: Rahul
Roll Number: 21
Class: 10th
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = input("Enter student name: ")` | Ye line user se student ka naam leti hai. `input()` function keyboard se value receive karta hai. Jo value user type karta hai, wo string format me `student_name` variable me store hoti hai. Naam par calculation nahi hoti, isliye string format perfect hai. |
| 2 | `roll_number = input("Enter roll number: ")` | Roll number student ki identity ke liye use hota hai. Yahan hum roll number ko input ke through le rahe hain. Agar roll number par calculation nahi karni, to usko string ke form me store karna safe hai. |
| 3 | `student_class = input("Enter class name: ")` | Student ki class input hoti hai. Variable ka naam `student_class` rakha gaya hai kyunki `class` Python ka keyword hai. Python keywords ko variable name ki tarah use nahi karna chahiye. |
| 5 | `print("Student Name:", student_name)` | Ye line stored name ko label ke saath print karti hai. Label output ko readable banata hai. |
| 6 | `print("Roll Number:", roll_number)` | Ye line roll number print karti hai. Isse student ki identification clear hoti hai. |
| 7 | `print("Class:", student_class)` | Ye line class value ko output me show karti hai. Ab profile complete dikhti hai. |

### Practice Task 1.2 - Input With Section and City

#### Task

Student ka name, section, aur city input lo. Phir do readable sentences print karo jisme section aur city mention ho.

#### Solution Code

```python
name = input("Enter name: ")
section = input("Enter section: ")
city = input("Enter city: ")

print(name, "belongs to section", section)
print(name, "is from", city)
```

#### Output

```text
Enter name: Ayesha
Enter section: B
Enter city: Delhi
Ayesha belongs to section B
Ayesha is from Delhi
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = input("Enter name: ")` | Student ka naam input hota hai. Ye value baad me sentence banane me use hogi. |
| 2 | `section = input("Enter section: ")` | Section input hota hai. Real school me same class ke multiple sections ho sakte hain, isliye section useful detail hai. |
| 3 | `city = input("Enter city: ")` | Student ka city input hota hai. Ye example students ko dikhata hai ki `input()` sirf marks ke liye nahi, kisi bhi text data ke liye use hota hai. |
| 5 | `print(name, "belongs to section", section)` | Is line me comma ke through multiple values print ki gayi hain. Python comma ke beech automatic space add karta hai. |
| 6 | `print(name, "is from", city)` | Ye output ko natural sentence ki tarah print karta hai. Aise messages report ko friendly banate hain. |

## 2. Marks Calculation

### Practice Task 2.1 - Three Subjects Total

#### Task

Math, Science, aur English ke fixed marks variables me store karo. Teeno marks ka total calculate karke print karo.

#### Solution Code

```python
math = 85
science = 90
english = 80

total = math + science + english

print("Total Marks:", total)
```

#### Output

```text
Total Marks: 255
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `math = 85` | Math subject ke marks variable me store kiye gaye hain. Variable ka naam meaningful hai, isliye code padhne me easy hai. |
| 2 | `science = 90` | Science marks separate variable me store hain. Har subject ko separate variable dena beginner ke liye clear approach hai. |
| 3 | `english = 80` | English marks store kiye gaye hain. Ab program ke paas three numeric values available hain. |
| 5 | `total = math + science + english` | Addition operator `+` three subjects ko add karta hai. Result `total` variable me store hota hai. Ye line project ke calculation part ka base hai. |
| 7 | `print("Total Marks:", total)` | Final total label ke saath display hota hai. Label user ko batata hai ki printed value ka meaning kya hai. |

### Practice Task 2.2 - Five Subjects Total

#### Task

Five subjects ke marks variables me store karo. Sabhi marks add karke total marks print karo.

#### Solution Code

```python
hindi = 76
english = 82
math = 91
science = 88
computer = 95

total = hindi + english + math + science + computer

print("Five Subjects Total:", total)
```

#### Output

```text
Five Subjects Total: 432
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1-5 | `hindi`, `english`, `math`, `science`, `computer` | Five subjects ke marks alag-alag variables me store kiye gaye hain. Real report card me multiple subjects hote hain, isliye ye example practical hai. |
| 7 | `total = hindi + english + math + science + computer` | Ye line all subject marks ko add karti hai. Agar marks numeric hain, to `+` operator mathematical addition karta hai. |
| 9 | `print("Five Subjects Total:", total)` | Ye final total display karta hai. Heading me "Five Subjects" likhne se output ka context clear hota hai. |

## 3. Percentage Calculation

### Practice Task 3.1 - Basic Percentage

#### Task

Total marks aur maximum marks variables me store karo. Percentage formula use karke percentage calculate and print karo.

#### Solution Code

```python
total_marks = 255
maximum_marks = 300

percentage = (total_marks / maximum_marks) * 100

print("Percentage:", percentage)
```

#### Output

```text
Percentage: 85.0
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `total_marks = 255` | Student ke obtained marks store hain. Ye numerator ka kaam karta hai. |
| 2 | `maximum_marks = 300` | Total possible marks store hain. Ye denominator ka kaam karta hai. |
| 4 | `percentage = (total_marks / maximum_marks) * 100` | Pehle obtained marks ko maximum marks se divide kiya jaata hai. Phir result ko 100 se multiply karke percentage banayi jaati hai. |
| 6 | `print("Percentage:", percentage)` | Calculated percentage output me show hoti hai. |

### Practice Task 3.2 - Rounded Percentage

#### Task

Total marks aur maximum marks ke basis par percentage calculate karo. Phir percentage ko round karke clean format me print karo.

#### Solution Code

```python
total = 432
maximum = 500

percentage = (total / maximum) * 100
rounded_percentage = round(percentage, 2)

print("Rounded Percentage:", rounded_percentage)
```

#### Output

```text
Rounded Percentage: 86.4
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `total = 432` | Student ke total obtained marks store hain. |
| 2 | `maximum = 500` | Five subjects ke liye maximum marks 500 assume kiye gaye hain. |
| 4 | `percentage = (total / maximum) * 100` | Ye percentage formula apply karta hai. Division ka result decimal ho sakta hai. |
| 5 | `rounded_percentage = round(percentage, 2)` | `round()` decimal points ko control karta hai. Reports me rounded percentage clean lagti hai. |
| 7 | `print("Rounded Percentage:", rounded_percentage)` | Rounded value final output me print hoti hai. |

## 4. Grade Assignment

### Practice Task 4.1 - Pass or Fail

#### Task

Percentage ke basis par check karo ki student Pass hai ya Fail. Agar percentage 40 ya usse zyada ho to Pass, otherwise Fail.

#### Solution Code

```python
percentage = 38

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Result:", result)
```

#### Output

```text
Result: Fail
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `percentage = 38` | Percentage value set ki gayi hai. Program isi value ke basis par pass/fail decide karega. |
| 3 | `if percentage >= 40:` | Condition check karti hai ki percentage 40 ya usse zyada hai ya nahi. |
| 4 | `result = "Pass"` | Agar condition true hoti, to result Pass hota. |
| 5 | `else:` | Jab `if` false hota hai tab `else` block run hota hai. |
| 6 | `result = "Fail"` | 38 less than 40 hai, isliye result Fail set hota hai. |
| 8 | `print("Result:", result)` | Final result display hota hai. |

### Practice Task 4.2 - Grade With Multiple Conditions

#### Task

Percentage ke basis par multiple conditions use karke grade assign karo. Highest grade condition pehle check karo.

#### Solution Code

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

#### Output

```text
Grade: A
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `percentage = 82` | Ye student ki percentage hai. |
| 3 | `if percentage >= 90:` | Highest grade condition pehle check hoti hai. 82 is condition ko satisfy nahi karta. |
| 5 | `elif percentage >= 75:` | Ye condition true hai because 82 greater than 75 hai. |
| 6 | `grade = "A"` | Grade A assign hota hai. Python baaki lower conditions skip kar deta hai. |
| 7-10 | `elif` and `else` | Ye alternate conditions hain. Current case me run nahi hoti. |
| 12 | `print("Grade:", grade)` | Final grade print hota hai. |

## 5. Result Display

### Practice Task 5.1 - Simple Result Card

#### Task

Student ka name, total, percentage, aur grade variables me store karo. In values ko result card format me print karo.

#### Solution Code

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

#### Output

```text
----- Result Card -----
Name: Aman
Total: 255
Percentage: 85.0
Grade: A
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1-4 | `name`, `total`, `percentage`, `grade` | Ye final report values store karte hain. Report display karne se pehle data ready hona chahiye. |
| 6 | `print("----- Result Card -----")` | Heading report ko clear start deti hai. |
| 7 | `print("Name:", name)` | Name label ke saath print hota hai. |
| 8 | `print("Total:", total)` | Total marks display hote hain. |
| 9 | `print("Percentage:", percentage)` | Percentage show hoti hai. |
| 10 | `print("Grade:", grade)` | Final grade output me aata hai. |

### Practice Task 5.2 - Result Using f-string

#### Task

Student ka name, percentage, aur grade use karke f-string ke through ek natural result sentence print karo.

#### Solution Code

```python
name = "Neha"
percentage = 91.5
grade = "A+"

print(f"{name} got {percentage}% and achieved grade {grade}.")
```

#### Output

```text
Neha got 91.5% and achieved grade A+.
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Neha"` | Student name variable me store hai. |
| 2 | `percentage = 91.5` | Percentage float value hai because decimal score possible hai. |
| 3 | `grade = "A+"` | Grade string value hai. |
| 5 | `print(f"{name} got {percentage}% and achieved grade {grade}.")` | F-string variables ko sentence ke andar directly place karne ka easy way hai. `{name}`, `{percentage}`, and `{grade}` real values se replace ho jaate hain. |

## 6. Basic Report Generation

### Practice Task 6.1 - Report With Remarks

#### Task

Student ke percentage ke basis par remarks decide karo aur final report me name, percentage, grade, aur remarks print karo.

#### Solution Code

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

#### Output

```text
========== Report ==========
Name: Rahul
Percentage: 86.4
Grade: A
Remarks: Good job, keep improving
============================
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1-3 | `name`, `percentage`, `grade` | Ye report ke important values hain. Inhi ke basis par final output banega. |
| 5 | `if percentage >= 75:` | Program performance check karta hai. 75 ya usse zyada ko good performance maana gaya hai. |
| 6 | `remarks = "Good job, keep improving"` | Condition true hone par positive remarks assign hote hain. |
| 7-8 | `else` block | Agar condition false hoti to improvement remarks assign hote. |
| 10-16 | `print(...)` | Ye complete report format display karta hai. Separator lines report ko clean banati hain. |

### Practice Task 6.2 - Complete Report From User Input

#### Task

Student name aur three subject marks user se input lo. Total, percentage, grade calculate karo aur final report print karo.

#### Solution Code

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

#### Output

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

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = input("Enter student name: ")` | User se student name input hota hai. Ye report me identity ke liye use hota hai. |
| 2-4 | `math`, `science`, `english` inputs | Marks input hote hain aur `int()` se number me convert hote hain. Without conversion calculation correct nahi hogi. |
| 6 | `total = math + science + english` | Three subjects ka total calculate hota hai. |
| 7 | `percentage = (total / 300) * 100` | Percentage formula apply hota hai. Maximum marks 300 assume kiye gaye hain. |
| 9-12 | `if` and `else` | Percentage ke basis par grade decide hota hai. |
| 14-17 | `print(...)` | Final report values output me show hoti hain. |

---

# Day 5 - Functions, Strings & Data Structures

## 1. Defining Functions

### Practice Task 1.1 - Welcome Function

#### Task

Ek function define karo jo Python class ke welcome messages print kare. Function ko call karke output show karo.

#### Solution Code

```python
def welcome():
    print("Welcome to Python class")
    print("Today we will learn functions")

welcome()
```

#### Output

```text
Welcome to Python class
Today we will learn functions
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def welcome():` | `def` keyword Python ko batata hai ki hum function define kar rahe hain. `welcome` function ka naam hai. Brackets function syntax ka part hain. Colon ke baad function ka block start hota hai. |
| 2 | `print("Welcome to Python class")` | Ye line function ke andar hai because indentation hai. Jab function call hoga tab ye first message print hoga. |
| 3 | `print("Today we will learn functions")` | Ye second message hai. Ye bhi function ke andar ka part hai. |
| 5 | `welcome()` | Ye function call hai. Sirf function define karne se code run nahi hota. Function ke andar ka code tab run hota hai jab function ko call kiya jaata hai. |

### Practice Task 1.2 - Function for Daily Task

#### Task

Ek function banao jo class start karne ke daily steps print kare: attendance, revision, aur today's topic.

#### Solution Code

```python
def start_class():
    print("Take attendance")
    print("Revise previous topic")
    print("Start today's topic")

start_class()
```

#### Output

```text
Take attendance
Revise previous topic
Start today's topic
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def start_class():` | Function ka naam `start_class` rakha gaya hai. Naam meaningful hai, isliye code padhte hi samajh aata hai ki function class start karne ke steps rakhta hai. |
| 2-4 | `print(...)` | Ye three lines function ke andar ke steps hain. Function call hone par ye steps same order me execute honge. |
| 6 | `start_class()` | Ye call function ko run karta hai. Is example se students ko samajh aata hai ki function ek task ko group kar sakta hai. |

## 2. Function Parameters & Arguments

### Practice Task 2.1 - Welcome Student By Name

#### Task

Parameter wala function banao jo student name receive kare aur personalized welcome message print kare.

#### Solution Code

```python
def welcome_student(name):
    print("Welcome", name)
    print(name, "is learning Python")

welcome_student("Rahul")
welcome_student("Ayesha")
```

#### Output

```text
Welcome Rahul
Rahul is learning Python
Welcome Ayesha
Ayesha is learning Python
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def welcome_student(name):` | `name` parameter hai. Function ko flexible banane ke liye parameter use hota hai. |
| 2 | `print("Welcome", name)` | Jo argument function call me pass hoga, wo `name` ki jagah use hoga. |
| 3 | `print(name, "is learning Python")` | Same parameter ko second sentence me bhi use kiya gaya hai. |
| 5 | `welcome_student("Rahul")` | `"Rahul"` argument hai. Function call ke time ye value `name` parameter me chali jaati hai. |
| 6 | `welcome_student("Ayesha")` | Same function different value ke saath run hota hai. Isi ko reusability kehte hain. |

### Practice Task 2.2 - Add Two Numbers

#### Task

Two parameters wala function banao jo two numbers add kare aur total print kare. Same function ko different values ke saath call karo.

#### Solution Code

```python
def add_numbers(num1, num2):
    total = num1 + num2
    print("Total:", total)

add_numbers(10, 20)
add_numbers(50, 70)
```

#### Output

```text
Total: 30
Total: 120
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def add_numbers(num1, num2):` | Function two parameters accept karta hai. `num1` and `num2` placeholders hain. |
| 2 | `total = num1 + num2` | Dono parameters ki values add hoti hain. Result `total` variable me store hota hai. |
| 3 | `print("Total:", total)` | Calculated total display hota hai. |
| 5 | `add_numbers(10, 20)` | Here 10 goes into `num1` and 20 goes into `num2`. Output 30 aata hai. |
| 6 | `add_numbers(50, 70)` | Same function dusri values ke saath run hota hai. Output 120 aata hai. |

## 3. Return Statement

### Practice Task 3.1 - Return Total Marks

#### Task

Function ke andar three subject marks ka total calculate karo aur `return` ke through result bahar bhejo.

#### Solution Code

```python
def calculate_total(math, science, english):
    total = math + science + english
    return total

marks = calculate_total(85, 90, 80)
print("Total Marks:", marks)
```

#### Output

```text
Total Marks: 255
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def calculate_total(math, science, english):` | Function three subject marks accept karta hai. |
| 2 | `total = math + science + english` | Marks add karke total calculate hota hai. |
| 3 | `return total` | Function calculated value ko caller ke paas wapas bhejta hai. |
| 5 | `marks = calculate_total(85, 90, 80)` | Function call hota hai and returned value `marks` variable me store hoti hai. |
| 6 | `print("Total Marks:", marks)` | Returned value ko output me display kiya jaata hai. |

### Practice Task 3.2 - Return Percentage

#### Task

Function banao jo total aur maximum marks accept kare, percentage calculate kare, aur return kare.

#### Solution Code

```python
def calculate_percentage(total, maximum):
    percentage = (total / maximum) * 100
    return percentage

result = calculate_percentage(432, 500)
print("Percentage:", result)
```

#### Output

```text
Percentage: 86.4
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def calculate_percentage(total, maximum):` | Function total and maximum marks accept karta hai. |
| 2 | `percentage = (total / maximum) * 100` | Percentage formula apply hota hai. |
| 3 | `return percentage` | Calculated percentage function ke bahar bheji jaati hai. |
| 5 | `result = calculate_percentage(432, 500)` | Function call ka returned value `result` me store hota hai. |
| 6 | `print("Percentage:", result)` | Percentage output me print hoti hai. |

## 4. Lambda Functions

### Practice Task 4.1 - Square Using Lambda

#### Task

Lambda function banao jo kisi number ka square calculate kare. Different numbers ke saath lambda call karo.

#### Solution Code

```python
square = lambda number: number * number

print(square(5))
print(square(8))
```

#### Output

```text
25
64
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `square = lambda number: number * number` | Lambda ek input `number` leta hai aur uska square return karta hai. Ye short function `square` variable me store hai. |
| 3 | `print(square(5))` | `square` function 5 ke saath call hota hai. 5 * 5 = 25 output aata hai. |
| 4 | `print(square(8))` | Same lambda 8 ke saath run hota hai. 8 * 8 = 64 output aata hai. |

### Practice Task 4.2 - Add GST Using Lambda

#### Task

Lambda function banao jo product price par 18 percent GST add karke final price return kare.

#### Solution Code

```python
add_gst = lambda price: price + (price * 0.18)

print(add_gst(1000))
```

#### Output

```text
1180.0
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `add_gst = lambda price: price + (price * 0.18)` | Lambda product price leta hai. Price ka 18 percent GST calculate hota hai aur original price me add hota hai. |
| 3 | `print(add_gst(1000))` | Lambda 1000 price par run hota hai. GST 180 banta hai, final price 1180.0 print hota hai. |

## 5. String Basics

### Practice Task 5.1 - Create and Print String

#### Task

Student name aur course ko string variables me store karo. Dono values print karo aur name ka data type check karo.

#### Solution Code

```python
student_name = "Rahul Sharma"
course = "Python"

print(student_name)
print(course)
print(type(student_name))
```

#### Output

```text
Rahul Sharma
Python
<class 'str'>
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = "Rahul Sharma"` | Text value quotes ke andar hai, isliye ye string hai. |
| 2 | `course = "Python"` | Course name bhi string format me store hai. |
| 4 | `print(student_name)` | Student name output me print hota hai. |
| 5 | `print(course)` | Course value print hoti hai. |
| 6 | `print(type(student_name))` | `type()` confirm karta hai ki variable string hai. |

### Practice Task 5.2 - String With Sentence

#### Task

Name aur city variables use karke ek readable sentence print karo.

#### Solution Code

```python
name = "Neha"
city = "Mumbai"

print(name, "is from", city)
```

#### Output

```text
Neha is from Mumbai
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Neha"` | Name string variable me store hai. |
| 2 | `city = "Mumbai"` | City bhi string value hai. |
| 4 | `print(name, "is from", city)` | Multiple strings and variables ko comma ke saath print kiya gaya hai. Python automatically spaces add karta hai. |

## 6. String Operations

### Practice Task 6.1 - Upper, Lower, Length

#### Task

String variable banao. Usko uppercase, lowercase, aur length ke saath print karo.

#### Solution Code

```python
name = "Rahul Sharma"

print(name.upper())
print(name.lower())
print(len(name))
```

#### Output

```text
RAHUL SHARMA
rahul sharma
12
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Rahul Sharma"` | String value variable me store hai. |
| 3 | `print(name.upper())` | `upper()` string ko uppercase me convert karta hai. Original string change nahi hoti; output uppercase version hota hai. |
| 4 | `print(name.lower())` | `lower()` string ko lowercase me convert karta hai. |
| 5 | `print(len(name))` | `len()` string ke total characters count karta hai, spaces included. |

### Practice Task 6.2 - Strip and Replace

#### Task

Extra spaces wali string ko clean karo aur usme old word ko new word se replace karo.

#### Solution Code

```python
message = "  I love Java  "

clean_message = message.strip()
new_message = clean_message.replace("Java", "Python")

print(new_message)
```

#### Output

```text
I love Python
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `message = "  I love Java  "` | String ke start and end me extra spaces hain. Real user input me aisi problem common hoti hai. |
| 3 | `clean_message = message.strip()` | `strip()` extra starting and ending spaces remove karta hai. |
| 4 | `new_message = clean_message.replace("Java", "Python")` | `replace()` old text ko new text se replace karta hai. |
| 6 | `print(new_message)` | Clean and updated message output me print hota hai. |

## 7. Lists

### Practice Task 7.1 - Create and Access List

#### Task

Fruits ki list banao. Complete list print karo, phir index ke through first aur third item access karo.

#### Solution Code

```python
fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
print(fruits[2])
```

#### Output

```text
['apple', 'banana', 'mango']
apple
mango
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `fruits = ["apple", "banana", "mango"]` | List square brackets me create hoti hai. Is list me three string items hain. |
| 3 | `print(fruits)` | Complete list print hoti hai. |
| 4 | `print(fruits[0])` | Index 0 first item ko access karta hai. Python indexing 0 se start hoti hai. |
| 5 | `print(fruits[2])` | Index 2 third item ko access karta hai. |

### Practice Task 7.2 - Add Item in List

#### Task

Skills ki list banao. List ke end me new skill add karo aur updated list print karo.

#### Solution Code

```python
skills = ["Python", "SQL"]

skills.append("Excel")

print(skills)
```

#### Output

```text
['Python', 'SQL', 'Excel']
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `skills = ["Python", "SQL"]` | Skills list me two values initially store hain. |
| 3 | `skills.append("Excel")` | `append()` list ke end me new item add karta hai. List mutable hoti hai, isliye change allowed hai. |
| 5 | `print(skills)` | Updated list output me print hoti hai. |

## 8. Tuples

### Practice Task 8.1 - Create Tuple

#### Task

Student details ka tuple banao. Complete tuple print karo aur index se first value access karo.

#### Solution Code

```python
student = ("Aman", 21, "Python")

print(student)
print(student[0])
```

#### Output

```text
('Aman', 21, 'Python')
Aman
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = ("Aman", 21, "Python")` | Tuple parentheses me create hota hai. Isme name, age, and course store hain. |
| 3 | `print(student)` | Complete tuple print hota hai. |
| 4 | `print(student[0])` | Index 0 tuple ka first item access karta hai. |

### Practice Task 8.2 - Tuple Unpacking

#### Task

Student tuple ko separate variables me unpack karo aur har variable print karo.

#### Solution Code

```python
student = ("Neha", 22, "Data Science")

name, age, course = student

print(name)
print(age)
print(course)
```

#### Output

```text
Neha
22
Data Science
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = ("Neha", 22, "Data Science")` | Tuple me three values store hain. |
| 3 | `name, age, course = student` | Tuple unpacking me tuple ki values separate variables me assign ho jaati hain. |
| 5-7 | `print(...)` | Har unpacked variable separately print hota hai. |

## 9. Dictionaries

### Practice Task 9.1 - Student Dictionary

#### Task

Student details dictionary me key-value pair ke form me store karo. Name aur course ko key se access karke print karo.

#### Solution Code

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print(student["name"])
print(student["course"])
```

#### Output

```text
Rahul
Python
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = {` | Dictionary curly braces me start hoti hai. |
| 2 | `"name": "Rahul"` | `"name"` key hai and `"Rahul"` value hai. |
| 3 | `"age": 21` | Age key numeric value store karti hai. |
| 4 | `"course": "Python"` | Course key course name store karti hai. |
| 7 | `print(student["name"])` | Key ke through name value access hoti hai. |
| 8 | `print(student["course"])` | Key ke through course value access hoti hai. |

### Practice Task 9.2 - Update Dictionary

#### Task

Student dictionary me marks update karo aur new grade key add karo. Updated dictionary print karo.

#### Solution Code

```python
student = {"name": "Ayesha", "marks": 85}

student["marks"] = 92
student["grade"] = "A+"

print(student)
```

#### Output

```text
{'name': 'Ayesha', 'marks': 92, 'grade': 'A+'}
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = {"name": "Ayesha", "marks": 85}` | Dictionary me name and marks store hain. |
| 3 | `student["marks"] = 92` | Existing marks value update hoti hai. Dictionary mutable hoti hai. |
| 4 | `student["grade"] = "A+"` | New key `grade` add hoti hai. |
| 6 | `print(student)` | Updated dictionary output me print hoti hai. |

## 10. Sets

### Practice Task 10.1 - Unique Skills

#### Task

Duplicate values ke saath skills set banao. Set print karo aur membership check karo ki Python present hai ya nahi.

#### Solution Code

```python
skills = {"Python", "SQL", "Python", "Excel"}

print(skills)
print("Python" in skills)
```

#### Output

```text
{'Python', 'SQL', 'Excel'}
True
```

Note: Set ka order fixed guarantee nahi hota. Output me items ka order different aa sakta hai, but duplicate Python only one time rahega.

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `skills = {"Python", "SQL", "Python", "Excel"}` | Set curly braces me create hua hai. Python duplicate hai, but set duplicate value ko one time rakhta hai. |
| 3 | `print(skills)` | Unique values print hoti hain. Order fixed nahi hota. |
| 4 | `print("Python" in skills)` | Membership operator `in` check karta hai ki Python set me present hai ya nahi. Since present hai, output True hai. |

### Practice Task 10.2 - Convert List to Set

#### Task

Duplicate city names wali list ko set me convert karo, taaki unique city names mil sakein.

#### Solution Code

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]

unique_cities = set(cities)

print(unique_cities)
```

#### Output

```text
{'Delhi', 'Mumbai', 'Pune'}
```

#### Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]` | List me duplicate city names hain. Real data me duplicate values common hoti hain. |
| 3 | `unique_cities = set(cities)` | `set()` list ko set me convert karta hai. Conversion ke time duplicate values remove ho jaati hain. |
| 5 | `print(unique_cities)` | Unique cities output me print hoti hain. Order fixed guarantee nahi hota. |
