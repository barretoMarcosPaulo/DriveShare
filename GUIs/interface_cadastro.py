# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DriveShare-cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 440, 131, 17))
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
        self.nomeLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nomeLineEdit.setGeometry(QtCore.QRect(100, 160, 191, 29))
        self.nomeLineEdit.setObjectName("nomeLineEdit")
        self.nomeLabel = QtWidgets.QLabel(Dialog)
        self.nomeLabel.setGeometry(QtCore.QRect(100, 140, 35, 17))
        self.nomeLabel.setObjectName("nomeLabel")
        self.nomeLineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.nomeLineEdit_2.setGeometry(QtCore.QRect(320, 160, 191, 29))
        self.nomeLineEdit_2.setObjectName("nomeLineEdit_2")
        self.nomeLabel_2 = QtWidgets.QLabel(Dialog)
        self.nomeLabel_2.setGeometry(QtCore.QRect(320, 140, 81, 17))
        self.nomeLabel_2.setObjectName("nomeLabel_2")
        self.nomeLineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.nomeLineEdit_3.setGeometry(QtCore.QRect(100, 220, 411, 29))
        self.nomeLineEdit_3.setObjectName("nomeLineEdit_3")
        self.nomeLabel_3 = QtWidgets.QLabel(Dialog)
        self.nomeLabel_3.setGeometry(QtCore.QRect(100, 200, 51, 17))
        self.nomeLabel_3.setObjectName("nomeLabel_3")
        self.nomeLineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.nomeLineEdit_4.setGeometry(QtCore.QRect(100, 280, 191, 29))
        self.nomeLineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.nomeLineEdit_4.setObjectName("nomeLineEdit_4")
        self.nomeLineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.nomeLineEdit_5.setGeometry(QtCore.QRect(320, 280, 191, 29))
        self.nomeLineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.nomeLineEdit_5.setObjectName("nomeLineEdit_5")
        self.nomeLabel_4 = QtWidgets.QLabel(Dialog)
        self.nomeLabel_4.setGeometry(QtCore.QRect(100, 260, 51, 17))
        self.nomeLabel_4.setObjectName("nomeLabel_4")
        self.nomeLabel_5 = QtWidgets.QLabel(Dialog)
        self.nomeLabel_5.setGeometry(QtCore.QRect(320, 260, 91, 17))
        self.nomeLabel_5.setObjectName("nomeLabel_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 340, 88, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 440, 54, 17))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 420, 54, 51))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.funcionalidades()

    def funcionalidades(self):
        self.pushButton_2.clicked.connect(self.cadastrar)

    def cadastrar(self):

        QtWidgets.QMessageBox.about(None, "Cadastro", "Cliente cadastrado com sucesso!",)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "DriveShare"))
        self.label_3.setText(_translate("Dialog", "Crie uma Nova Conta"))
        self.nomeLabel.setText(_translate("Dialog", "Nome"))
        self.nomeLabel_2.setText(_translate("Dialog", "Sobrenome"))
        self.nomeLabel_3.setText(_translate("Dialog", "E-mail"))
        self.nomeLabel_4.setText(_translate("Dialog", "Senha"))
        self.nomeLabel_5.setText(_translate("Dialog", "Repetir Senha"))
        self.pushButton_2.setText(_translate("Dialog", "Cadastrar"))
        # self.label_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/logoShare.png\"/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":logoShare.png\"/></p></body></html>"))
# import imageLogo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())