import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 8080))
mysock.send('GET /zl/ HTTP/1.0\n\n')
while True:
  data = mysock.recv(512)
  if ( len(data) < 1 ) :
    break
  print data
mysock.close()
