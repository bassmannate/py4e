count = 0
total = 0
while True:
  num = input("Please enter a number: ")
  if num == "done":
    break
  try:
    num = float(num)
  except:
    print("Input must be numeric")
    continue
  total = total + num
  count = count +1
print(total,count,total / count)


