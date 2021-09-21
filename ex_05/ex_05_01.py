pieces = list()
while True:
  num = input("Please enter a number: ")
  if num == "done":
    break
  try:
    num = int(num)
  except:
    print("Input must be numeric")
    exit()
  pieces = pieces.append(num)
print(pieces)