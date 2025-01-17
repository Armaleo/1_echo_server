import socket
import logging # Модуль для ведения лог-файла


# =============================================================================
""" Заготовки для лог файла"""
# =============================================================================
Log_Format = "%(levelname)s %(asctime)s - %(message)s" # Формат лог-файла Уровень предупреджения -> Время предупреждения -> Предупреждение

logging.basicConfig(filename = "clientlog.log",    # Название лог файла
                    filemode = "w", # Ставим файл на запись
                    format = Log_Format, # Подставляем формат лога сюда
                    level = logging.DEBUG) # Ставим уровень отображаемых сообщений на минимальный

logger = logging.getLogger() # Инициируем логгер. Все упоминания logger дальше - внесение записей в log файл

sock = socket.socket()
sock.setblocking(1)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname) # Получаем свой айпишник - для дефолтного адреса IP

# =============================================================================

print("Your Computer IP Address is :" + IPAddr)

# =============================================================================
"""

    Ввод IP адреса:
    
    Исключения стоят на:
    - символы кроме точки и цифр
    - на адрес неправильной длины (1.44.2)
    - на числа вне диапозона (от 0 до 255)
    
    Если нажмём Enter с пустой строкой - попробует подключиться на свой IP адрес с портом 9000
    
    Если IP адрес корректный - предложит ввести порт (Диапозон от 1024 до 9999)
    
    Если получится подключиться - пропустит дальше, иначе всё предстоит повторить заново 
    
"""
# =============================================================================


while True:
	addrIP = str(input('Input IP address of echo-server\nor press enter to connect to default IP: '))
	if len(addrIP) == 0:
		try: sock.connect((IPAddr, 9000))
		except ConnectionRefusedError: print("Default address doesn't respond")
		else: break
	correct_check = addrIP.replace('.', '')
	correct_check = correct_check.replace(' ', '')
	for i in range(10): correct_check = correct_check.replace(str(i), '')
	if len(correct_check) != 0: print('There are excess symbols in your address, IP can contain only dots and digits')
	else:
		format = addrIP.split('.')
		if len(format) != 4: print('There are not 3 dots in your ip address')
		else:
			for i in range(4):
				if int(format[i]) > 255 or int(format[i]) < 0: 
					print('Incorrect IP address, nubers must be in between 0 and 255')
					break
			else:
				try:
					portNum = int(input('Input the port Number: '))
				except:
					print('Incorrect symbols, port number can contain only 4 digits')
				else:
					if portNum < 9999 and portNum > 1024:
						try: sock.connect((addrIP, portNum))
						except ConnectionRefusedError:	print('There in no server with that address and port')
						else: break
					else: print('incorrect diapozone')
                    
# =============================================================================


logger.info('connected to server')


print('Succsessfully connected! Press Enter to continue') # Всё подключено - отправляем серверу пустое сообщение чтобы он нас признал
msg = ''
a = 0

# =============================================================================
""" Обмен сообщениями с сервером """
# =============================================================================
while msg!= 'exit': # Если мы напишем exit - соединение будет прервано

	msg = input()
# 	print()
	sock.send(msg.encode()) # Сообщение которое мы отправим кодируется в байтовый формат
    
	if a != 0:logger.info('Message succsessfully sended') # Костыль, чтобы служебное сообщение об отправление (простите за тавтологию) сообщения не выводилось на первое пустое сообщение
	else: a = 1 
    
    
	data = sock.recv(1024) # Сообщение которое примем будет иметь размер 1 байт
    
	logger.info('You recieved a message!')
    
	print(data.decode()) # Выводим декодированное сообщение сервера
# 	print()


logger.info('connection closed')
sock.close() # Закрываем сокет
# =============================================================================