# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Upload(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 480)
        Form.setFixedSize(731, 480)
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
        self.buttonUpload.setGeometry(QtCore.QRect(310, 170, 171, 41))
        self.buttonUpload.setObjectName("buttonUpload")
        self.buttonEnviar = QtWidgets.QPushButton(Form)
        self.buttonEnviar.setGeometry(QtCore.QRect(550, 430, 87, 29))
        self.buttonEnviar.setObjectName("buttonEnviar")
        self.buttonCancelar = QtWidgets.QPushButton(Form)
        self.buttonCancelar.setGeometry(QtCore.QRect(100, 430, 87, 29))
        self.buttonCancelar.setObjectName("buttonCancelar")
        self.label_file = QtWidgets.QLabel(Form)
        self.label_file.setGeometry(QtCore.QRect(300, 330, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_file.setFont(font)
        self.label_file.setObjectName("label_file")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 180, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 250, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(310, 240, 171, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(5, "")
        self.label_file_2 = QtWidgets.QLabel(Form)
        self.label_file_2.setGeometry(QtCore.QRect(200, 330, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_file_2.setFont(font)
        self.label_file_2.setObjectName("label_file_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "DriveShare | Upload de Arquivos"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><img src=\"logoShare.png\"/></p></body></html>"))
        self.buttonUpload.setText(_translate("Form", "Arquivo"))
        self.buttonEnviar.setText(_translate("Form", "Enviar"))
        self.buttonCancelar.setText(_translate("Form", "Cancelar"))
        self.label_file.setText(_translate("Form", "Nenhum Arquivo Selecionado"))
        self.label_3.setText(_translate("Form", "Escolha um arquivo"))
        self.label_4.setText(_translate("Form", "Destino do Arquivo"))
        self.comboBox.setItemText(0, _translate("Form", "documentos"))
        self.comboBox.setItemText(1, _translate("Form", "imagens"))
        self.comboBox.setItemText(2, _translate("Form", "musicas"))
        self.comboBox.setItemText(3, _translate("Form", "videos"))
        self.comboBox.setItemText(4, _translate("Form", "outros"))
        self.label_file_2.setText(_translate("Form", "Arquivo:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
