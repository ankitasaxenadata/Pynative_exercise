# Exercise 11: Get each digit from a number in the reverse order.

"""For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space 
separating the digits."""

num = int(input("Enter the number: "))
rev = 0

while num != 0:
    n = num % 10
    rev = rev * 10 + n
    num = num // 10
print(rev)