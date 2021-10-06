import re

while True:
  file = input("Please enter a file name or \"quit\" to quit: ")
  if len(file) < 1:
    fhand = open("../mbox-short.txt")
    break
  elif file.lower() == "quit":
    exit()
  else:
    try:
      fhand = open(file)
      break
    except:
      print("You must enter a valid file name.")
      continue

total = None
count = 0

for line in fhand:
  if re.search('^New Revision:', line):
    if total == None:
      number = re.findall('[0-9]+', line)
      total = int(number[0])
    else:
      number = re.findall('[0-9]+', line) 
      total += int(number[0])
    count += 1
print(int(total/count))