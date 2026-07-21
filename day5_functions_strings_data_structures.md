# Day 5 - Functions, Strings & Data Structures

## Topics Covered

Defining Functions, Function Parameters & Arguments, Return Statement, Lambda Functions, String Basics, String Operations, Lists, Tuples, Dictionaries, and Sets.

Day 5 ka goal hai code ko reusable banana and data ko better structure mein store karna. Ab tak hum variables, conditions, loops, and mini project kar chuke hain. Lekin real projects mein code bada hota hai. Agar hum same code baar-baar likhenge to program messy ho jaayega. Functions code ko reusable banate hain. Strings text handle karte hain. Lists, tuples, dictionaries, and sets multiple data ko organize karte hain.

---

# 1. Defining Functions

## Topic Samjho

Function ek reusable code block hota hai. Agar koi kaam baar-baar karna ho, to uska function bana sakte hain. Function define karne ke liye Python mein `def` keyword use hota hai.

Story type samjho: maan lo teacher har student ko welcome message bolta hai. Agar 50 students hain, to same print line 50 baar likhna boring hoga. Function bana do, phir jab bhi zaroorat ho function call kar do.

## Kyu Use Karte Hain?

Function code repetition kam karta hai. Code clean and manageable banata hai. Agar function ke andar logic change karna ho, to ek jagah change karna hota hai.

## Fayda

Functions se code reusable, organized, and professional banta hai. Large projects mein functions must-have concept hai.

## Practice Code 1

```python
def welcome_student():
    print("Welcome to Python class")
    print("Today we are learning functions")

welcome_student()
```

## Output

```text
Welcome to Python class
Today we are learning functions
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def welcome_student():` | `def` keyword function define karne ke liye use hota hai. `welcome_student` function ka naam hai. Brackets function call format ka part hain. Colon batata hai function block start ho raha hai. |
| 2 | `print("Welcome to Python class")` | Ye line function ke andar hai because indented hai. Jab function call hoga, ye message print hoga. |
| 3 | `print("Today we are learning functions")` | Ye bhi function ke andar hai. Function call hone par second message print hoga. |
| 5 | `welcome_student()` | Ye function call hai. Function define karne se code run nahi hota; function call karne par function ke andar ka code execute hota hai. |

---

# 2. Function Parameters & Arguments

## Topic Samjho

Parameter function definition ke andar variable jaisa placeholder hota hai. Argument wo actual value hoti hai jo function call karte time pass ki jaati hai.

Story: Agar welcome message har student ke naam ke saath print karna hai, to function ko student ka naam dena padega. Function ke andar `name` parameter hoga, and call karte time `"Rahul"` argument pass hoga.

## Kyu Use Karte Hain?

Parameters se function flexible banta hai. Same function different values ke saath kaam kar sakta hai.

## Fayda

Ek hi function multiple students, products, marks, users ke liye use ho sakta hai.

## Practice Code 2

```python
def welcome_student(name):
    print("Welcome", name)
    print(name, "is learning Python")

welcome_student("Rahul")
welcome_student("Ayesha")
```

## Output

```text
Welcome Rahul
Rahul is learning Python
Welcome Ayesha
Ayesha is learning Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def welcome_student(name):` | Function define hua and `name` parameter diya gaya. Parameter function ke andar temporary variable ki tarah kaam karta hai. |
| 2 | `print("Welcome", name)` | Fixed text `Welcome` and parameter value print hoti hai. Function call ke according name change hoga. |
| 3 | `print(name, "is learning Python")` | Name ko sentence ke start mein use kiya gaya hai. Isse output personal banta hai. |
| 5 | `welcome_student("Rahul")` | Function call hua and `"Rahul"` argument pass hua. Ab function ke andar `name` ki value Rahul hogi. |
| 6 | `welcome_student("Ayesha")` | Same function dobara call hua with different argument. Ab output Ayesha ke liye generate hoga. |

---

# 3. Return Statement

## Topic Samjho

