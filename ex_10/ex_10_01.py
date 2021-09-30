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
addresses = dict()
for line in fhand:
  line = line.rstrip()
  if line.startswith("From "):
    words = line.split()
    if words[1] not in addresses:
      addresses[words[1]] = 1
    else:
      addresses[words[1]] = addresses[words[1]] + 1

if len(addresses) == 0:
  print("No addresses found")
  exit()
lst = list()
for key, val in list(addresses.items()):
  lst.append((val, key))
lst.sort(reverse = True)
print(lst[0])
