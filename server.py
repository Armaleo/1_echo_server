import socket
import datetime

print(datetime.now, 'server started')
greet = 'Hello '
sock = socket.socket()
portNum = 9000
while True:

	try: sock.bind(('', portNum))
	except:	portNum += 1
	else: break

print('Server is opened on port: ', portNum)
c = 0
users = {'key':'info'}
print(list(users.keys()))
while c<5:
	print('Looking for connection...')
	sock.listen()
	conn, addr = sock.accept()
	print(addr[0])
	curr = list(users.keys())
	print("Connected by ", addr)
	for i in range(len(curr)):
		if str(curr[i]) == str(addr[0]):
			greet1 = greet + users[addr[0]] + '!'
			conn.send(bytes(greet1, encoding = 'utf-8'))
			break
	else:
		print('nickname requested')
		conn.send(b'Hello, stranger! Input your username')
		sock.listen(0)
		Username = ''
		while Username == '':
			data = conn.recv(1024)
			if not data:
				None
			else:
				Username = str(data)
				Username = Username.replace("'", "")
				Username = Username.replace('b', '', 1)
				print(Username)
				users[addr[0]] = Username
				print('entered')
				conn.send(b'Nice to meet you and welcome to server!')
				print(users)
				break
	sock.listen(0)
	msg = ''
	while msg != 'exit':
		msg = ''
		msg = users[addr[0]] + ': '
		data = conn.recv(1024)
		print('Recieved message by ', users[addr[0]])
		if not data:
			break
		msg += data.decode()
		data2 = bytes(msg, encoding = 'utf-8')
		print(msg)
		conn.send(data2)
		print('Message sent to this user!')

	conn.close()
	c += 1
	print('Connection closed')
print('Server closed')