`return` statement function se value wapas bhejne ke liye use hota hai. `print()` sirf screen par show karta hai, lekin `return` value ko function ke bahar use karne ke liye send karta hai.

Story: Agar function total marks calculate karta hai, to hume result sirf print nahi karna, kabhi-kabhi us result ko percentage calculation mein bhi use karna hota hai. Isliye return useful hai.

## Kyu Use Karte Hain?

Return se function ka result variable mein store kar sakte hain. Phir us result ko further calculation mein use kar sakte hain.

## Fayda

Functions reusable and calculation-friendly bante hain.

## Practice Code 3

```python
def add_marks(math_marks, science_marks):
    total = math_marks + science_marks
    return total

result = add_marks(80, 90)
print("Total Marks:", result)
```

## Output

```text
Total Marks: 170
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def add_marks(math_marks, science_marks):` | Function define hua with two parameters. Ye function two subject marks receive karega. |
| 2 | `total = math_marks + science_marks` | Dono marks add hote hain and result `total` variable mein store hota hai. |
| 3 | `return total` | Function total value ko bahar return karta hai. Ye value later variable mein store ho sakti hai. |
| 5 | `result = add_marks(80, 90)` | Function call hua with 80 and 90. Return value `result` variable mein store hui. |
| 6 | `print("Total Marks:", result)` | Returned result print hota hai. Output 170 hai. |

---

# 4. Lambda Functions

## Topic Samjho

Lambda function small one-line function hota hai. Jab simple calculation ya short operation karna ho, lambda use kar sakte hain.

## Kyu Use Karte Hain?

Short functions ke liye lambda quick syntax deta hai. Example: number double karna, square nikalna, small calculation.

## Fayda

Lambda code ko short banata hai. Lekin beginners ko pehle normal function samajhna chahiye, phir lambda.

## Practice Code 4

```python
square = lambda number: number * number

print(square(5))
```

## Output

```text
25
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `square = lambda number: number * number` | Lambda function create hua and `square` variable mein store hua. `number` input parameter hai. Colon ke baad expression hai jo square calculate karta hai. |
| 3 | `print(square(5))` | Lambda function ko 5 argument ke saath call kiya. Function `5 * 5` calculate karta hai and output 25 print hota hai. |

---

# 5. String Basics

## Topic Samjho

String text data hota hai. Python mein string quotes ke andar likhte hain. Name, city, email, course name, address sab strings hote hain.

## Kyu Use Karte Hain?

Real applications mein text data bahut common hota hai. User name, messages, labels, passwords, search text sab string hote hain.

## Fayda

Strings se hum text store, print, combine, search, and modify kar sakte hain.

## Practice Code 5

```python
name = "Rahul"
course = "Python"

print(name)
print(course)
```

## Output

```text
Rahul
Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Rahul"` | Name string value hai, quotes ke andar likha gaya hai. Ye text data store karta hai. |
| 2 | `course = "Python"` | Course name bhi string hai. String ko single ya double quotes mein likh sakte hain. |
| 4 | `print(name)` | Name variable ki value print hoti hai. |
| 5 | `print(course)` | Course variable ki value print hoti hai. |

---

# 6. String Operations

## Topic Samjho

String operations ka matlab strings par kaam karna. Example: string combine karna, uppercase/lowercase karna, length find karna, specific character access karna.

## Kyu Use Karte Hain?

Text processing real projects mein common hoti hai. User name format karna, email validate karna, search feature banana, message generate karna.

## Fayda

String operations se text ko clean and useful format mein convert kar sakte hain.

## Practice Code 6

```python
name = "rahul"

print(name.upper())
print(name.capitalize())
print(len(name))
```

## Output

```text
RAHUL
Rahul
5
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "rahul"` | Lowercase string store ki gayi hai. |
| 3 | `print(name.upper())` | `upper()` string ko uppercase mein convert karta hai. Output RAHUL hai. |
| 4 | `print(name.capitalize())` | `capitalize()` first letter capital karta hai. Output Rahul hai. |
| 5 | `print(len(name))` | `len()` string ki length batata hai. Rahul mein 5 characters hain. |

