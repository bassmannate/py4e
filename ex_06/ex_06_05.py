str = 'X-DSPAM-Confidence:0.8475'
index = str.find(":")
#print(index)
num = float(str[index + 1:])
print(num)
