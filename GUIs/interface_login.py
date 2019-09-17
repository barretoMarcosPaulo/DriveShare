# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DriveShare-Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 494)
        Dialog.setStyleSheet("")
        self.usuRioLineEdit = QtWidgets.QLineEdit(Dialog)
        self.usuRioLineEdit.setGeometry(QtCore.QRect(190, 180, 251, 29))
        self.usuRioLineEdit.setObjectName("usuRioLineEdit")
        self.usuRioLabel = QtWidgets.QLabel(Dialog)
        self.usuRioLabel.setGeometry(QtCore.QRect(190, 160, 51, 20))
        self.usuRioLabel.setObjectName("usuRioLabel")
        self.senhaLabel = QtWidgets.QLabel(Dialog)
        self.senhaLabel.setGeometry(QtCore.QRect(190, 230, 35, 29))
        self.senhaLabel.setObjectName("senhaLabel")
        self.senhaLineEdit = QtWidgets.QLineEdit(Dialog)
        self.senhaLineEdit.setGeometry(QtCore.QRect(190, 260, 253, 29))
        self.senhaLineEdit.setText("")
        self.senhaLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senhaLineEdit.setObjectName("senhaLineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 430, 251, 51))
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
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 330, 88, 29))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 290, 121, 17))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 330, 88, 29))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.pushButton.setText(_translate("Dialog", "Cadastre -se"))
        self.label_4.setText(_translate("Dialog", "Esqueci minha senha"))
        self.pushButton_2.setText(_translate("Dialog", "Entrar"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/logoShare/logoShare.png\"/></p></body></html>"))
# import imageLogo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
