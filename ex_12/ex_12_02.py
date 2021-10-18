import socket

count = 0

text = ''

while True:
    address = input("Enter a valid URL: ")
    if len(address) < 1:
        address = "http://data.pr4e.org/romeo.txt"
        break
    else:
        break

addresspiece = address.split("/")
domain = addresspiece[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((domain, 80))
cmd = 'GET ' + address + ' HTTP/1.0\r\n\r\n'
mysock.send(cmd.encode())

while True:
    data = mysock.recv(4096)
    if len(data) < 1:
        break
    text += data.decode()
#    datastrip = data.decode().rstrip()
    #for i in data:
      #count += 1
      #if count > 2997:
        #print(data.decode()[:count], end='')
        #break
    #print(data.decode(), end='')

textsplit = text.split("Content-Type:", *, "\n\r")[1]
for i in textsplit:
  count += 1
  if count > 2999:
    break

mysock.close()
#print(text[:3000])
print(textsplit)
print("Characters:",count)