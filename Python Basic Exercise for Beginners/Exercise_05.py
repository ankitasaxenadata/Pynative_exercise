# Exercise 5: Check if the first and last numbers of a list are the same

"""Write a code to return True if the list's first and last numbers are the same. 
    If the numbers are different, return False."""

size = int(input("Enter the size of the list: "))
list_1 = []

# function to check whether the first and last numbers of the list are same or not

def check():
    for i in range (size):
        if(list_1[0] == list_1[-1]):
            return True
        else:
            return False


# input the list from user
for ele in range (size):
    list_1.append(int(input()))
print(list_1)
check()
print("The result is", check())