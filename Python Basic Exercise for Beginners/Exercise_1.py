# Exercise 1: Calculate the multiplication and sum of two numbers

""" Given two integer numbers, write a Python code to return their product only if the product is
 equal to or lower than 1000. Otherwise, return their sum."""

num1 = int(input("number1 = "))
num2 = int(input("number2 = "))

if num1 * num2 < 1000:
    print("The result is ", (num1 * num2))
else:
    print("The result is ",(num1 + num2))