fhand = open("words.txt")
wordcount = dict()
for line in fhand:
  line = line.rstrip()
  words = line.split()
  for word in words:
    if word not in wordcount:
      wordcount[word] = 1
    else:
      wordcount[word] = wordcount[word] + 1
print(wordcount)
