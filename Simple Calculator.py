first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))
operation =  input ("what operation would you like to do: add, subtract, multiply, or divide? ")

def add(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

def subtract(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")

def multiply(num1, num2):
    print(f"{num1} * {num2} = {num1 * num2}")

def divide(num1, num2):
    print(f" {num1} / {num2} = {num1 / num2} ")

if operation == 'add':
    add(first_number, second_number)
elif operation == 'subtract':
    subtract(first_number, second_number)
elif operation == 'multiply':
    multiply(first_number, second_number)
elif operation == 'divide':
    divide(first_number, second_number)