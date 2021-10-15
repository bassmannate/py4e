import socket

count = 0

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
    datastrip = data.decode().rstrip()
    for i in datastrip:
      count += 1
      if count > 2998:
        break
    print(data.decode(), end='')

mysock.close()
print("Characters:",count)