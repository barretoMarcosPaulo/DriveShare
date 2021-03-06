# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nova_tela_pastas.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserFilesScreen(object):


    def loadData(self, lista, tabela):
        tabela.setRowCount(0)
        self.buttons = []
        self.infos = []
        for row_number in range(len(lista)):
            tabela.insertRow(row_number)
            tabela.setItem(row_number, 0, QtWidgets.QTableWidgetItem(lista[row_number][1]))
            tabela.setItem(row_number, 1, QtWidgets.QTableWidgetItem(lista[row_number][2]))
            tabela.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(lista[row_number][3])))
            tabela.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(lista[row_number][4])))
            tabela.setItem(row_number, 4, QtWidgets.QTableWidgetItem("Download"))
            self.infos.append(lista[row_number])

    def setupUi(self, UserFilesScreen):
        UserFilesScreen.setObjectName("UserFilesScreen")
        UserFilesScreen.setWindowModality(QtCore.Qt.NonModal)
        UserFilesScreen.resize(916, 615)
        UserFilesScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        UserFilesScreen.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(UserFilesScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(370, 550, 181, 31))
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
        self.tabWidget.setGeometry(QtCore.QRect(20, 100, 871, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tableWidget.setMinimumSize(QtCore.QSize(871, 421))
        self.tableWidget.setMaximumSize(QtCore.QSize(871, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.escolher_destino = QtWidgets.QGroupBox(self.tab)
        self.escolher_destino.setGeometry(QtCore.QRect(160, 0, 531, 201))
        self.escolher_destino.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.escolher_destino.setObjectName("escolher_destino")
        self.salvar_arquivo = QtWidgets.QPushButton(self.escolher_destino)
        self.salvar_arquivo.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo.setObjectName("salvar_arquivo")
        self.caminho = QtWidgets.QLineEdit(self.escolher_destino)
        self.caminho.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho.setObjectName("caminho")
        self.cancelar = QtWidgets.QPushButton(self.escolher_destino)
        self.cancelar.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar.setObjectName("cancelar")
        self.btn_comp_6 = QtWidgets.QPushButton(self.escolher_destino)
        self.btn_comp_6.setGeometry(QtCore.QRect(330, 150, 131, 28))
        self.btn_comp_6.setObjectName("btn_comp_6")
        self.label_9 = QtWidgets.QLabel(self.escolher_destino)
        self.label_9.setGeometry(QtCore.QRect(300, 110, 191, 20))
        self.label_9.setObjectName("label_9")
        self.enviar = QtWidgets.QGroupBox(self.tab)
        self.enviar.setGeometry(QtCore.QRect(160, 210, 531, 201))
        self.enviar.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.enviar.setObjectName("enviar")
        self.salvar_arquivo_11 = QtWidgets.QPushButton(self.enviar)
        self.salvar_arquivo_11.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_11.setObjectName("salvar_arquivo_11")
        self.caminho_11 = QtWidgets.QLineEdit(self.enviar)
        self.caminho_11.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_11.setObjectName("caminho_11")
        self.cancelar_11 = QtWidgets.QPushButton(self.enviar)
        self.cancelar_11.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_11.setObjectName("cancelar_11")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.escolher_destino_2 = QtWidgets.QGroupBox(self.tab_2)
        self.escolher_destino_2.setGeometry(QtCore.QRect(150, 20, 531, 191))
        self.escolher_destino_2.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.escolher_destino_2.setObjectName("escolher_destino_2")
        self.salvar_arquivo_2 = QtWidgets.QPushButton(self.escolher_destino_2)
        self.salvar_arquivo_2.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_2.setObjectName("salvar_arquivo_2")
        self.caminho_2 = QtWidgets.QLineEdit(self.escolher_destino_2)
        self.caminho_2.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_2.setObjectName("caminho_2")
        self.cancelar_2 = QtWidgets.QPushButton(self.escolher_destino_2)
        self.cancelar_2.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_2.setObjectName("cancelar_2")
        self.btn_comp_5 = QtWidgets.QPushButton(self.escolher_destino_2)
        self.btn_comp_5.setGeometry(QtCore.QRect(340, 140, 131, 28))
        self.btn_comp_5.setObjectName("btn_comp_5")
        self.label_8 = QtWidgets.QLabel(self.escolher_destino_2)
        self.label_8.setGeometry(QtCore.QRect(310, 110, 191, 20))
        self.label_8.setObjectName("label_8")
        self.enviar_2 = QtWidgets.QGroupBox(self.tab_2)
        self.enviar_2.setGeometry(QtCore.QRect(150, 220, 531, 201))
        self.enviar_2.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.enviar_2.setObjectName("enviar_2")
        self.salvar_arquivo_12 = QtWidgets.QPushButton(self.enviar_2)
        self.salvar_arquivo_12.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_12.setObjectName("salvar_arquivo_12")
        self.caminho_12 = QtWidgets.QLineEdit(self.enviar_2)
        self.caminho_12.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_12.setObjectName("caminho_12")
        self.cancelar_12 = QtWidgets.QPushButton(self.enviar_2)
        self.cancelar_12.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_12.setObjectName("cancelar_12")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.escolher_destino_3 = QtWidgets.QGroupBox(self.tab_3)
        self.escolher_destino_3.setGeometry(QtCore.QRect(150, 10, 531, 191))
        self.escolher_destino_3.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.escolher_destino_3.setObjectName("escolher_destino_3")
        self.salvar_arquivo_3 = QtWidgets.QPushButton(self.escolher_destino_3)
        self.salvar_arquivo_3.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_3.setObjectName("salvar_arquivo_3")
        self.caminho_3 = QtWidgets.QLineEdit(self.escolher_destino_3)
        self.caminho_3.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_3.setObjectName("caminho_3")
        self.cancelar_3 = QtWidgets.QPushButton(self.escolher_destino_3)
        self.cancelar_3.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_3.setObjectName("cancelar_3")
        self.btn_comp_4 = QtWidgets.QPushButton(self.escolher_destino_3)
        self.btn_comp_4.setGeometry(QtCore.QRect(330, 140, 131, 28))
        self.btn_comp_4.setObjectName("btn_comp_4")
        self.label_7 = QtWidgets.QLabel(self.escolher_destino_3)
        self.label_7.setGeometry(QtCore.QRect(300, 110, 191, 20))
        self.label_7.setObjectName("label_7")
        self.enviar_3 = QtWidgets.QGroupBox(self.tab_3)
        self.enviar_3.setGeometry(QtCore.QRect(140, 220, 531, 201))
        self.enviar_3.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.enviar_3.setObjectName("enviar_3")
        self.salvar_arquivo_13 = QtWidgets.QPushButton(self.enviar_3)
        self.salvar_arquivo_13.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_13.setObjectName("salvar_arquivo_13")
        self.caminho_13 = QtWidgets.QLineEdit(self.enviar_3)
        self.caminho_13.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_13.setObjectName("caminho_13")
        self.cancelar_13 = QtWidgets.QPushButton(self.enviar_3)
        self.cancelar_13.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_13.setObjectName("cancelar_13")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.escolher_destino_4 = QtWidgets.QGroupBox(self.tab_4)
        self.escolher_destino_4.setGeometry(QtCore.QRect(140, 0, 531, 191))
        self.escolher_destino_4.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.escolher_destino_4.setObjectName("escolher_destino_4")
        self.salvar_arquivo_5 = QtWidgets.QPushButton(self.escolher_destino_4)
        self.salvar_arquivo_5.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_5.setObjectName("salvar_arquivo_5")
        self.caminho_5 = QtWidgets.QLineEdit(self.escolher_destino_4)
        self.caminho_5.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_5.setObjectName("caminho_5")
        self.cancelar_5 = QtWidgets.QPushButton(self.escolher_destino_4)
        self.cancelar_5.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_5.setObjectName("cancelar_5")
        self.btn_comp_3 = QtWidgets.QPushButton(self.escolher_destino_4)
        self.btn_comp_3.setGeometry(QtCore.QRect(340, 130, 131, 28))
        self.btn_comp_3.setObjectName("btn_comp_3")
        self.label_6 = QtWidgets.QLabel(self.escolher_destino_4)
        self.label_6.setGeometry(QtCore.QRect(310, 100, 191, 20))
        self.label_6.setObjectName("label_6")
        self.enviar_4 = QtWidgets.QGroupBox(self.tab_4)
        self.enviar_4.setGeometry(QtCore.QRect(140, 200, 531, 201))
        self.enviar_4.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.enviar_4.setObjectName("enviar_4")
        self.salvar_arquivo_14 = QtWidgets.QPushButton(self.enviar_4)
        self.salvar_arquivo_14.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_14.setObjectName("salvar_arquivo_14")
        self.caminho_14 = QtWidgets.QLineEdit(self.enviar_4)
        self.caminho_14.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_14.setObjectName("caminho_14")
        self.cancelar_14 = QtWidgets.QPushButton(self.enviar_4)
        self.cancelar_14.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_14.setObjectName("cancelar_14")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        self.escolher_destino_5 = QtWidgets.QGroupBox(self.tab_5)
        self.escolher_destino_5.setGeometry(QtCore.QRect(150, 0, 531, 171))
        self.escolher_destino_5.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.escolher_destino_5.setObjectName("escolher_destino_5")
        self.salvar_arquivo_6 = QtWidgets.QPushButton(self.escolher_destino_5)
        self.salvar_arquivo_6.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_6.setObjectName("salvar_arquivo_6")
        self.caminho_6 = QtWidgets.QLineEdit(self.escolher_destino_5)
        self.caminho_6.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_6.setObjectName("caminho_6")
        self.cancelar_6 = QtWidgets.QPushButton(self.escolher_destino_5)
        self.cancelar_6.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_6.setObjectName("cancelar_6")
        self.btn_comp_2 = QtWidgets.QPushButton(self.escolher_destino_5)
        self.btn_comp_2.setGeometry(QtCore.QRect(330, 130, 131, 28))
        self.btn_comp_2.setObjectName("btn_comp_2")
        self.label_5 = QtWidgets.QLabel(self.escolher_destino_5)
        self.label_5.setGeometry(QtCore.QRect(300, 100, 191, 20))
        self.label_5.setObjectName("label_5")
        self.enviar_5 = QtWidgets.QGroupBox(self.tab_5)
        self.enviar_5.setGeometry(QtCore.QRect(150, 190, 531, 201))
        self.enviar_5.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.enviar_5.setObjectName("enviar_5")
        self.salvar_arquivo_16 = QtWidgets.QPushButton(self.enviar_5)
        self.salvar_arquivo_16.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_16.setObjectName("salvar_arquivo_16")
        self.caminho_16 = QtWidgets.QLineEdit(self.enviar_5)
        self.caminho_16.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_16.setObjectName("caminho_16")
        self.cancelar_16 = QtWidgets.QPushButton(self.enviar_5)
        self.cancelar_16.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_16.setObjectName("cancelar_16")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 0, 871, 371))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(5)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        self.escolher_destino_6 = QtWidgets.QGroupBox(self.tab_7)
        self.escolher_destino_6.setGeometry(QtCore.QRect(130, 90, 531, 181))
        self.escolher_destino_6.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.escolher_destino_6.setObjectName("escolher_destino_6")
        self.salvar_arquivo_7 = QtWidgets.QPushButton(self.escolher_destino_6)
        self.salvar_arquivo_7.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_7.setObjectName("salvar_arquivo_7")
        self.caminho_7 = QtWidgets.QLineEdit(self.escolher_destino_6)
        self.caminho_7.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_7.setObjectName("caminho_7")
        self.cancelar_7 = QtWidgets.QPushButton(self.escolher_destino_6)
        self.cancelar_7.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_7.setObjectName("cancelar_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_7.setGeometry(QtCore.QRect(0, 0, 871, 421))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(5)
        self.tableWidget_7.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        self.escolher_destino_7 = QtWidgets.QGroupBox(self.tab_6)
        self.escolher_destino_7.setGeometry(QtCore.QRect(160, 0, 531, 171))
        self.escolher_destino_7.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.escolher_destino_7.setObjectName("escolher_destino_7")
        self.salvar_arquivo_8 = QtWidgets.QPushButton(self.escolher_destino_7)
        self.salvar_arquivo_8.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_8.setObjectName("salvar_arquivo_8")
        self.caminho_8 = QtWidgets.QLineEdit(self.escolher_destino_7)
        self.caminho_8.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_8.setObjectName("caminho_8")
        self.cancelar_8 = QtWidgets.QPushButton(self.escolher_destino_7)
        self.cancelar_8.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_8.setObjectName("cancelar_8")
        self.btn_comp = QtWidgets.QPushButton(self.escolher_destino_7)
        self.btn_comp.setGeometry(QtCore.QRect(330, 130, 131, 28))
        self.btn_comp.setObjectName("btn_comp")
        self.label_4 = QtWidgets.QLabel(self.escolher_destino_7)
        self.label_4.setGeometry(QtCore.QRect(300, 100, 191, 20))
        self.label_4.setObjectName("label_4")
        self.enviar_6 = QtWidgets.QGroupBox(self.tab_6)
        self.enviar_6.setGeometry(QtCore.QRect(160, 180, 531, 201))
        self.enviar_6.setStyleSheet("background-color: #f1f2f3f4;\n"
"")
        self.enviar_6.setObjectName("enviar_6")
        self.salvar_arquivo_19 = QtWidgets.QPushButton(self.enviar_6)
        self.salvar_arquivo_19.setGeometry(QtCore.QRect(300, 70, 90, 28))
        self.salvar_arquivo_19.setObjectName("salvar_arquivo_19")
        self.caminho_19 = QtWidgets.QLineEdit(self.enviar_6)
        self.caminho_19.setGeometry(QtCore.QRect(20, 70, 271, 28))
        self.caminho_19.setObjectName("caminho_19")
        self.cancelar_19 = QtWidgets.QPushButton(self.enviar_6)
        self.cancelar_19.setGeometry(QtCore.QRect(400, 70, 91, 28))
        self.cancelar_19.setObjectName("cancelar_19")
        self.tabWidget.addTab(self.tab_6, "")
        UserFilesScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UserFilesScreen)
        self.statusbar.setObjectName("statusbar")
        UserFilesScreen.setStatusBar(self.statusbar)

        self.retranslateUi(UserFilesScreen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UserFilesScreen)

    def retranslateUi(self, UserFilesScreen):
        _translate = QtCore.QCoreApplication.translate
        UserFilesScreen.setWindowTitle(_translate("UserFilesScreen", "MainWindow"))
        self.uploadButton.setText(_translate("UserFilesScreen", "Upload"))
        self.label_2.setText(_translate("UserFilesScreen", "<html><head/><body><p><img src=\"logoShare.png\"/></p></body></html>"))
        self.label_3.setText(_translate("UserFilesScreen", "DriveShare"))
        self.version_app.setText(_translate("UserFilesScreen", "Versão 1.0"))
        self.label.setText(_translate("UserFilesScreen", "Marcos Paulo"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("UserFilesScreen", "Arquivo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("UserFilesScreen", "Diretório"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("UserFilesScreen", "Tamanho(B)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("UserFilesScreen", "Data"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("UserFilesScreen", "Ações"))
        self.escolher_destino.setTitle(_translate("UserFilesScreen", "Escolha um local para salvar o arquivo"))
        self.salvar_arquivo.setText(_translate("UserFilesScreen", "Salvar"))
        self.cancelar.setText(_translate("UserFilesScreen", "Cancelar"))
        self.btn_comp_6.setText(_translate("UserFilesScreen", "Compartilhar"))
        self.label_9.setText(_translate("UserFilesScreen", "_____________Ou______________"))
        self.enviar.setTitle(_translate("UserFilesScreen", "Envie esse arquivo para um amigo -informe o email do destinatário"))
        self.salvar_arquivo_11.setText(_translate("UserFilesScreen", "Enviar"))
        self.cancelar_11.setText(_translate("UserFilesScreen", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("UserFilesScreen", "Recentes"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("UserFilesScreen", "Arquivo"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("UserFilesScreen", "Diretório"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("UserFilesScreen", "Tamanho(B)"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("UserFilesScreen", "Data"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("UserFilesScreen", "Ações"))
        self.escolher_destino_2.setTitle(_translate("UserFilesScreen", "Escolha um local para salvar o arquivo"))
        self.salvar_arquivo_2.setText(_translate("UserFilesScreen", "Salvar"))
        self.cancelar_2.setText(_translate("UserFilesScreen", "Cancelar"))
        self.btn_comp_5.setText(_translate("UserFilesScreen", "Compartilhar"))
        self.label_8.setText(_translate("UserFilesScreen", "_____________Ou______________"))
        self.enviar_2.setTitle(_translate("UserFilesScreen", "Envie esse arquivo para um amigo -informe o email do destinatário"))
        self.salvar_arquivo_12.setText(_translate("UserFilesScreen", "Enviar"))
        self.cancelar_12.setText(_translate("UserFilesScreen", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("UserFilesScreen", "Documentos"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("UserFilesScreen", "Arquivo"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("UserFilesScreen", "Diretório"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("UserFilesScreen", "Tamanho(B)"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("UserFilesScreen", "Data"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("UserFilesScreen", "Ações"))
        self.escolher_destino_3.setTitle(_translate("UserFilesScreen", "Escolha um local para salvar o arquivo"))
        self.salvar_arquivo_3.setText(_translate("UserFilesScreen", "Salvar"))
        self.cancelar_3.setText(_translate("UserFilesScreen", "Cancelar"))
        self.btn_comp_4.setText(_translate("UserFilesScreen", "Compartilhar"))
        self.label_7.setText(_translate("UserFilesScreen", "_____________Ou______________"))
        self.enviar_3.setTitle(_translate("UserFilesScreen", "Envie esse arquivo para um amigo -informe o email do destinatário"))
        self.salvar_arquivo_13.setText(_translate("UserFilesScreen", "Enviar"))
        self.cancelar_13.setText(_translate("UserFilesScreen", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("UserFilesScreen", "Imagens"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("UserFilesScreen", "Arquivo"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("UserFilesScreen", "Diretório"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("UserFilesScreen", "Tamanho(B)"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("UserFilesScreen", "Data"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("UserFilesScreen", "Ações"))
        self.escolher_destino_4.setTitle(_translate("UserFilesScreen", "Escolha um local para salvar o arquivo"))
        self.salvar_arquivo_5.setText(_translate("UserFilesScreen", "Salvar"))
        self.cancelar_5.setText(_translate("UserFilesScreen", "Cancelar"))
        self.btn_comp_3.setText(_translate("UserFilesScreen", "Compartilhar"))
        self.label_6.setText(_translate("UserFilesScreen", "_____________Ou______________"))
        self.enviar_4.setTitle(_translate("UserFilesScreen", "Envie esse arquivo para um amigo -informe o email do destinatário"))
        self.salvar_arquivo_14.setText(_translate("UserFilesScreen", "Enviar"))
        self.cancelar_14.setText(_translate("UserFilesScreen", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("UserFilesScreen", "Vídeos"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("UserFilesScreen", "Arquivo"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("UserFilesScreen", "Diretório"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("UserFilesScreen", "Tamanho(B)"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("UserFilesScreen", "Data"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("UserFilesScreen", "Ações"))
        self.escolher_destino_5.setTitle(_translate("UserFilesScreen", "Escolha um local para salvar o arquivo"))
        self.salvar_arquivo_6.setText(_translate("UserFilesScreen", "Salvar"))
        self.cancelar_6.setText(_translate("UserFilesScreen", "Cancelar"))
        self.btn_comp_2.setText(_translate("UserFilesScreen", "Compartilhar"))
        self.label_5.setText(_translate("UserFilesScreen", "_____________Ou______________"))
        self.enviar_5.setTitle(_translate("UserFilesScreen", "Envie esse arquivo para um amigo -informe o email do destinatário"))
        self.salvar_arquivo_16.setText(_translate("UserFilesScreen", "Enviar"))
        self.cancelar_16.setText(_translate("UserFilesScreen", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("UserFilesScreen", "Músicas"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("UserFilesScreen", "Arquivo"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("UserFilesScreen", "Diretório"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("UserFilesScreen", "Tamanho(B)"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("UserFilesScreen", "Data"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("UserFilesScreen", "Ações"))
        self.escolher_destino_6.setTitle(_translate("UserFilesScreen", "Escolha um local para salvar o arquivo"))
        self.salvar_arquivo_7.setText(_translate("UserFilesScreen", "Salvar"))
        self.cancelar_7.setText(_translate("UserFilesScreen", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("UserFilesScreen", "Compartilhados"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("UserFilesScreen", "Arquivo"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("UserFilesScreen", "Diretório"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("UserFilesScreen", "Tamanho(B)"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("UserFilesScreen", "Data"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("UserFilesScreen", "Ações"))
        self.escolher_destino_7.setTitle(_translate("UserFilesScreen", "Escolha um local para salvar o arquivo"))
        self.salvar_arquivo_8.setText(_translate("UserFilesScreen", "Salvar"))
        self.cancelar_8.setText(_translate("UserFilesScreen", "Cancelar"))
        self.btn_comp.setText(_translate("UserFilesScreen", "Compartilhar"))
        self.label_4.setText(_translate("UserFilesScreen", "_____________Ou______________"))
        self.enviar_6.setTitle(_translate("UserFilesScreen", "Envie esse arquivo para um amigo -informe o email do destinatário"))
        self.salvar_arquivo_19.setText(_translate("UserFilesScreen", "Enviar"))
        self.cancelar_19.setText(_translate("UserFilesScreen", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("UserFilesScreen", "Outros"))
import imageLogo_rc
import logo_user_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserFilesScreen = QtWidgets.QMainWindow()
    ui = Ui_UserFilesScreen()
    ui.setupUi(UserFilesScreen)
    UserFilesScreen.show()
    sys.exit(app.exec_())
