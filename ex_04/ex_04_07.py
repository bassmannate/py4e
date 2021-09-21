def computegrade(score):
  if score > 1.0 or score < 0.0:
    print("You must enter a numeric value between 0.0 and 1.0.")
    exit()
  elif score >= 0.9:
    grade = "A"
  elif score >= 0.8:
    grade = "B"
  elif score >= 0.7:
    grade = "C"
  elif score >= 0.6:
    grade = "D"
  else:
    grade = "F"
  return grade

try:
  score = float(input("Please enter a score: "))
except:
  print("You must enter a numeric value between 0.0 and 1.0.")
  exit()

grade = computegrade(score)
print(grade)
