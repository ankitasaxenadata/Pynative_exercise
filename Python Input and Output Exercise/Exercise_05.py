# Exercise 5: Accept a list of 5 float numbers as an input from the user

size = int(input("Enter the size of your list = "))
list1 = []

print("Enter the elements in your list: ")

for i in range (size):
    list1.append(float(input()))

print(list1)
