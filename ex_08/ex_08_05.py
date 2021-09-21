fname = 'mbox-short.txt'
#fname = input("Enter file name: ")
#if len(fname) < 1:
#    fname = "mbox-short.txt"

fh = open('mbox-short.txt')
count = 0
for line in fh:
    print(line)
    wds = line.rstrip()
    if wds[0] != 'From':
        continue
    count = count + 1
    print(line[1])
print("There were", count, "lines in the file with From as the first word")
