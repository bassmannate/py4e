def computepay(hours,rate):
  otrate = rate * 1.5
  if hours > 40:
    othours = hours - 40
    otpay = otrate * othours
    regpay = rate * 40
    pay = otpay + regpay
  else:
    pay = hours * rate
  return pay

try:
  hours = float(input("Enter the hours: "))
  rate = float(input("Enter the pay rate: "))
except:
  print("Please enter numeric input.")
  quit()

print("Pay:",computepay(hours,rate))