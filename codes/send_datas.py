import socket

class SendDatas():
	def __init__(self):
		self.host = ''
		self.port = 7000
		self.addr=(self.host , self.port)
		self.connection = ''
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	def send_to_server(self):
		mensagem = input('digite uma mensagem para enviar ao servidor: ')
		self.client_socket.connect(self.addr)
		self.client_socket.send(mensagem.encode())
		# print(self.client_socket.recv(1024).decode())
		self.client_socket.close() 	

client = SendDatas()
client.send_to_server()