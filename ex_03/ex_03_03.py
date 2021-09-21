try:
  score = float(input("Please enter a score: "))
except:
  print("You must enter a numeric value between 0.0 and 1.0.")
  exit()
if score > 1.0 or score < 0.0:
  print("You must enter a numeric value between 0.0 and 1.0.")
  exit()
elif score >= 0.9:
  print("A")
elif score >= 0.8:
  print("B")
elif score >= 0.7:
  print("C")
elif score >= 0.6:
  print("D")
else:
  print("F")