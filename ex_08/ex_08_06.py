data = list()
while True:
  num = input("Please enter a number: ")
  if num == "done":
    break
  try:
    num = float(num)
  except:
    print("Input must be numeric")
    continue
  data.append(num)
#data.sort()
maximum = max(data)
minimum = min(data)
print("Maximum:",maximum,"Minimum:",minimum)