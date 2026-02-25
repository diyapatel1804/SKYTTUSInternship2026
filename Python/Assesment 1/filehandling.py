# Read a file and display its contents

file = open("sample.txt", "r")
print(file.read())
file.close()

# Count number of lines in a file

file=open("sample.txt","r")
lines = file.readlines()
print("Number of lines:",len(lines))
file.close()

# Count how many times each word appears in a file

file = open("sample.txt","r")
words = file.read().split()
count = {}

for w in words:
    count[w] = count.get(w,0) + 1

print(count)
file.close()

# Write 5 user-entered sentences to a file

file = open("sentences.txt","w")

for i in range(5):
    line = input("Enter sentence: ")
    file.write(line + "\n")
file.close()

# Append a list of strings to an existing file

data = ["Apple", "Banana", "Mango"]

file = open("sample.txt", "a")
for item in data:
    file.write(item + "\n")
file.close()

# Print only lines containing a specific word

word = input("Enter word to search: ")

file = open("sample.txt", "r")
for line in file:
    if word in line:
        print(line)
file.close()

# Replace a specific word in a file

file = open("sample.txt", "r")
content = file.read()
file.close()

content = content.replace("old", "new")

file = open("sample.txt", "w")
file.write(content)
file.close()

# Merge contents of two files into a third file

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f3 = open("merged.txt", "w")

f3.write(f1.read())
f3.write(f2.read())

f1.close()
f2.close()
f3.close()

# Read a CSV file and display formatted output

import csv

file = open("data.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(" | ".join(row))

file.close()

# Back up a file by copying its contents

source = open("sample.txt", "r")
backup = open("backup.txt", "w")

backup.write(source.read())

source.close()
backup.close()
