# Exercise 3: Print characters present at an even index number

"""Write a Python code to accept a string from the user and display characters present at an even 
    index number.

For example, str = "PYnative". so your code should display 'P', 'n', 't', 'v'."""

# Displaying original string
original = input("Original String is : ")

print("Printing only even Index chars")

for i in range (len(original)):
    if (i % 2 == 0):
        print(original[i])