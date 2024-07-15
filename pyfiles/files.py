# # classwork

# Write a Python program that takes two numbers as input from the user and prints their sum, difference, product,and division as a function

# # * / + -

first_num = int(input("Enter the first number "))
second_num = int(input("Enter yhe second number "))
operation = input("Which operation do you want to do chosse between +, -, / , *  ")


def sum(a,b):
    return a + b

def minus(a,b):
    return a - b

def mult(a,b):
    return a * b

def division(a,b):
    return a /b

if(operation == '+'):
    print(sum(first_num, second_num))
elif(operation == "-"):
    print(minus(first_num, second_num))
elif(operation == "/"):
    print(division(first_num,second_num))
elif(operation == "*"):
    print(mult(first_num,second_num))            












# Write a Python program that takes a string as input and checks if it is a palindrome 
# Hint: [::-1]




# Write a Python program that takes a temperature in Celsius as input and converts it to Fahrenheit.
# hint: fahrenheit = (celsius * 9/5) + 32


