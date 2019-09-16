
import pymysql

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
		self.host = 'localhost'
		self.database = 'drive'
		self.user = 'driveshare'
		self.passwd = 'drive@123'


	def register(self , name , lastname , email , password):
		
		name = name
		lastname = lastname
		email = email
		password = password

		try:
			connection = pymysql.connect(host=self.host,db=self.database, user=self.user, passwd=self.passwd)
			cursor = connection.cursor()
			querySaveUser = "INSERT INTO users(primaryName,lastName,email,passwd) VALUES(%s,%s,%s,%s)"
			
			try:
				cursor.execute(querySaveUser,(name,lastname,email,password))
				connection.commit()
				print("OK.")
			except:
				print("Error!!!")
		except:
			print("Connection Error!!!")
