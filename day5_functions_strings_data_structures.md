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

