from gui_login import Login_Ui_Dialog
from gui_register import Register_Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class DriveShare():
	def __init__(self):
		self.ui_login = Login_Ui_Dialog() 
		# self.ui_register = Register_Ui_Dialog()

	def show_login(self):
		app = QtWidgets.QApplication(sys.argv)
		Dialog = QtWidgets.QDialog()
		self.ui_login.setupUi(Dialog)
		Dialog.show()
		sys.exit(app.exec_())

	# def show_register(self): 
	# 	app = QtWidgets.QApplication(sys.argv)
	# 	Dialog = QtWidgets.QDialog()
	# 	self.ui_register.setupUi(Dialog)
	# 	Dialog.show()
	# 	sys.exit(app.exec_())

app = DriveShare()
app.show_login()
