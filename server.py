import socket
import logging
import datetime as dt

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format,
                    level = logging.DEBUG)

logger = logging.getLogger()

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

a = "Your Computer Name is:"+hostname
logger.info(a)
a = "Your Computer IP Address is:"+IPAddr
logger.info(a)
logger.info('server started')
greet = 'Hello '
sock = socket.socket()
portNum = 9000
while True:

	try: sock.bind(('', portNum))
	except:	portNum += 1
	else: break
a = 'The port number is ' + str(portNum)
logger.info(a)
a = ('Server is opened on port: ', portNum)
logger.info(a)
c = 0
users = {'key':'info'}
print(list(users.keys()))
while c<5:
	logger.info('Looking for connection...')
	sock.listen()
	conn, addr = sock.accept()
	print(addr[0])
	curr = list(users.keys())
	logger.info("Connected by ", addr)
	for i in range(len(curr)):
		if str(curr[i]) == str(addr[0]):
			greet1 = greet + users[addr[0]] + '!'
			conn.send(bytes(greet1, encoding = 'utf-8'))
			break
	else:
		logger.info('nickname requested')
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
				logger.info('User entered nickname')
				conn.send(b'Nice to meet you and welcome to server!')
				print(users)
				break
	sock.listen(0)
	msg = ''
	while msg != 'exit':
		msg = ''
		msg = users[addr[0]] + ': '
		data = conn.recv(1024)
		uzver = str('Recieved message by ' + users[addr[0]])
		logger.info(uzver)
		if not data:
			break
		msg += data.decode()
		data2 = bytes(msg, encoding = 'utf-8')
		print(msg)
		conn.send(data2)
		logger.info('Message sent to this user!')

	conn.close()
	c += 1
	logger.info('Connection closed')
logger.info('Server closed')
