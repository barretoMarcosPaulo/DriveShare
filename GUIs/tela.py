# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_pastas.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserFilesScreen(object):
    def setupUi(self, UserFilesScreen):
        UserFilesScreen.setObjectName("UserFilesScreen")
        UserFilesScreen.setWindowModality(QtCore.Qt.NonModal)
        UserFilesScreen.resize(916, 615)
        UserFilesScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        UserFilesScreen.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(UserFilesScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(820, 90, 81, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 255, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 255, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 255, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.uploadButton.setPalette(palette)
        self.uploadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uploadButton.setStyleSheet("selection-background-color: rgb(110, 255, 188);")
        self.uploadButton.setObjectName("uploadButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-5, 10, 21, 431))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 54, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.version_app = QtWidgets.QLabel(self.centralwidget)
        self.version_app.setGeometry(QtCore.QRect(830, 570, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.version_app.setFont(font)
        self.version_app.setObjectName("version_app")
        self.foto_perfil = QtWidgets.QLabel(self.centralwidget)
        self.foto_perfil.setGeometry(QtCore.QRect(820, 10, 54, 41))
        self.foto_perfil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.foto_perfil.setText("")
        self.foto_perfil.setPixmap(QtGui.QPixmap("imagesQT/person.png"))
        self.foto_perfil.setObjectName("foto_perfil")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(800, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 100, 871, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabela_recentes = QtWidgets.QTreeWidget(self.tab)
        self.tabela_recentes.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tabela_recentes.setObjectName("tabela_recentes")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_recentes.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_recentes.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_recentes.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_recentes.headerItem().setFont(3, font)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabela_documentos = QtWidgets.QTreeWidget(self.tab_2)
        self.tabela_documentos.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tabela_documentos.setObjectName("tabela_documentos")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_documentos.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_documentos.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_documentos.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_documentos.headerItem().setFont(3, font)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabela_imagens = QtWidgets.QTreeWidget(self.tab_3)
        self.tabela_imagens.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tabela_imagens.setObjectName("tabela_imagens")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_imagens.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_imagens.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_imagens.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_imagens.headerItem().setFont(3, font)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabela_videos = QtWidgets.QTreeWidget(self.tab_4)
        self.tabela_videos.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tabela_videos.setObjectName("tabela_videos")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_videos.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_videos.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_videos.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_videos.headerItem().setFont(3, font)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabela_musicas = QtWidgets.QTreeWidget(self.tab_5)
        self.tabela_musicas.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tabela_musicas.setObjectName("tabela_musicas")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_musicas.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_musicas.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_musicas.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_musicas.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_musicas.headerItem().setFont(4, font)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabela_compartilhados = QtWidgets.QTreeWidget(self.tab_7)
        self.tabela_compartilhados.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tabela_compartilhados.setObjectName("tabela_compartilhados")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_compartilhados.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_compartilhados.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_compartilhados.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_compartilhados.headerItem().setFont(3, font)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabela_outros = QtWidgets.QTreeWidget(self.tab_6)
        self.tabela_outros.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tabela_outros.setStyleSheet("")
        self.tabela_outros.setObjectName("tabela_outros")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_outros.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_outros.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_outros.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabela_outros.headerItem().setFont(3, font)
        self.tabWidget.addTab(self.tab_6, "")
        UserFilesScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UserFilesScreen)
        self.statusbar.setObjectName("statusbar")
        UserFilesScreen.setStatusBar(self.statusbar)

        self.retranslateUi(UserFilesScreen)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(UserFilesScreen)

    def retranslateUi(self, UserFilesScreen):
        _translate = QtCore.QCoreApplication.translate
        UserFilesScreen.setWindowTitle(_translate("UserFilesScreen", "MainWindow"))
        self.uploadButton.setText(_translate("UserFilesScreen", "Upload"))
        self.label_2.setText(_translate("UserFilesScreen", "<html><head/><body><p><img src=\"logoShare.png\"/></p></body></html>"))
        self.label_3.setText(_translate("UserFilesScreen", "DriveShare"))
        self.version_app.setText(_translate("UserFilesScreen", "Versão 1.0"))
        self.label.setText(_translate("UserFilesScreen", "Marcos Paulo"))
        self.tabela_recentes.headerItem().setText(0, _translate("UserFilesScreen", "Arquivo"))
        self.tabela_recentes.headerItem().setText(1, _translate("UserFilesScreen", "Tamanho(MB)"))
        self.tabela_recentes.headerItem().setText(2, _translate("UserFilesScreen", "Diretório"))
        self.tabela_recentes.headerItem().setText(3, _translate("UserFilesScreen", "Data "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("UserFilesScreen", "Recentes"))
        self.tabela_documentos.headerItem().setText(0, _translate("UserFilesScreen", "Arquivo"))
        self.tabela_documentos.headerItem().setText(1, _translate("UserFilesScreen", "Tamanho(MB)"))
        self.tabela_documentos.headerItem().setText(2, _translate("UserFilesScreen", "Diretório"))
        self.tabela_documentos.headerItem().setText(3, _translate("UserFilesScreen", "Data "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("UserFilesScreen", "Documentos"))
        self.tabela_imagens.headerItem().setText(0, _translate("UserFilesScreen", "Arquivo"))
        self.tabela_imagens.headerItem().setText(1, _translate("UserFilesScreen", "Tamanho(MB)"))
        self.tabela_imagens.headerItem().setText(2, _translate("UserFilesScreen", "Diretório"))
        self.tabela_imagens.headerItem().setText(3, _translate("UserFilesScreen", "Data "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("UserFilesScreen", "Imagens"))
        self.tabela_videos.headerItem().setText(0, _translate("UserFilesScreen", "Arquivo"))
        self.tabela_videos.headerItem().setText(1, _translate("UserFilesScreen", "Tamanho(MB)"))
        self.tabela_videos.headerItem().setText(2, _translate("UserFilesScreen", "Diretório"))
        self.tabela_videos.headerItem().setText(3, _translate("UserFilesScreen", "Data "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("UserFilesScreen", "Vídeos"))
        self.tabela_musicas.headerItem().setText(0, _translate("UserFilesScreen", "Arquivo"))
        self.tabela_musicas.headerItem().setText(1, _translate("UserFilesScreen", "Tamanho(MB)"))
        self.tabela_musicas.headerItem().setText(2, _translate("UserFilesScreen", "Diretório"))
        self.tabela_musicas.headerItem().setText(3, _translate("UserFilesScreen", "Data "))
        self.tabela_musicas.headerItem().setText(4, _translate("UserFilesScreen", "Ação"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("UserFilesScreen", "Músicas"))
        self.tabela_compartilhados.headerItem().setText(0, _translate("UserFilesScreen", "Arquivo"))
        self.tabela_compartilhados.headerItem().setText(1, _translate("UserFilesScreen", "Tamanho(MB)"))
        self.tabela_compartilhados.headerItem().setText(2, _translate("UserFilesScreen", "Diretório"))
        self.tabela_compartilhados.headerItem().setText(3, _translate("UserFilesScreen", "Data "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("UserFilesScreen", "Compartilhados"))
        self.tabela_outros.headerItem().setText(0, _translate("UserFilesScreen", "Arquivo"))
        self.tabela_outros.headerItem().setText(1, _translate("UserFilesScreen", "Tamanho(MB)"))
        self.tabela_outros.headerItem().setText(2, _translate("UserFilesScreen", "Diretório"))
        self.tabela_outros.headerItem().setText(3, _translate("UserFilesScreen", "Data "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("UserFilesScreen", "Outros"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserFilesScreen = QtWidgets.QMainWindow()
    ui = Ui_UserFilesScreen()
    ui.setupUi(UserFilesScreen)
    UserFilesScreen.show()
    sys.exit(app.exec_())
