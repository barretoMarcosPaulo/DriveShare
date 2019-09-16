
class User():
	def __init__(self ,name , lastname,email,password):
		self.name = name
		self.lastname = lastname
		self.email = email
		self.password = password

	def get_name(self):
		return self.name

	def get_lastname(self):
		return self.lastname
	
	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

	def set_name(self , name):
		self.name = name

	def set_lastname(self , lastname):
		self.lastname = lastname

	def set_email(self , email):
		self.email = email

	def set_password(self , password):
		self.password = password

	name = property(get_name , set_name)
	lastname = property(get_lastname , set_lastname)
	email = property(get_email , set_email)
	password = property(get_password , set_password)

class Register():
	def __init__(self):
		self.clients = []

	def get_clientes(self):
		for client in self.clients:
			print(client)

	def register(self , client):
		self.clients.append(client)