---

# 7. Lists

## Topic Samjho

List multiple values ko ek variable mein store karne ke liye use hoti hai. List square brackets `[]` se banti hai.

## Kyu Use Karte Hain?

Jab multiple values store karni ho, jaise students, marks, products, tasks, tab list use hoti hai.

## Fayda

List changeable hoti hai. Hum items add, update, delete kar sakte hain.

## Practice Code 7

```python
students = ["Rahul", "Ayesha", "Priya"]

print(students)
print(students[0])
```

## Output

```text
['Rahul', 'Ayesha', 'Priya']
Rahul
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `students = ["Rahul", "Ayesha", "Priya"]` | Students naam ki list banayi gayi hai. Isme three string values store hain. |
| 3 | `print(students)` | Complete list print hoti hai. |
| 4 | `print(students[0])` | Index 0 first item ko access karta hai. Output Rahul hai. |

---

# 8. Tuples

## Topic Samjho

Tuple list jaisa collection hota hai, lekin tuple immutable hota hai. Matlab create hone ke baad change nahi hota. Tuple parentheses `()` se banta hai.

## Kyu Use Karte Hain?

Jab fixed data store karna ho, jaise weekdays, coordinates, RGB colors, tab tuple use hota hai.

## Fayda

Tuple data ko accidental changes se protect karta hai.

## Practice Code 8

```python
week_days = ("Monday", "Tuesday", "Wednesday")

print(week_days)
print(week_days[1])
```

## Output

```text
('Monday', 'Tuesday', 'Wednesday')
Tuesday
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `week_days = ("Monday", "Tuesday", "Wednesday")` | Tuple create kiya gaya hai. Week days fixed data hain, isliye tuple suitable hai. |
| 3 | `print(week_days)` | Complete tuple print hota hai. |
| 4 | `print(week_days[1])` | Index 1 second item access karta hai. Output Tuesday hai. |

---

# 9. Dictionaries

## Topic Samjho

Dictionary key-value pair data store karta hai. Example: student ka name, age, city ek dictionary mein store kar sakte hain.

## Kyu Use Karte Hain?

Jab labelled data store karna ho, dictionary best hoti hai. Example: `name: Rahul`, `age: 21`, `course: Python`.

## Fayda

Dictionary se data meaningful keys ke through access hota hai.

