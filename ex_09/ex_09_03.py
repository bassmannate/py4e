while True:
  file = input("Please enter a file name: ")
  if len(file) < 1:
    fhand = open("../mbox-short.txt")
    break
  else:
    try:
      fhand = open(file)
      break
    except:
      print("You must enter a valid file name.")
      continue
days = dict()
for line in fhand:
  line = line.rstrip()
  if line.startswith("From "):
    words = line.split()
    if words[1] not in days:
      days[words[1]] = 1
    else:
      days[words[1]] = days[words[1]] + 1
      
print(days)
