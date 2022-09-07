import socket

sock = socket.socket()
sock.bind(('', 9090))
msg = ''

while msg != 'exit':

	sock.listen(0)
	conn, addr = sock.accept()
	name = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)

print(msg)

conn.close()
