# Exercise 10: Merge two lists using the following condition

"""Given two lists of numbers, write a Python code to create a new list such that the latest list should
    contain odd numbers from the first list and even numbers from the second list."""

size1 = int(input("Enter the size of first list: "))
size2 = int(input("Enter the size of second list: "))
list1 = []
list2 = []

# enter the elements in the list1 & list2
print("Enter the elements of First list")
for i in range (size1):
    list1.append(int(input()))
print("The First list is ", list1)

print("Enter the elements of Second list")
for i in range (size2):
    list2.append(int(input()))
print("The Second list is ", list2)

list3 =[]

for i in range (size1):
    if(list1[i] % 2 != 0):
        list3.append(list1[i])

for i in range (size2):
    if(list2[i] % 2  == 0):
        list3.append(list2[i])

print("result list : ", list3)
