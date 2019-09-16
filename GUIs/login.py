
from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(629, 494)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.usuRioLineEdit = QtGui.QLineEdit(Dialog)
        self.usuRioLineEdit.setGeometry(QtCore.QRect(190, 180, 251, 29))
        self.usuRioLineEdit.setObjectName(_fromUtf8("usuRioLineEdit"))
        self.usuRioLabel = QtGui.QLabel(Dialog)
        self.usuRioLabel.setGeometry(QtCore.QRect(190, 160, 51, 20))
        self.usuRioLabel.setObjectName(_fromUtf8("usuRioLabel"))
        self.senhaLabel = QtGui.QLabel(Dialog)
        self.senhaLabel.setGeometry(QtCore.QRect(190, 230, 35, 29))
        self.senhaLabel.setObjectName(_fromUtf8("senhaLabel"))
        self.senhaLineEdit = QtGui.QLineEdit(Dialog)
        self.senhaLineEdit.setGeometry(QtCore.QRect(190, 260, 253, 29))
        self.senhaLineEdit.setText(_fromUtf8(""))
        self.senhaLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.senhaLineEdit.setObjectName(_fromUtf8("senhaLineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 430, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label.setProperty("icon", icon)
        self.label.setProperty("File", icon)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 80, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 330, 88, 29))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 290, 121, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 330, 88, 29))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 430, 54, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.usuRioLabel.setText(_translate("Dialog", "E-mail:", None))
        self.senhaLabel.setText(_translate("Dialog", "Senha", None))
        self.label.setText(_translate("Dialog", "DriveShare", None))
        self.label_2.setText(_translate("Dialog", "Acesse sua conta", None))
        self.pushButton.setText(_translate("Dialog", "Cadastre -se", None))
        self.label_4.setText(_translate("Dialog", "Esqueci minha senha", None))
        self.pushButton_2.setText(_translate("Dialog", "Entrar", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/logoShare/logoShare.png\"/></p></body></html>", None))

import imageLogo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

