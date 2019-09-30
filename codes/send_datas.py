import socket 
import time
class ClientSide():
	def __init__(self):
		self.host = 'localhost'
		self.port = 3000
		self.address=((self.host,self.port))
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	def connect(self):
		connected = True
		try:
			self.client_socket.connect(self.address)
		except:
			connected = self.reestablish_connection()
		return connected


	def reestablish_connection(self):
		connection_attempt = 0
		connected = False
		while(connection_attempt<5):
			try:
				print("try connection...")
				time.sleep(5)
				self.client_socket.connect(self.address)
				connected = True
				break
			except:
				connection_attempt+=1
		return connected


	def sendDatas(self,content):
		
		self.connect()
			
		self.client_socket.send(content.encode()) 
		print(self.client_socket.recv(1024).decode())

	def closeConnection(self):
		self.client_socket.close()


Connection = ClientSide()

Connection.sendDatas("MArcos")


# import socket
# ip = input('digite o ip de conexao: ')
# port = 7000
# addr = ((ip,port)) #define a tupla de endereco
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
# client_socket.connect(addr) #realiza a conexao
# while(True):
#     mensagem = input('digite uma mensagem para enviar ao servidor: ')
#     client_socket.send(mensagem.encode()) #envia mensagem
#     print(client_socket.recv(1024).decode())

# client_socket.close() #fecha conexao 