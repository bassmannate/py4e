while True:
  file = input("Please enter a file name or \"quit\" to quit: ")
  if len(file) < 1:
    fhand = open("../words.txt")
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

lettercount = dict()
lst = list()

for line in fhand:
  words = line.rstrip().lower().split()
  for word in words:
    for letter in word:
      if letter.isalpha():
        lettercount[letter] = lettercount.get(letter, 0) + 1

for k, v in list(lettercount.items()):
  lst.append((v, k))
lst.sort(reverse = True)
for v, k in lst:
  print(k,"-", v)
