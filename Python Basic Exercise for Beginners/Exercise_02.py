# Exercise 2: Print the Sum of a Current Number and a Previous number

"""Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of 
the current and previous number"""

# Taking input from the user
num = int(input("Printing current and previous number sum in a range: "))

# declare a counter variable
prev = 0
for i in range (num):
    sum = prev + i
    print("Current Number ",i,"Previous Number", prev,"Sum:", sum)
    prev = i
