import socket

host = 'localhost'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
a = input().encode()
b = input().encode()
c = input().encode()
s.send(a + '#'.encode() + b + '#'.encode() + c)
ans = s.recv(1024).decode()
print ('answer', ans)



