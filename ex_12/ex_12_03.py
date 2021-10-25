import urllib.request, urllib.parse, urllib.error

count = 0

#text = ''

while True:
    address = input("Enter a valid URL: ")
    if len(address) < 1:
        address = "http://data.pr4e.org/romeo-full.txt"
        break
    else:
        break

text = urllib.request.urlopen(address).read()

for i in text:
  count += 1

print(text[:2999], "\n", "Count: ", count)