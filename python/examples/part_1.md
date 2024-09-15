# Python Basics: Examples for Beginners

## 1. Variables

```python
# Creating and using variables
name = "Alice"
age = 30
height = 1.65

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My height is {height} meters.")
```

Output:
```
My name is Alice.
I am 30 years old.
My height is 1.65 meters.
```

## 2. Data Types

```python
# Demonstrating different data types
integer_num = 42
float_num = 3.14
text = "Python is fun!"
is_beginner = True

print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"String: {text}, Type: {type(text)}")
print(f"Boolean: {is_beginner}, Type: {type(is_beginner)}")
```

Output:
```
Integer: 42, Type: <class 'int'>
Float: 3.14, Type: <class 'float'>
String: Python is fun!, Type: <class 'str'>
Boolean: True, Type: <class 'bool'>
```

## 3. Lists

```python
# Creating and manipulating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last number: {numbers[-1]}")

# Modifying lists
fruits.append("orange")
numbers.remove(3)

print(f"Updated fruits: {fruits}")
print(f"Updated numbers: {numbers}")

# List operations
combined = fruits + numbers
print(f"Combined list: {combined}")
```

Output:
```
First fruit: apple
Last number: 5
Updated fruits: ['apple', 'banana', 'cherry', 'orange']
Updated numbers: [1, 2, 4, 5]
Combined list: ['apple', 'banana', 'cherry', 'orange', 1, 2, 4, 5]
```

## 4. If-Else Statements

```python
# Using if-else statements
age = 18

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Nested if-else
score = 85

if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A!")
    elif score >= 80:
        print("You got a B!")
    else:
        print("You got a C!")
else:
    print("You failed. Try again!")
```

Output:
```
You are a teenager.
You passed!
You got a B!
```

## 5. Operators

```python
# Arithmetic operators
a = 10
b = 3

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")

# Comparison operators
x = 5
y = 8

print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")

# Logical operators
p = True
q = False

print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")
```

Output:
```
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Exponentiation: 1000
x == y: False
x != y: True
x < y: True
x > y: False
p and q: False
p or q: True
not p: False
```
