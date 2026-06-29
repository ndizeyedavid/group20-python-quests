#!/usr/bin/python3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: You can not divide by zero"
    return a / b

number1 = float(input("Enter the first number: "))
operation = input("Enter the operation (add, subtract, multiply, or divide): ").lower()
number2 = float(input("Enter the second number: "))

if operation == "add":
    result = add(number1, number2)

elif operation == "subtract":
    result = subtract(number1, number2)

elif operation == "multiply":
    result = multiply(number1, number2)

elif operation == "divide":
    result = divide(number1, number2)

else: 
    result = "Invalid operation"


print("Result:", result)
