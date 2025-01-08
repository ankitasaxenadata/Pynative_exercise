# Exercise 3: Convert Decimal number to octal using print() output formatting

"""
Expected Output:
The octal number of decimal number 8 is 10"""

num = int(input("num = "))
original = num
list1 = ""

while num > 0:
    q = num // 8  
    r = num % 8
    list1 = list1 + str(r) # reverse to get the octal number
    num = q

print("The octal number of decimal number",original,"is",list1[::-1])
    

