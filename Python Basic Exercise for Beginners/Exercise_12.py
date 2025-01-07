# Exercise 12: Calculate income tax

"""Calculate income tax for the given income by adhering to the rules below
    
| Taxable Income       | Rate (in %) |
|----------------------|-------------|
| First $10,000        | 0           |
| Next $10,000         | 10          |
| The remaining        | 20          |
"""

taxable_income = int(input("Enter the taxable income: "))
n1 = 0

if ( taxable_income <= 10000):
    tax = taxable_income * 0
elif ( taxable_income <= 20000):
    tax = (taxable_income - 10000) * 0.10
else:
    n1 = 10000 * 0.10
    n2 = (taxable_income - 20000) * 0.20
    tax = n1 + n2

print(tax)