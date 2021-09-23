file = input("Please enter a file name: ")
if len(file) < 1:
    fhand = open("mbox-short.txt")
elif file == "na na boo boo":
    print("NA NA BOO BOO TO YOU!")
    exit()
else:
    try:
        fhand = open(file)
    except:
        print("Please enter a valid file name.")
        exit()
count = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        words = line.split()
        #print(words)
        total = total + float(words[1])
        count = count + 1
average = total / count
print("Average SPAM confidence:",average)