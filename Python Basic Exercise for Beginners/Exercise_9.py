# Exercise 9: Check Palindrome Number

"""Write a Python code to check if the given number is palindrome. 
    A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number"""

original_num = int(input("Enter the number: "))
reverse_num = 0


while num != 0:
    n = num % 10
    rev = rev * 10 + n
    num = num // 10
print(rev)
print(num)
if ( rev == num):
    print("given number is palindrome number")
else:
    print("given number is not palindrome number")