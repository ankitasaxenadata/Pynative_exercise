# Exercise 6: Display numbers divisible by 5

"""Write a Python code to display numbers from a list divisible by 5."""

size = int(input("Enter the size of the list: "))
list_1 = []

def check():
    for i in range (size):
        if (list_1[i] % 5 == 0):
            print(list_1[i])
        

# input list from the user

for ele in range (size):
    list_1.append(int(input()))
print(list_1)
print("Divisible by 5")
check()
