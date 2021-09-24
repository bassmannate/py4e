def count(w, l):
  x = 0
  for letter in w:
    #print(letter)
    if letter is l:
        x = x + 1
  return x


word = 'banana'

print(count("banana", "a"))
