from gui_login import Login_Ui_Dialog
from gui_register import Register_Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot

class DriveShare():
	def __init__(self):
		self.ui_login = Login_Ui_Dialog() 
		self.ui_register = Register_Ui_Dialog()
        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()

        


app = DriveShare()

