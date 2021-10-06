import re

fhand = open("../mbox.txt")
count = 0

regex = input("Please enter a regular expression: ")

for line in fhand:
  if re.search(regex, line):
    count += 1
print('mbox.txt had', count, 'lines that matched', regex)