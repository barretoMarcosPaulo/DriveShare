from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from gui_login import Login_Ui_Dialog
from gui_register import Register_Ui_Dialog

from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()


        self.tela_inicio = Login_Ui_Dialog()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro = Register_Ui_Dialog()
        self.tela_cadastro.setupUi(self.stack1)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.tela_inicio.loginRegisterButton.clicked.connect(self.openLoginScreen)
        self.tela_cadastro.buttonRegister.clicked.connect(self.registerGetDatas)

    def openLoginScreen(self):
        self.QtStack.setCurrentIndex(1)

    def registerGetDatas(self):
        passwdRepeat = self.tela_cadastro.passRepeatRegister.text()
        lastname = self.tela_cadastro.lastNameRegister.text()
        passwd = self.tela_cadastro.passRegister.text()
        email = self.tela_cadastro.emailRegister.text()
        name = self.tela_cadastro.nameRegister.text()
        
        if name!="" and lastname!="" and email!="" and passwd!="" and passwdRepeat!="":
            if passwd != passwdRepeat:
                QtWidgets.QMessageBox.about(None, "Ooops!", "Suas senhas Nao Conferem.")

            elif not '@' in email and email != None :
                QtWidgets.QMessageBox.about(None, "Ooops!", "Seu E-mail e Invalido.")
            else:
                QtWidgets.QMessageBox.about(None, "Muito Bem!", "Cadastro Realizado Com Sucesso.")
                self.QtStack.setCurrentIndex(0)
                

    	

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())