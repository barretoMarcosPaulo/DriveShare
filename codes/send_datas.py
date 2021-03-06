import socket 
import time
from datetime import datetime

class ClientSide():
	def __init__(self):
		# self.host = '168.235.110.16'
		self.host = 'localhost'
		self.port = 8000
		self.address=((self.host,self.port))
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.connect()

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
				time.sleep(2)
				self.client_socket.connect(self.address)
				connected = True
				break
			except:
				connection_attempt+=1
		return connected


	def sendDatas(self,content):
				
		self.client_socket.send(content.encode()) 
		# Return error/success and message
		
		resposta = self.client_socket.recv(1024).decode()
		
		if resposta == "error":
			return False
		if resposta == "ok":
			return True
		else:
			# resposta = resposta.split(",")
			resposta = resposta.replace("[","")
			resposta = resposta.replace("]","")
			resposta = resposta.replace("','","")
			resposta = resposta.replace("'","")
			resposta=resposta.split(",")
			return resposta

	def request_download(self,path,name,destination):



		self.client_socket.send(path.encode())
		destination +="/"+name
		print("destination", destination)

		f = open(destination,'wb')

                                                    
		while True:
			l = self.client_socket.recv(1024)
            
			while "done" not in str(l):
				print(l)
				print("Download")
				f.write(l)
				
				l = self.client_socket.recv(1024)

			f.close()
			print("Concluido")
			break
	
	def sendFile(self, path):

		fileName = path
		f = open(fileName,'rb')
		print('Sending...')

		self.client_socket.send(fileName.encode())

		l = f.read(1024)
		while (l):
		    print('Sending...')
		    self.client_socket.send(l)
		    l = f.read(1024)
		f.close()
		time.sleep(3)
		self.client_socket.send("done".encode())
		print("Done Sending")


	def request_files(self,user_id,type_file):
		request = "get_files,"+type_file+","+user_id
		self.client_socket.send(request.encode())
		files = self.client_socket.recv(1024).decode()
		files = files.split(";")

		files.pop(0)

		nova_lista = []

		for i in range(len(files)):
			files[i] = files[i].replace("]","")
			files[i] = files[i].replace("'","")
			nova_lista.append(files[i].split(","))



		for x in range( len(nova_lista)):
			nova_lista[x].pop(0)


		return nova_lista

	def request_comp(self, user_id):
		send = "files_comp,"+user_id

		self.client_socket.send(send.encode())
		files = self.client_socket.recv(1024).decode()

		lista = files.split(";")
		
		return lista	
	

	def closeConnection(self):
		self.client_socket.close()

# teste = ClientSide()

# a = datetime.now()
# while True:
# 	teste.sendDatas(str(a))
# teste.closeConnection()