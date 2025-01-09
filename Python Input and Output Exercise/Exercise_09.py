# Exercise 9: Check file is empty or not

f = open("ankita.txt")

word = f.readlines()
count = 0
for i in range(len(word)):
    count = count + 1

if (count != 0):
    print("File is not empty")
else:
    print("File is empty")