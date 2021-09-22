maximum = 0
minimum = 0
while True:
  num = input("Please enter a number: ")
  if num == "done":
    break
  try:
    num = float(num)
  except:
    print("Input must be numeric")
    continue
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum:",maximum,"Minimum:",minimum)
