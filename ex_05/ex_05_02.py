maximum = None
minimum = None
while True:
  num = input("Please enter a number: ")
  if num == "done":
    break
  try:
    num = float(num)
  except:
    print("Input must be numeric")
    continue
  if maximum is None or maximum < num:
    maximum = num
  if minimum is None or minimum > num:
    minimum = num
print("Maximum:",maximum,"Minimum:",minimum)
