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

hours = dict()

for line in fhand:
  if line.startswith("From "):
    hour = line.split()[5].split(":")[0]
    hours[hour] = hours.get(hour, 0) + 1
#print(hours)

lst = list()

for k, v in list(hours.items()):
  lst.append((k, v))
lst.sort()
for k, v in lst:
  print(k, v)
