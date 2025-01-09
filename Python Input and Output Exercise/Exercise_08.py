# Exercise 8: Format variables using a string.format() method.

total_money = int(input("totalMoney = "))
quantity = int(input("quantity = "))
price = int(input("price = "))

print("I have {0} dollars so I can buy {1} football for {2:.2f} dollars.".format(total_money, quantity, price))