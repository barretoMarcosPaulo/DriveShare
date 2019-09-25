from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem

from gui_login import Login_Ui_Dialog
from gui_register import Register_Ui_Dialog
from user_home import User_Home_Ui_Dialog

from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot
from mysqlDataBase import RegisterToDataBase 

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.MYSQL_DB = RegisterToDataBase()

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()


        self.tela_login = Login_Ui_Dialog()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Register_Ui_Dialog()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_home = User_Home_Ui_Dialog()
        self.tela_home.setupUi(self.stack2)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.tela_login.loginRegisterButton.clicked.connect(self.openLoginScreen)
        self.tela_cadastro.buttonRegister.clicked.connect(self.registerGetDatas)
        self.tela_login.loginButton.clicked.connect(self.loginUser)
        self.tela_home.SearchButtom.clicked.connect(self.search)

    def openLoginScreen(self):
        self.QtStack.setCurrentIndex(1)

    def registerGetDatas(self):
        passwdRepeat = self.tela_cadastro.passRepeatRegister.text()
        lastname = self.tela_cadastro.lastNameRegister.text()
        passwd = self.tela_cadastro.passRegister.text()
        email = self.tela_cadastro.emailRegister.text()
        name = self.tela_cadastro.nameRegister.text()

        self.MYSQL_DB.save_datas( 

            self.tela_cadastro.nameRegister.text(),
            self.tela_cadastro.lastNameRegister.text(),
            self.tela_cadastro.emailRegister.text(),
            self.tela_cadastro.passRegister.text(),

            )

        self.tela_cadastro.passRepeatRegister.setText("")
        self.tela_cadastro.lastNameRegister.setText("")
        self.tela_cadastro.passRegister.setText("")
        self.tela_cadastro.emailRegister.setText("")
        self.tela_cadastro.nameRegister.setText("")


        
        if name!="" and lastname!="" and email!="" and passwd!="" and passwdRepeat!="":
            if passwd != passwdRepeat:
                QtWidgets.QMessageBox.about(None, "Ooops!", "Suas senhas Nao Conferem.")

            elif not '@' in email and email != None :
                QtWidgets.QMessageBox.about(None, "Ooops!", "Seu E-mail e Invalido.")
            else:
                QtWidgets.QMessageBox.about(None, "Muito Bem!", "Cadastro Realizado Com Sucesso.")

                self.MYSQL_DB.save_datas( 

                    self.tela_cadastro.nameRegister.text(),
                    self.tela_cadastro.lastNameRegister.text(),
                    self.tela_cadastro.emailRegister.text(),
                    self.tela_cadastro.passRegister.text(),

                    )

                self.tela_cadastro.passRepeatRegister.setText("")
                self.tela_cadastro.lastNameRegister.setText("")
                self.tela_cadastro.passRegister.setText("")
                self.tela_cadastro.emailRegister.setText("")
                self.tela_cadastro.nameRegister.setText("")

                self.QtStack.setCurrentIndex(0)
        else:
            QtWidgets.QMessageBox.about(None , "Ooops!" , "Preencha Todos Os Campos.")       

    def loginUser(self):
        user_email = self.tela_login.emailLogin.text()
        user_pass = self.tela_login.passLogin.text()

        if user_email!="" and user_pass!="":
            if not '@' in user_email:
                QtWidgets.QMessageBox.about(None, "Ooops!", "Esse E-mail esta invalido.")
            else:

                if self.MYSQL_DB.isRegistred(user_email,user_pass):
                    self.QtStack.setCurrentIndex(2)
                else:
                    QtWidgets.QMessageBox.about(None, "Ooops!", "E-mail e/ou Senhas Incorretos.")
        else:
            QtWidgets.QMessageBox.about(None, "Ooops!", "Preencha Todos Os Campos.")


    def search(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())