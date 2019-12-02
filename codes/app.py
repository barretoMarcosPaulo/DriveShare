from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem,QFileDialog

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
from userlogado import *
import time
from functools import partial


class Ui_Main(QtWidgets.QWidget): 
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.connection = ClientSide()
        self.path = " "
        self.download_destination = " "
        self.file_size = str()
        self.usuario = UserLogado()
        self.download_in_progress = False
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
        self.tela_home.uploadButton.clicked.connect(self.openUploadScreen)
        self.tela_upload.buttonCancelar.clicked.connect(self.backHomePage)
        self.tela_upload.buttonUpload.clicked.connect(self.selectFile)
        self.tela_upload.buttonEnviar.clicked.connect(self.sendFile)
        
        self.tela_home.tableWidget.cellClicked.connect(      partial(self.selectFileDownload , self.tela_home.tableWidget, self.tela_home.escolher_destino))
        self.tela_home.tableWidget_2.cellClicked.connect(    partial(self.selectFileDownload , self.tela_home.tableWidget_2, self.tela_home.escolher_destino_2))
        self.tela_home.tableWidget_3.cellClicked.connect(    partial(self.selectFileDownload , self.tela_home.tableWidget_3, self.tela_home.escolher_destino_3))
        self.tela_home.tableWidget_4.cellClicked.connect(    partial(self.selectFileDownload ,self.tela_home.tableWidget_4, self.tela_home.escolher_destino_4))
        self.tela_home.tableWidget_5.cellClicked.connect(    partial(self.selectFileDownload , self.tela_home.tableWidget_5, self.tela_home.escolher_destino_5))
        self.tela_home.tableWidget_6.cellClicked.connect(    partial(self.selectFileDownload , self.tela_home.tableWidget_6, self.tela_home.escolher_destino_6))
        self.tela_home.tableWidget_7.cellClicked.connect(    partial(self.selectFileDownload , self.tela_home.tableWidget_7, self.tela_home.escolher_destino_7))
        
        # self.tela_home.salvar_arquivo.clicked.connect(self.get_destination_download)
        

        self.tela_home.cancelar.clicked.connect(  partial(self.cancel_download ,self.tela_home.tableWidget , self.tela_home.escolher_destino))
        self.tela_home.cancelar_2.clicked.connect(partial(self.cancel_download ,self.tela_home.tableWidget_2 , self.tela_home.escolher_destino_2))
        self.tela_home.cancelar_3.clicked.connect(partial(self.cancel_download ,self.tela_home.tableWidget_3 , self.tela_home.escolher_destino_3))
        self.tela_home.cancelar_5.clicked.connect(partial(self.cancel_download ,self.tela_home.tableWidget_4 , self.tela_home.escolher_destino_4))
        self.tela_home.cancelar_6.clicked.connect(partial(self.cancel_download ,self.tela_home.tableWidget_5 , self.tela_home.escolher_destino_5))
        self.tela_home.cancelar_7.clicked.connect(partial(self.cancel_download ,self.tela_home.tableWidget_6 , self.tela_home.escolher_destino_6))
        self.tela_home.cancelar_8.clicked.connect(partial(self.cancel_download ,self.tela_home.tableWidget_7 , self.tela_home.escolher_destino_7))


    def cancel_download(self,tabela,janela):
        tabela.show()
        janela.hide()

    def selectFileDownload(self,tabela,janela):

        row = tabela.currentRow()
        col = tabela.currentColumn()
        remote_file = str()

        if col == 4:

            janela.show()
            tabela.hide()

            # if not self.download_in_progress:
                                
            #     file = tabela.item(row, 0).text()
            #     path = tabela.item(row, 1).text()
                
            #     QtWidgets.QMessageBox.about(None, "Ok!", "Download do arquivo {} iniciado, aguarde ate o final.".format(file))
    
            #     remote_file+=self.usuario.email+"/"+path+"/"+file
            #     remote_file = remote_file.replace(" ","")

            #     request = "download,"+remote_file

            #     self.connection.request_download(request,file)

            #     self.download_in_progress = False
                
            # else:
            #      QtWidgets.QMessageBox.about(None, "Calma!", "Aguarde o termino do download atual.")



    def selectFile(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.file_size = str(os.path.getsize(filename[0]))
        name = self.path.split("/")
        name = name[len(name)-1]
        self.tela_upload.label_file.setText(name)
    
    def sendFile(self):
        name = self.path.split("/")
        name = name[len(name)-1]
        send = "upload,"+name+","+self.usuario.email+","+self.usuario.id+","+str(self.tela_upload.comboBox.currentText()+","+self.file_size )
        send = send.replace(" ", "")
        if self.connection.sendDatas(send):
            self.connection.sendFile(self.path) 
        QtWidgets.QMessageBox.about(None, "Ok!", "Upload Finalizado")
        self.homePageUser()
            

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
                    # self.tela_cadastro.lastNbuttonEnviarbuttonEnviarameRegister.setText("")
                    self.tela_cadastro.passRegister.setText("")
                    self.tela_cadastro.emailRegister.setText("")
                    self.tela_cadastro.nameRegister.setText("")
                    self.QtStack.setCurrentIndex(0)
                else:
                    QtWidgets.QMessageBox.about(None, "Ooops!", "E-mail ja cadastrado.")
                  
        else:
            QtWidgets.QMessageBox.about(None , "Ooops!" , "Preencha Todos Os Campos.")       


    def load_infos(self):
        recentes = []
        documentos = []
        imagens = []
        videos = []
        musicas = []
        outros = []
        compart = []

        recentes = self.connection.request_files(self.usuario.id,"recentes")
        documentos = self.connection.request_files(self.usuario.id,"documentos")
        imagens = self.connection.request_files(self.usuario.id,"imagens")
        videos = self.connection.request_files(self.usuario.id,"videos")
        musicas = self.connection.request_files(self.usuario.id,"musicas")
        outros = self.connection.request_files(self.usuario.id,"outros")
        compart = self.connection.request_files(self.usuario.id,"compartilhados")

   
        self.tela_home.loadData(recentes,self.tela_home.tableWidget)
        self.tela_home.loadData(documentos,self.tela_home.tableWidget_2)
        self.tela_home.loadData(imagens,self.tela_home.tableWidget_3)
        self.tela_home.loadData(videos,self.tela_home.tableWidget_4)
        self.tela_home.loadData(musicas,self.tela_home.tableWidget_5)
        self.tela_home.loadData(compart,self.tela_home.tableWidget_6)
        self.tela_home.loadData(outros,self.tela_home.tableWidget_7)

    def homePageUser(self):
        self.QtStack.setCurrentIndex(2)
        self.tela_home.label.setText(self.usuario.primaryName)
        self.load_infos()

    def loginUser(self):
        user_email = self.tela_login.emailLogin.text()
        user_pass = self.tela_login.passLogin.text()

        datas_form_login = "login,"
        if user_email!="" and user_pass!="":
            if not '@' in user_email:
                QtWidgets.QMessageBox.about(None, "Ooops!", "Esse E-mail esta invalido.")
            else:
                datas_form_login+=user_email+","+user_pass
                
                status,response = self.connection.sendDatas(datas_form_login)

                if status:
                    self.usuario.id = response[0]
                    self.usuario.primaryName = response[1]
                    self.usuario.lastName = response[2]
                    self.usuario.email = response[3]                    
                    self.homePageUser()
                    

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