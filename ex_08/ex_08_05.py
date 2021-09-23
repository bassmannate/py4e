while True:
  file = input("Please enter a file name: ")
  if len(file) < 1:
    fhand = open("mbox-short.txt")
    break
  else:
    try:
      fhand = open(file)
      break
    except:
      print("You must enter a valid file name.")
      continue
count = 0
for line in fhand:
  line = line.rstrip()
  if line.startswith("From "):
    words = line.split()
    print(words[1])
    count = count + 1
print(count)
