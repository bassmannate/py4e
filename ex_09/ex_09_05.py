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
domaincount = dict()
for line in fhand:
  line = line.rstrip()
  if line.startswith("From "):
    words = line.split()
    address = words[1].split("@")
    domain = address[1]
    if domain not in domaincount:
      domaincount[domain] = 1
    else:
      domaincount[domain] = domaincount[domain] + 1
      
print(domaincount)
