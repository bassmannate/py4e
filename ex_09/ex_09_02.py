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
    if words[2] not in days:
      days[words[2]] = 1
    else:
      days[words[2]] = days[words[2]] + 1
print(days)
