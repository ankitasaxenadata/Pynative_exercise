# Exercise 14: Print a downward half-pyramid pattern of stars
"""
* * * * *  
* * * *  
* * *  
* *  
*
"""
size = int(input("Enter the size of the pattern: "))

while size != 0:
    print(" * " * size)
    size = size - 1