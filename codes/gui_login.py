# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
class Login_Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Entre em sua conta")
        Dialog.resize(629, 494)
        Dialog.setStyleSheet("")
        self.emailLogin = QtWidgets.QLineEdit(Dialog)
        self.emailLogin.setGeometry(QtCore.QRect(190, 180, 251, 29))
        self.emailLogin.setObjectName("emailLogin")
        self.usuRioLabel = QtWidgets.QLabel(Dialog)
        self.usuRioLabel.setGeometry(QtCore.QRect(190, 160, 51, 20))
        self.usuRioLabel.setObjectName("usuRioLabel")
        self.senhaLabel = QtWidgets.QLabel(Dialog)
        self.senhaLabel.setGeometry(QtCore.QRect(190, 230, 35, 29))
        self.senhaLabel.setObjectName("senhaLabel")
        self.passLogin = QtWidgets.QLineEdit(Dialog)
        self.passLogin.setGeometry(QtCore.QRect(190, 260, 253, 29))
        self.passLogin.setText("")
        self.passLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passLogin.setObjectName("passLogin")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 430, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label.setProperty("icon", icon)
        self.label.setProperty("File", icon)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 80, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.loginRegisterButton = QtWidgets.QPushButton(Dialog)
        self.loginRegisterButton.setGeometry(QtCore.QRect(190, 330, 88, 29))
        self.loginRegisterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginRegisterButton.setObjectName("loginRegisterButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 290, 121, 17))
        self.label_4.setObjectName("label_4")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(360, 330, 88, 29))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setObjectName("loginButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 430, 54, 51))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.usuRioLabel.setText(_translate("Dialog", "E-mail:"))
        self.senhaLabel.setText(_translate("Dialog", "Senha"))
        self.label.setText(_translate("Dialog", "DriveShare"))
        self.label_2.setText(_translate("Dialog", "Acesse sua conta"))
        self.loginRegisterButton.setText(_translate("Dialog", "Cadastre -se"))
        self.label_4.setText(_translate("Dialog", "Esqueci minha senha"))
        self.loginButton.setText(_translate("Dialog", "Entrar"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\"logoShare.png\"/></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Login_Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
