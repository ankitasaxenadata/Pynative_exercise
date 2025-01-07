# Exercise 15: Get an int value of base raises to the power of exponent

"""
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer."""

def exponent ( base , exp):
    pow = base ** exp
    return pow

base = int(input("base = "))
exp = int(input("exponent = "))

print(base," raises to the power of ",exp,":",exponent(base, exp),
      "i.e.","*".join(str(base) * exp), "=", exponent(base, exp))