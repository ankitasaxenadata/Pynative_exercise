# Exercise 10: Read line number 4 from the following file

file = open("test.txt")

word = file.readlines()
count = 0
for i in range(len(word)):
    count = count + 1
    if (count == 4):
        print(word[i])