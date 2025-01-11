# Exercise 9: Check file is empty or not

file = open("ankita.txt")

word = file.readlines()
count = 0
for i in range(len(word)):
    count = count + 1

if (count != 0):
    print("File is not empty")
else:
    print("File is empty")