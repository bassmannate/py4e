file = input("Please enter a file name: ")
if len(file) < 1:
    fhand = open("romeo.txt")
else:
    try:
        fhand = open(file)
    except:
        print("Please enter a valid file name.")
unique = list()
for line in fhand:
    words = line.rstrip().split()
    for word in words:
        if word not in unique:
            unique.append(word)
unique.sort()
print(unique)
print(len(unique))