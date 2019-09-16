# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from cadastro import User , Register

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

MYSQL = Register()

class Ui_Dialog_Cadastro(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 440, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 30, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.nomeLineEdit = QtGui.QLineEdit(Dialog)
        self.nomeLineEdit.setGeometry(QtCore.QRect(100, 160, 191, 29))
        self.nomeLineEdit.setObjectName(_fromUtf8("nomeLineEdit"))
        self.nomeLabel = QtGui.QLabel(Dialog)
        self.nomeLabel.setGeometry(QtCore.QRect(100, 140, 35, 17))
        self.nomeLabel.setObjectName(_fromUtf8("nomeLabel"))
        self.nomeLineEdit_2 = QtGui.QLineEdit(Dialog)
        self.nomeLineEdit_2.setGeometry(QtCore.QRect(320, 160, 191, 29))
        self.nomeLineEdit_2.setObjectName(_fromUtf8("nomeLineEdit_2"))
        self.nomeLabel_2 = QtGui.QLabel(Dialog)
        self.nomeLabel_2.setGeometry(QtCore.QRect(320, 140, 81, 17))
        self.nomeLabel_2.setObjectName(_fromUtf8("nomeLabel_2"))
        self.nomeLineEdit_3 = QtGui.QLineEdit(Dialog)
        self.nomeLineEdit_3.setGeometry(QtCore.QRect(100, 220, 411, 29))
        self.nomeLineEdit_3.setObjectName(_fromUtf8("nomeLineEdit_3"))
        self.nomeLabel_3 = QtGui.QLabel(Dialog)
        self.nomeLabel_3.setGeometry(QtCore.QRect(100, 200, 51, 17))
        self.nomeLabel_3.setObjectName(_fromUtf8("nomeLabel_3"))
        self.nomeLineEdit_4 = QtGui.QLineEdit(Dialog)
        self.nomeLineEdit_4.setGeometry(QtCore.QRect(100, 280, 191, 29))
        self.nomeLineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.nomeLineEdit_4.setObjectName(_fromUtf8("nomeLineEdit_4"))
        self.nomeLineEdit_5 = QtGui.QLineEdit(Dialog)
        self.nomeLineEdit_5.setGeometry(QtCore.QRect(320, 280, 191, 29))
        self.nomeLineEdit_5.setEchoMode(QtGui.QLineEdit.Password)
        self.nomeLineEdit_5.setObjectName(_fromUtf8("nomeLineEdit_5"))
        self.nomeLabel_4 = QtGui.QLabel(Dialog)
        self.nomeLabel_4.setGeometry(QtCore.QRect(100, 260, 51, 17))
        self.nomeLabel_4.setObjectName(_fromUtf8("nomeLabel_4"))
        self.nomeLabel_5 = QtGui.QLabel(Dialog)
        self.nomeLabel_5.setGeometry(QtCore.QRect(320, 260, 91, 17))
        self.nomeLabel_5.setObjectName(_fromUtf8("nomeLabel_5"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 340, 88, 29))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 440, 54, 17))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 420, 54, 51))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        if self.pushButton_2.isChecked():
            print("2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        self.funcionalidades()

    def funcionalidades(self):
        self.pushButton_2.clicked.connect(self.get_data)

    def get_data(self):
        w = QWidget()

        name        = self.nomeLineEdit.text()
        lastname    = self.nomeLineEdit_2.text()
        email       = self.nomeLineEdit_3.text()
        password    = self.nomeLineEdit_4.text()
        repeat_pass = self.nomeLineEdit_5.text()

        if name!="" and lastname!="" and email!="" and password!="" and repeat_pass!="":
            if password != repeat_pass:
                QMessageBox.information(w, "Ooops!", "As Senhas Fornecidas Estao Erradas.")
           
            elif not '@' in email and email != None :
                QMessageBox.information(w, "Ooops!", "Digite um email valido.")
            else:
                
                # userRegistrer = User(self.nomeLineEdit.text() , self.nomeLineEdit_2.text() , self.nomeLineEdit_3.text() , self.nomeLineEdit_4.text())
                MYSQL.register(str(name) , str(lastname) , str(email) , str(password))
                QMessageBox.information(w, "Cadastro Realizado!", "Muito Bem, seu cadastro foi realizado.")
        else:    
            QMessageBox.information(w, "Ooops!", "Por Favor, Preencha Todos Os Campos.")




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Criar Uma Nova Conta", None))
        self.label.setText(_translate("Dialog", "DriveShare", None))
        self.label_3.setText(_translate("Dialog", "Crie uma Nova Conta", None))
        self.nomeLabel.setText(_translate("Dialog", "Nome", None))
        self.nomeLabel_2.setText(_translate("Dialog", "Sobrenome", None))
        self.nomeLabel_3.setText(_translate("Dialog", "E-mail", None))
        self.nomeLabel_4.setText(_translate("Dialog", "Senha", None))
        self.nomeLabel_5.setText(_translate("Dialog", "Repetir Senha", None))
        self.pushButton_2.setText(_translate("Dialog", "Cadastrar", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":logoShare.png\"/></p></body></html>", None))


# import imageLogo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog_Cadastro()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
