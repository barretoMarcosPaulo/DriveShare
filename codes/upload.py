# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QFileDialog
import socket 
import os
import pickle

class Ui_Upload(object):
    def setupUi(self, Form):


        Form.setObjectName("Form")
        Form.resize(731, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 54, 51))
        self.label_2.setObjectName("label_2")
        self.buttonUpload = QtWidgets.QPushButton(Form)
        self.buttonUpload.setGeometry(QtCore.QRect(240, 190, 241, 61))
        self.buttonUpload.setObjectName("buttonUpload")
        self.buttonEnviar = QtWidgets.QPushButton(Form)
        self.buttonEnviar.setGeometry(QtCore.QRect(550, 430, 87, 29))
        self.buttonEnviar.setObjectName("buttonEnviar")
        self.buttonCancelar = QtWidgets.QPushButton(Form)
        self.buttonCancelar.setGeometry(QtCore.QRect(100, 430, 87, 29))
        self.buttonCancelar.setObjectName("buttonCancelar")
        self.label_file = QtWidgets.QLabel(Form)
        self.label_file.setGeometry(QtCore.QRect(280, 260, 400, 17))
        self.label_file.setObjectName("label_file")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "DriveShare | Upload de Arquivos"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><img src=\"logoShare.png\"/></p></body></html>"))
        self.buttonUpload.setText(_translate("Form", "Escolher Arquivo do Computador"))
        self.buttonEnviar.setText(_translate("Form", "Enviar"))
        self.buttonCancelar.setText(_translate("Form", "Cancelar"))
        self.label_file.setText(_translate("Form", "Nenhum Arquivo Selecionado"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Upload()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
