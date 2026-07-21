# Day 5 - Functions, Strings & Data Structures

## Topics Covered

Defining Functions, Function Parameters & Arguments, Return Statement, Lambda Functions, String Basics, String Operations, Lists, Tuples, Dictionaries, and Sets.

Day 5 ka goal hai code ko reusable banana and data ko better structure mein store karna. Ab tak hum variables, conditions, loops, and mini project kar chuke hain. Lekin real projects mein code bada hota hai. Agar hum same code baar-baar likhenge to program messy ho jaayega. Functions code ko reusable banate hain. Strings text handle karte hain. Lists, tuples, dictionaries, and sets multiple data ko organize karte hain.

---

Teacher speaking flow: Aaj hum Python ko thoda professional style me likhna start karenge. Ab tak hum simple variables, conditions, loops, aur mini project kar chuke hain. Lekin agar project bada ho jaaye, to same code baar-baar likhna problem ban jaata hai. Functions se code reusable banega, aur data structures se data ko smart way me store karna seekhenge. Har topic ke andar same format follow karenge: concept, real use, fayda, practice code, output, aur detailed explanation.

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
