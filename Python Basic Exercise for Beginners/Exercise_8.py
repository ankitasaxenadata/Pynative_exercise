# Exercise 8: Print the following pattern

"""
1
2   2
3   3   3
4   4   4   4
5   5   5   5   5
"""

# input the size of the pattern
size = int(input("Enter the size: "))

# logic of the pattern

for i in range (size + 1):
    for j in range (i):
        print(i,"\t", end = " ")
    print()