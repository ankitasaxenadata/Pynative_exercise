# Exercise 6: Write all content of a given file into a new file by skipping line number 5

count = 0
with open('test.txt') as f:
    for line in f:
        count = count + 1 # count the line number so that we can eliminate line number 5
        if( count != 5):
            print(line.strip())
