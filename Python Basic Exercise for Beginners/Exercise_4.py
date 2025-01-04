# Exercise 4: Remove first n characters from a string

"""Write a Python code to remove characters from a string from 0 to n and return a new string.

For Example:

remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string."""

str = input("Enter the string: ")
remove = int(input("How many characters do you want to remove from the start = "))
length = len(str)

word = ""
for i in range (length):
    if i in range (remove,length):
        word = word + str[i]
print(word)

