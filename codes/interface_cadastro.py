# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from cadastro import Register
from interface_login import Login_Ui_Dialog

class Register_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 440, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 30, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nameRegister = QtWidgets.QLineEdit(Dialog)
        self.nameRegister.setGeometry(QtCore.QRect(100, 160, 191, 29))
        self.nameRegister.setObjectName("nameRegister")
        self.nomeLabel = QtWidgets.QLabel(Dialog)
        self.nomeLabel.setGeometry(QtCore.QRect(100, 140, 35, 17))
        self.nomeLabel.setObjectName("nomeLabel")
        self.lastNameRegister = QtWidgets.QLineEdit(Dialog)
        self.lastNameRegister.setGeometry(QtCore.QRect(320, 160, 191, 29))
        self.lastNameRegister.setObjectName("lastNameRegister")
        self.nomeLabel_2 = QtWidgets.QLabel(Dialog)
        self.nomeLabel_2.setGeometry(QtCore.QRect(320, 140, 81, 17))
        self.nomeLabel_2.setObjectName("nomeLabel_2")
        self.emailRegister = QtWidgets.QLineEdit(Dialog)
        self.emailRegister.setGeometry(QtCore.QRect(100, 220, 411, 29))
        self.emailRegister.setObjectName("emailRegister")
        self.nomeLabel_3 = QtWidgets.QLabel(Dialog)
        self.nomeLabel_3.setGeometry(QtCore.QRect(100, 200, 51, 17))
        self.nomeLabel_3.setObjectName("nomeLabel_3")
        self.passRegister = QtWidgets.QLineEdit(Dialog)
        self.passRegister.setGeometry(QtCore.QRect(100, 280, 191, 29))
        self.passRegister.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passRegister.setObjectName("passRegister")
        self.passRepeatRegister = QtWidgets.QLineEdit(Dialog)
        self.passRepeatRegister.setGeometry(QtCore.QRect(320, 280, 191, 29))
        self.passRepeatRegister.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passRepeatRegister.setObjectName("passRepeatRegister")
        self.nomeLabel_4 = QtWidgets.QLabel(Dialog)
        self.nomeLabel_4.setGeometry(QtCore.QRect(100, 260, 51, 17))
        self.nomeLabel_4.setObjectName("nomeLabel_4")
        self.nomeLabel_5 = QtWidgets.QLabel(Dialog)
        self.nomeLabel_5.setGeometry(QtCore.QRect(320, 260, 91, 17))
        self.nomeLabel_5.setObjectName("nomeLabel_5")
        self.buttonRegister = QtWidgets.QPushButton(Dialog)
        self.buttonRegister.setGeometry(QtCore.QRect(430, 340, 88, 29))
        self.buttonRegister.setObjectName("buttonRegister")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 440, 54, 17))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 420, 54, 61))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.action_button()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadastre-se"))
        self.label.setText(_translate("Dialog", "DriveShare"))
        self.label_3.setText(_translate("Dialog", "Crie uma Nova Conta"))
        self.nomeLabel.setText(_translate("Dialog", "Nome"))
        self.nomeLabel_2.setText(_translate("Dialog", "Sobrenome"))
        self.nomeLabel_3.setText(_translate("Dialog", "E-mail"))
        self.nomeLabel_4.setText(_translate("Dialog", "Senha"))
        self.nomeLabel_5.setText(_translate("Dialog", "Repetir Senha"))
        self.buttonRegister.setText(_translate("Dialog", "Cadastrar"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\"logoShare.png\"/></p></body></html>"))

    def action_button(self):
        self.buttonRegister.clicked.connect(self.get_data_form)

    def get_data_form(self):
        passwdRepeat = self.passRepeatRegister.text()
        lastname = self.lastNameRegister.text()
        passwd = self.passRegister.text()
        email = self.emailRegister.text()
        name = self.nameRegister.text()

        if name!="" and lastname!="" and email!="" and passwd!="" and passwdRepeat!="":
            if passwd != passwdRepeat:
                QtWidgets.QMessageBox.about(None, "Ooops!", "Suas senhas Nao Conferem.")

            elif not '@' in email and email != None :
                QtWidgets.QMessageBox.about(None, "Ooops!", "Seu E-mail e Invalido.")
            else:
                QtWidgets.QMessageBox.about(None, "Muito Bem!", "Cadastro Realizado Com Sucesso.")

                
                #DialogLogin = QtWidgets.QDialog()
                self.login_screen = Login_Ui_Dialog()
                self.login_screen
                #login_screen.setupUi(DialogLogin)
                #DialogLogin.show()
                

        else:
            QtWidgets.QMessageBox.about(None, "Ooops!", "Preencha Todos Os Campos.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Register_Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
