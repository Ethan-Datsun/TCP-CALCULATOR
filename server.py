import socket

host = 'localhost'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print ('server is ready')
con, addr = s.accept()
print ('connect by', addr, con)
while 1:
	data = con.recv(1024).decode()
	token = data.split('#',3)
	oper = token[0]
	a = int(token[1])
	b = int(token[2])
	if oper == '+' :
		c = a + b
	elif oper == '-' :
		c = a - b
	elif oper == '*' :
		c = a * b
	elif oper == '/':
		c = a / b
	con.send(str(c).encode())
	con.close()
	break
s.close()
