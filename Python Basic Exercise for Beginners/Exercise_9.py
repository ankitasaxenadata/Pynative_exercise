# Exercise 9: Check Palindrome Number

"""Write a Python code to check if the given number is palindrome. 
    A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number"""

num = int(input("Enter the number: "))
original_num = num
rev = 0

# logic for reversing the string
while num != 0:
    n = num % 10
    rev = rev * 10 + n
    num = num // 10

# comparing original number with the reverse number
if ( rev == original_num):
    print("given number is palindrome number")
else:
    print("given number is not palindrome number")