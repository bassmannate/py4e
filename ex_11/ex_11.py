import re

while True:
  file = input("Please enter a file name or \"quit\" to quit: ")
  if len(file) < 1:
    fhand = open("../regex_sum_42.txt")
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

for line in fhand:
  number = re.findall('[0-9]+', line)
  #print(number)
  for entry in number:
    if total == None:
      total = int(entry)
    else:
      total += int(entry)
print(total)
    