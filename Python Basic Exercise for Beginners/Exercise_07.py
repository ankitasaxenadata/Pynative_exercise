# Exercise 7: Find the number of occurrences of a substring in a string

"""Write a Python code to find how often the substring “Emma” appears in the given string."""

str = input("Enter the string : ")

list = str.split()
print(list)
count = 0

for i in range (len(list)):
    if (list[i] == 'Emma'):
        count = count + 1
print("Emma appeared ", count ,"times.")