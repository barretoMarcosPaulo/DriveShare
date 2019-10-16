from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem

from send_datas import ClientSide

from gui_login import Login_Ui_Dialog
from gui_register import Register_Ui_Dialog
from home import Ui_UserFilesScreen
from upload import Ui_Upload
from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot


class Ui_Main(QtWidgets.QWidget): 
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.connection = ClientSide()

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()


        self.tela_login = Login_Ui_Dialog()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Register_Ui_Dialog()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_home = Ui_UserFilesScreen()
        self.tela_home.setupUi(self.stack2)

        self.tela_upload = Ui_Upload()
        self.tela_upload.setupUi(self.stack3)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.tela_login.loginRegisterButton.clicked.connect(self.openLoginScreen)
        self.tela_cadastro.buttonRegister.clicked.connect(self.registerGetDatas)
        self.tela_login.loginButton.clicked.connect(self.loginUser)
        self.tela_home.SearchButtom.clicked.connect(self.search)
        self.tela_home.uploadButton.clicked.connect(self.openUploadScreen)
        self.tela_upload.buttonCancelar.clicked.connect(self.backHomePage)

    def openLoginScreen(self):
        self.QtStack.setCurrentIndex(1)
    
    def backHomePage(self):
        self.QtStack.setCurrentIndex(2)
    
    def openUploadScreen(self):
        self.QtStack.setCurrentIndex(3)
    
    def registerGetDatas(self):
        datas_form_register = "register,"

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
                datas_form_register += name+","+lastname+","+email+","+passwd 
                if self.connection.sendDatas(datas_form_register):
                    QtWidgets.QMessageBox.about(None, "Muito Bem!", "Cadastro Realizado.")
                    self.tela_cadastro.passRepeatRegister.setText("")
                    self.tela_cadastro.lastNameRegister.setText("")
                    self.tela_cadastro.passRegister.setText("")
                    self.tela_cadastro.emailRegister.setText("")
                    self.tela_cadastro.nameRegister.setText("")
                    self.QtStack.setCurrentIndex(0)
                else:
                    QtWidgets.QMessageBox.about(None, "Ooops!", "E-mail ja cadastrado.")
                  
        else:
            QtWidgets.QMessageBox.about(None , "Ooops!" , "Preencha Todos Os Campos.")       

    def loginUser(self):
        user_email = self.tela_login.emailLogin.text()
        user_pass = self.tela_login.passLogin.text()
        
        datas_form_login = "login,"
        
        if user_email!="" and user_pass!="":
            if not '@' in user_email:
                QtWidgets.QMessageBox.about(None, "Ooops!", "Esse E-mail esta invalido.")
            else:
                datas_form_login+=user_email+","+user_pass
                if self.connection.sendDatas(datas_form_login):
                    self.QtStack.setCurrentIndex(2)
                else:
                    QtWidgets.QMessageBox.about(None, "Ooops!", "e-mail e/oi usuario incorretos!")

        else:
            QtWidgets.QMessageBox.about(None, "Ooops!", "Preencha Todos Os Campos.")


    def search(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())