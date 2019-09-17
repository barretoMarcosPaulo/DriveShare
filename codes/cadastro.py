
import pymysql


class Register():
	def __init__(self):
		self.host = 'localhost'
		self.database = 'drive'
		self.user = 'driveshare'
		self.passwd = 'drive@123'
		self.connection = pymysql.connect(host=self.host,db=self.database, user=self.user, passwd=self.passwd)


	def register(self , name , lastname , email , password):
		
		name = name
		lastname = lastname
		email = email
		password = password

		try:
			cursor = self.connection.cursor()
			querySaveUser = "INSERT INTO users(primaryName,lastName,email,passwd) VALUES(%s,%s,%s,%s)"
			
			try:
				cursor.execute(querySaveUser,(name,lastname,email,password))
				self.connection.commit()
				print("OK.")
			except:
				print("Error!!!")
		except:
			print("Connection Error!!!")
