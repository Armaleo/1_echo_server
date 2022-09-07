import socket


sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.0.2.15', 9090))
while msg!= 'exit':
	msg = input()
	sock.send(msg.encode())

	data = sock.recv(1024)

	print(data.decode())

sock.close()
