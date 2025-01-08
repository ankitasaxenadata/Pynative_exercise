# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”

"""
Expected Output:
For example: print('Name', 'Is', 'James') will display Name**Is**James"""

string = input("Enter the string = ")

con_list = string.split()
convert = str(con_list)[1:-1]

word = '**'.join(con_list)
print(convert)
print(word)