## Practice Code 9

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print(student["name"])
print(student["course"])
```

## Output

```text
Rahul
Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = {` | Dictionary start hoti hai. Curly braces dictionary ke liye use hote hain. |
| 2 | `"name": "Rahul"` | Key `name` hai and value Rahul hai. |
| 3 | `"age": 21` | Key age hai and value 21 hai. |
| 4 | `"course": "Python"` | Course key ke andar Python value store hai. |
| 7 | `print(student["name"])` | Name key ki value access hoti hai. Output Rahul hai. |
| 8 | `print(student["course"])` | Course key ki value access hoti hai. Output Python hai. |

---

# 10. Sets

## Topic Samjho

Set unique values ka collection hota hai. Set duplicate values store nahi karta.

## Kyu Use Karte Hain?

Jab unique items chahiye hon, set use hota hai. Example: unique cities, unique skills, unique roll numbers.

## Fayda

Set automatically duplicate values remove karta hai.

## Practice Code 10

```python
skills = {"Python", "SQL", "Python", "Excel"}

print(skills)
print("Python" in skills)
```

## Output

```text
{'Python', 'SQL', 'Excel'}
True
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `skills = {"Python", "SQL", "Python", "Excel"}` | Set create kiya gaya hai. Python duplicate hai, but set duplicate value ko ek hi baar rakhega. |
| 3 | `print(skills)` | Set print hota hai with unique values only. Order fixed guarantee nahi hota. |
| 4 | `print("Python" in skills)` | Membership check hota hai. Python set mein present hai, so output True hai. |

---

# Structured Practice Examples for Day 5

# Functions, Strings & Data Structures

Day 5 me students ko ye samjhana important hai ki programming sirf line by line instructions likhne ka naam nahi hai. Jab code bada hota hai, to hume usko organize karna padta hai. Functions code ko reusable banate hain. Strings text data handle karte hain. Lists, tuples, dictionaries, and sets multiple values ko structured way me store karte hain. Ye topics future me data science, web development, automation, and real applications ke base banenge.

Teacher speaking flow: "Aaj hum Python ko thoda professional style me likhna start karenge. Ab tak hum simple variables, conditions, loops, aur mini project kar chuke hain. Lekin agar project bada ho jaaye, to same code baar-baar likhna problem ban jaata hai. Functions se code reusable banega, aur data structures se data ko smart way me store karna seekhenge."

---

# 1. Defining Functions

Function reusable code block hota hai. Jab koi kaam baar-baar karna ho, to uska function bana dete hain. Function define karne ke liye `def` keyword use hota hai. Function define karna matlab ek machine banana. Function call karna matlab us machine ko start karna.

## Practice Code 1.1 - Welcome Function

```python
def welcome():
    print("Welcome to Python class")
    print("Today we will learn functions")

welcome()
```

## Output

```text
Welcome to Python class
Today we will learn functions
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def welcome():` | `def` keyword Python ko batata hai ki hum function define kar rahe hain. `welcome` function ka naam hai. Brackets function syntax ka part hain. Colon ke baad function ka block start hota hai. |
| 2 | `print("Welcome to Python class")` | Ye line function ke andar hai because indentation hai. Jab function call hoga tab ye first message print hoga. |
| 3 | `print("Today we will learn functions")` | Ye second message hai. Ye bhi function ke andar ka part hai. |
| 5 | `welcome()` | Ye function call hai. Sirf function define karne se code run nahi hota. Function ke andar ka code tab run hota hai jab function ko call kiya jaata hai. |

## Practice Code 1.2 - Function for Daily Task

```python
def start_class():
    print("Take attendance")
    print("Revise previous topic")
    print("Start today's topic")

start_class()
```

## Output

```text
Take attendance
Revise previous topic
Start today's topic
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def start_class():` | Function ka naam `start_class` rakha gaya hai. Naam meaningful hai, isliye code padhte hi samajh aata hai ki function class start karne ke steps rakhta hai. |
| 2-4 | `print(...)` | Ye three lines function ke andar ke steps hain. Function call hone par ye steps same order me execute honge. |
| 6 | `start_class()` | Ye call function ko run karta hai. Is example se students ko samajh aata hai ki function ek task ko group kar sakta hai. |

---

# 2. Function Parameters & Arguments

Parameter function definition me placeholder hota hai. Argument actual value hoti hai jo function call karte time pass ki jaati hai. Simple words me, parameter empty box hai aur argument us box ke andar rakhi hui real value hai.

## Practice Code 2.1 - Welcome Student By Name

```python
def welcome_student(name):
    print("Welcome", name)
    print(name, "is learning Python")

welcome_student("Rahul")
welcome_student("Ayesha")
```

## Output

```text
Welcome Rahul
Rahul is learning Python
Welcome Ayesha
Ayesha is learning Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def welcome_student(name):` | `name` parameter hai. Function ko flexible banane ke liye parameter use hota hai. |
| 2 | `print("Welcome", name)` | Jo argument function call me pass hoga, wo `name` ki jagah use hoga. |
| 3 | `print(name, "is learning Python")` | Same parameter ko second sentence me bhi use kiya gaya hai. |
| 5 | `welcome_student("Rahul")` | `"Rahul"` argument hai. Function call ke time ye value `name` parameter me chali jaati hai. |
| 6 | `welcome_student("Ayesha")` | Same function different value ke saath run hota hai. Isi ko reusability kehte hain. |

## Practice Code 2.2 - Add Two Numbers

```python
def add_numbers(num1, num2):
    total = num1 + num2
    print("Total:", total)

add_numbers(10, 20)
add_numbers(50, 70)
```

## Output

```text
Total: 30
Total: 120
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def add_numbers(num1, num2):` | Function two parameters accept karta hai. `num1` and `num2` placeholders hain. |
| 2 | `total = num1 + num2` | Dono parameters ki values add hoti hain. Result `total` variable me store hota hai. |
| 3 | `print("Total:", total)` | Calculated total display hota hai. |
| 5 | `add_numbers(10, 20)` | Here 10 goes into `num1` and 20 goes into `num2`. Output 30 aata hai. |
| 6 | `add_numbers(50, 70)` | Same function dusri values ke saath run hota hai. Output 120 aata hai. |

---

# 3. Return Statement

`return` function ka result bahar bhejne ke liye use hota hai. Agar function ke andar calculation hoti hai aur us result ko baad me use karna ho, to `return` use karte hain. `print()` sirf screen par dikhata hai, but `return` value ko program ke next step ke liye available banata hai.

## Practice Code 3.1 - Return Total Marks

```python
def calculate_total(math, science, english):
    total = math + science + english
    return total

marks = calculate_total(85, 90, 80)
print("Total Marks:", marks)
```

## Output

```text
Total Marks: 255
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def calculate_total(math, science, english):` | Function three subject marks accept karta hai. |
| 2 | `total = math + science + english` | Marks add karke total calculate hota hai. |
| 3 | `return total` | Function calculated value ko caller ke paas wapas bhejta hai. |
| 5 | `marks = calculate_total(85, 90, 80)` | Function call hota hai and returned value `marks` variable me store hoti hai. |
| 6 | `print("Total Marks:", marks)` | Returned value ko output me display kiya jaata hai. |

## Practice Code 3.2 - Return Percentage

```python
def calculate_percentage(total, maximum):
    percentage = (total / maximum) * 100
    return percentage

result = calculate_percentage(432, 500)
print("Percentage:", result)
```

## Output

```text
Percentage: 86.4
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `def calculate_percentage(total, maximum):` | Function total and maximum marks accept karta hai. |
| 2 | `percentage = (total / maximum) * 100` | Percentage formula apply hota hai. |
| 3 | `return percentage` | Calculated percentage function ke bahar bheji jaati hai. |
| 5 | `result = calculate_percentage(432, 500)` | Function call ka returned value `result` me store hota hai. |
| 6 | `print("Percentage:", result)` | Percentage output me print hoti hai. |

---

# 4. Lambda Functions

Lambda function small anonymous function hota hai. Iska use tab karte hain jab one-line short logic banana ho. Lambda ko beginner level par simple rakho: "short function for short task." Large logic ke liye normal `def` function better hota hai.

## Practice Code 4.1 - Square Using Lambda

```python
square = lambda number: number * number

print(square(5))
print(square(8))
```

## Output

```text
25
64
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `square = lambda number: number * number` | Lambda ek input `number` leta hai aur uska square return karta hai. Ye short function `square` variable me store hai. |
| 3 | `print(square(5))` | `square` function 5 ke saath call hota hai. 5 * 5 = 25 output aata hai. |
| 4 | `print(square(8))` | Same lambda 8 ke saath run hota hai. 8 * 8 = 64 output aata hai. |

## Practice Code 4.2 - Add GST Using Lambda

```python
add_gst = lambda price: price + (price * 0.18)

print(add_gst(1000))
```

## Output

```text
1180.0
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `add_gst = lambda price: price + (price * 0.18)` | Lambda product price leta hai. Price ka 18 percent GST calculate hota hai aur original price me add hota hai. |
| 3 | `print(add_gst(1000))` | Lambda 1000 price par run hota hai. GST 180 banta hai, final price 1180.0 print hota hai. |

---

# 5. String Basics

String text data hota hai. Name, email, course name, city, address, message, password, and comments sab strings hote hain. Python me string quotes ke andar likhi jaati hai.

## Practice Code 5.1 - Create and Print String

```python
student_name = "Rahul Sharma"
course = "Python"

print(student_name)
print(course)
print(type(student_name))
```

## Output

```text
Rahul Sharma
Python
<class 'str'>
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = "Rahul Sharma"` | Text value quotes ke andar hai, isliye ye string hai. |
| 2 | `course = "Python"` | Course name bhi string format me store hai. |
| 4 | `print(student_name)` | Student name output me print hota hai. |
| 5 | `print(course)` | Course value print hoti hai. |
| 6 | `print(type(student_name))` | `type()` confirm karta hai ki variable string hai. |

## Practice Code 5.2 - String With Sentence

```python
name = "Neha"
city = "Mumbai"

print(name, "is from", city)
```

## Output

```text
Neha is from Mumbai
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Neha"` | Name string variable me store hai. |
| 2 | `city = "Mumbai"` | City bhi string value hai. |
| 4 | `print(name, "is from", city)` | Multiple strings and variables ko comma ke saath print kiya gaya hai. Python automatically spaces add karta hai. |

---

# 6. String Operations

String operations text ko modify, search, count, format, and clean karne ke kaam aate hain. Real apps me user input messy ho sakta hai. Example: user name small letters me likhe, extra spaces daal de, email uppercase me likh de. String methods data ko clean banate hain.

## Practice Code 6.1 - Upper, Lower, Length

```python
name = "Rahul Sharma"

print(name.upper())
print(name.lower())
print(len(name))
```

## Output

```text
RAHUL SHARMA
rahul sharma
12
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Rahul Sharma"` | String value variable me store hai. |
| 3 | `print(name.upper())` | `upper()` string ko uppercase me convert karta hai. Original string change nahi hoti; output uppercase version hota hai. |
| 4 | `print(name.lower())` | `lower()` string ko lowercase me convert karta hai. |
| 5 | `print(len(name))` | `len()` string ke total characters count karta hai, spaces included. |

## Practice Code 6.2 - Strip and Replace

```python
message = "  I love Java  "

clean_message = message.strip()
new_message = clean_message.replace("Java", "Python")

print(new_message)
```

## Output

```text
I love Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `message = "  I love Java  "` | String ke start and end me extra spaces hain. Real user input me aisi problem common hoti hai. |
| 3 | `clean_message = message.strip()` | `strip()` extra starting and ending spaces remove karta hai. |
| 4 | `new_message = clean_message.replace("Java", "Python")` | `replace()` old text ko new text se replace karta hai. |
| 6 | `print(new_message)` | Clean and updated message output me print hota hai. |

---

# 7. Lists

List multiple values ka ordered collection hota hai. List changeable hoti hai, matlab hum items add, remove, and update kar sakte hain. Student names, marks, products, tasks, and skills store karne ke liye list very useful hai.

## Practice Code 7.1 - Create and Access List

```python
fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
print(fruits[2])
```

## Output

```text
['apple', 'banana', 'mango']
apple
mango
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `fruits = ["apple", "banana", "mango"]` | List square brackets me create hoti hai. Is list me three string items hain. |
| 3 | `print(fruits)` | Complete list print hoti hai. |
| 4 | `print(fruits[0])` | Index 0 first item ko access karta hai. Python indexing 0 se start hoti hai. |
| 5 | `print(fruits[2])` | Index 2 third item ko access karta hai. |

## Practice Code 7.2 - Add Item in List

```python
skills = ["Python", "SQL"]

skills.append("Excel")

print(skills)
```

## Output

```text
['Python', 'SQL', 'Excel']
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `skills = ["Python", "SQL"]` | Skills list me two values initially store hain. |
| 3 | `skills.append("Excel")` | `append()` list ke end me new item add karta hai. List mutable hoti hai, isliye change allowed hai. |
| 5 | `print(skills)` | Updated list output me print hoti hai. |

---

# 8. Tuples

Tuple multiple values ka ordered collection hota hai, but tuple immutable hota hai. Immutable ka matlab once create hone ke baad values change nahi hoti. Fixed data ke liye tuple useful hai, jaise date of birth, coordinates, fixed profile information.

## Practice Code 8.1 - Create Tuple

```python
student = ("Aman", 21, "Python")

print(student)
print(student[0])
```

## Output

```text
('Aman', 21, 'Python')
Aman
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = ("Aman", 21, "Python")` | Tuple parentheses me create hota hai. Isme name, age, and course store hain. |
| 3 | `print(student)` | Complete tuple print hota hai. |
| 4 | `print(student[0])` | Index 0 tuple ka first item access karta hai. |

## Practice Code 8.2 - Tuple Unpacking

```python
student = ("Neha", 22, "Data Science")

name, age, course = student

print(name)
print(age)
print(course)
```

## Output

```text
Neha
22
Data Science
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = ("Neha", 22, "Data Science")` | Tuple me three values store hain. |
| 3 | `name, age, course = student` | Tuple unpacking me tuple ki values separate variables me assign ho jaati hain. |
| 5-7 | `print(...)` | Har unpacked variable separately print hota hai. |

---

# 9. Dictionaries

Dictionary key-value pair me data store karta hai. Jab hume labeled data chahiye, dictionary best choice hoti hai. Example: name, age, course, marks. List me values index se milti hain, dictionary me values key se milti hain.

## Practice Code 9.1 - Student Dictionary

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print(student["name"])
print(student["course"])
```

## Output

```text
Rahul
Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = {` | Dictionary curly braces me start hoti hai. |
| 2 | `"name": "Rahul"` | `"name"` key hai and `"Rahul"` value hai. |
| 3 | `"age": 21` | Age key numeric value store karti hai. |
| 4 | `"course": "Python"` | Course key course name store karti hai. |
| 7 | `print(student["name"])` | Key ke through name value access hoti hai. |
| 8 | `print(student["course"])` | Key ke through course value access hoti hai. |

## Practice Code 9.2 - Update Dictionary

```python
student = {"name": "Ayesha", "marks": 85}

student["marks"] = 92
student["grade"] = "A+"

print(student)
```

## Output

```text
{'name': 'Ayesha', 'marks': 92, 'grade': 'A+'}
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student = {"name": "Ayesha", "marks": 85}` | Dictionary me name and marks store hain. |
| 3 | `student["marks"] = 92` | Existing marks value update hoti hai. Dictionary mutable hoti hai. |
| 4 | `student["grade"] = "A+"` | New key `grade` add hoti hai. |
| 6 | `print(student)` | Updated dictionary output me print hoti hai. |

---

# 10. Sets

Set unique values ka collection hota hai. Set duplicate values ko automatically remove kar deta hai. Jab hume unique data chahiye, set useful hota hai. Example: unique student IDs, unique skills, unique cities, unique subject names.

## Practice Code 10.1 - Unique Skills

```python
skills = {"Python", "SQL", "Python", "Excel"}

print(skills)
print("Python" in skills)
```

## Output

```text
{'Python', 'SQL', 'Excel'}
True
```

Note: Set ka order fixed guarantee nahi hota. Output me items ka order different aa sakta hai, but duplicate Python only one time rahega.

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `skills = {"Python", "SQL", "Python", "Excel"}` | Set curly braces me create hua hai. Python duplicate hai, but set duplicate value ko one time rakhta hai. |
| 3 | `print(skills)` | Unique values print hoti hain. Order fixed nahi hota. |
| 4 | `print("Python" in skills)` | Membership operator `in` check karta hai ki Python set me present hai ya nahi. Since present hai, output True hai. |

## Practice Code 10.2 - Convert List to Set

```python
cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]

unique_cities = set(cities)

print(unique_cities)
```

## Output

```text
{'Delhi', 'Mumbai', 'Pune'}
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]` | List me duplicate city names hain. Real data me duplicate values common hoti hain. |
| 3 | `unique_cities = set(cities)` | `set()` list ko set me convert karta hai. Conversion ke time duplicate values remove ho jaati hain. |
| 5 | `print(unique_cities)` | Unique cities output me print hoti hain. Order fixed guarantee nahi hota. |
