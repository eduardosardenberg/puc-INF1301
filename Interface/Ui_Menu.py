#Autor: Victor Nielsen
#Tempo: 5 horas


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\victo\Desktop\PUC\Modular\Projeto\Ludo-Python\Interface\Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(750, 609)
        Menu.setMinimumSize(QtCore.QSize(750, 609))
        Menu.setMaximumSize(QtCore.QSize(750, 609))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imagens/ludo_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Menu.setWindowIcon(icon)
        Menu.setStyleSheet("")
        self.MenuWidget = QtWidgets.QWidget(Menu)
        self.MenuWidget.setStyleSheet("QWidget#MenuWidget {\n"
"background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"")
        self.MenuWidget.setObjectName("MenuWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MenuWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageLayout = QtWidgets.QWidget(self.MenuWidget)
        self.imageLayout.setObjectName("imageLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.imageLayout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTitle = QtWidgets.QLabel(self.imageLayout)
        self.labelTitle.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout_2.addWidget(self.labelTitle, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.imageTitle = QtWidgets.QLabel(self.imageLayout)
        self.imageTitle.setMinimumSize(QtCore.QSize(300, 300))
        self.imageTitle.setMaximumSize(QtCore.QSize(300, 300))
        self.imageTitle.setStyleSheet("image: url(:/Imagens/peca.png);")
        self.imageTitle.setText("")
        self.imageTitle.setObjectName("imageTitle")
        self.verticalLayout_2.addWidget(self.imageTitle, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.imageLayout, 0, QtCore.Qt.AlignHCenter)
        self.optionsLayout = QtWidgets.QWidget(self.MenuWidget)
        self.optionsLayout.setStyleSheet("\n"
"QPushButton:hover {\n"
"    background-color: rgb(180,180,180);\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180,180, 180);\n"
"}")
        self.optionsLayout.setObjectName("optionsLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.optionsLayout)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.menuOptions = QtWidgets.QWidget(self.optionsLayout)
        self.menuOptions.setMinimumSize(QtCore.QSize(0, 0))
        self.menuOptions.setMaximumSize(QtCore.QSize(430, 600))
        self.menuOptions.setObjectName("menuOptions")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menuOptions)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonPlay = QtWidgets.QPushButton(self.menuOptions)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPlay.setFont(font)
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.verticalLayout_3.addWidget(self.pushButtonPlay)
        self.pushButtonRules = QtWidgets.QPushButton(self.menuOptions)
        self.pushButtonRules.setObjectName("pushButtonRules")
        self.verticalLayout_3.addWidget(self.pushButtonRules)
        self.pushButtonHistory = QtWidgets.QPushButton(self.menuOptions)
        self.pushButtonHistory.setObjectName("pushButtonHistory")
        self.verticalLayout_3.addWidget(self.pushButtonHistory)
        self.pushButtonExit = QtWidgets.QPushButton(self.menuOptions)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.verticalLayout_3.addWidget(self.pushButtonExit)
        self.verticalLayout_4.addWidget(self.menuOptions)
        self.playerOptions = QtWidgets.QWidget(self.optionsLayout)
        self.playerOptions.setMinimumSize(QtCore.QSize(0, 0))
        self.playerOptions.setMaximumSize(QtCore.QSize(430, 600))
        self.playerOptions.setObjectName("playerOptions")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.playerOptions)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.numPlayersLayout = QtWidgets.QWidget(self.playerOptions)
        self.numPlayersLayout.setMaximumSize(QtCore.QSize(500, 60))
        self.numPlayersLayout.setObjectName("numPlayersLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.numPlayersLayout)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelNumPlayers = QtWidgets.QLabel(self.numPlayersLayout)
        self.labelNumPlayers.setMinimumSize(QtCore.QSize(240, 0))
        self.labelNumPlayers.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelNumPlayers.setFont(font)
        self.labelNumPlayers.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNumPlayers.setObjectName("labelNumPlayers")
        self.horizontalLayout_4.addWidget(self.labelNumPlayers, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.spinBoxNumPlayers = QtWidgets.QSpinBox(self.numPlayersLayout)
        self.spinBoxNumPlayers.setMinimumSize(QtCore.QSize(90, 0))
        self.spinBoxNumPlayers.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxNumPlayers.setFont(font)
        self.spinBoxNumPlayers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBoxNumPlayers.setReadOnly(False)
        self.spinBoxNumPlayers.setMinimum(2)
        self.spinBoxNumPlayers.setMaximum(4)
        self.spinBoxNumPlayers.setProperty("value", 2)
        self.spinBoxNumPlayers.setObjectName("spinBoxNumPlayers")
        self.horizontalLayout_4.addWidget(self.spinBoxNumPlayers)
        self.verticalLayout_6.addWidget(self.numPlayersLayout, 0, QtCore.Qt.AlignLeft)
        self.warningLayout = QtWidgets.QWidget(self.playerOptions)
        self.warningLayout.setMinimumSize(QtCore.QSize(0, 50))
        self.warningLayout.setMaximumSize(QtCore.QSize(16777215, 30))
        self.warningLayout.setObjectName("warningLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.warningLayout)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.warningImage = QtWidgets.QLabel(self.warningLayout)
        self.warningImage.setMinimumSize(QtCore.QSize(30, 30))
        self.warningImage.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.warningImage.setFont(font)
        self.warningImage.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.warningImage.setStyleSheet("image: url(:/Imagens/warningIcon.png);")
        self.warningImage.setText("")
        self.warningImage.setObjectName("warningImage")
        self.horizontalLayout_11.addWidget(self.warningImage)
        self.warningLabel = QtWidgets.QLabel(self.warningLayout)
        self.warningLabel.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.warningLabel.setFont(font)
        self.warningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warningLabel.setObjectName("warningLabel")
        self.horizontalLayout_11.addWidget(self.warningLabel)
        self.verticalLayout_6.addWidget(self.warningLayout, 0, QtCore.Qt.AlignLeft)
        self.optionsP1 = QtWidgets.QWidget(self.playerOptions)
        self.optionsP1.setMinimumSize(QtCore.QSize(0, 50))
        self.optionsP1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.optionsP1.setObjectName("optionsP1")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.optionsP1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelP1 = QtWidgets.QLabel(self.optionsP1)
        self.labelP1.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelP1.setFont(font)
        self.labelP1.setObjectName("labelP1")
        self.horizontalLayout_10.addWidget(self.labelP1)
        self.lineEditP1 = QtWidgets.QLineEdit(self.optionsP1)
        self.lineEditP1.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEditP1.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditP1.setFont(font)
        self.lineEditP1.setObjectName("lineEditP1")
        self.horizontalLayout_10.addWidget(self.lineEditP1)
        self.colorP1 = QtWidgets.QToolButton(self.optionsP1)
        self.colorP1.setMinimumSize(QtCore.QSize(30, 30))
        self.colorP1.setMaximumSize(QtCore.QSize(30, 30))
        self.colorP1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.colorP1.setText("")
        self.colorP1.setObjectName("colorP1")
        self.horizontalLayout_10.addWidget(self.colorP1)
        self.verticalLayout_6.addWidget(self.optionsP1)
        self.optionsP2 = QtWidgets.QWidget(self.playerOptions)
        self.optionsP2.setMinimumSize(QtCore.QSize(0, 50))
        self.optionsP2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.optionsP2.setObjectName("optionsP2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.optionsP2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelP2 = QtWidgets.QLabel(self.optionsP2)
        self.labelP2.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelP2.setFont(font)
        self.labelP2.setObjectName("labelP2")
        self.horizontalLayout_6.addWidget(self.labelP2)
        self.lineEditP2 = QtWidgets.QLineEdit(self.optionsP2)
        self.lineEditP2.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEditP2.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditP2.setFont(font)
        self.lineEditP2.setObjectName("lineEditP2")
        self.horizontalLayout_6.addWidget(self.lineEditP2)
        self.colorP2 = QtWidgets.QToolButton(self.optionsP2)
        self.colorP2.setMinimumSize(QtCore.QSize(30, 30))
        self.colorP2.setMaximumSize(QtCore.QSize(30, 30))
        self.colorP2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.colorP2.setText("")
        self.colorP2.setObjectName("colorP2")
        self.horizontalLayout_6.addWidget(self.colorP2)
        self.verticalLayout_6.addWidget(self.optionsP2)
        self.optionsP3 = QtWidgets.QWidget(self.playerOptions)
        self.optionsP3.setMinimumSize(QtCore.QSize(0, 50))
        self.optionsP3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.optionsP3.setObjectName("optionsP3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.optionsP3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelP3 = QtWidgets.QLabel(self.optionsP3)
        self.labelP3.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelP3.setFont(font)
        self.labelP3.setObjectName("labelP3")
        self.horizontalLayout_7.addWidget(self.labelP3)
        self.lineEditP3 = QtWidgets.QLineEdit(self.optionsP3)
        self.lineEditP3.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEditP3.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditP3.setFont(font)
        self.lineEditP3.setObjectName("lineEditP3")
        self.horizontalLayout_7.addWidget(self.lineEditP3)
        self.colorP3 = QtWidgets.QToolButton(self.optionsP3)
        self.colorP3.setMinimumSize(QtCore.QSize(30, 30))
        self.colorP3.setMaximumSize(QtCore.QSize(30, 30))
        self.colorP3.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.colorP3.setText("")
        self.colorP3.setObjectName("colorP3")
        self.horizontalLayout_7.addWidget(self.colorP3)
        self.verticalLayout_6.addWidget(self.optionsP3)
        self.optionsP4 = QtWidgets.QWidget(self.playerOptions)
        self.optionsP4.setMinimumSize(QtCore.QSize(0, 50))
        self.optionsP4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.optionsP4.setObjectName("optionsP4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.optionsP4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelP4 = QtWidgets.QLabel(self.optionsP4)
        self.labelP4.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelP4.setFont(font)
        self.labelP4.setObjectName("labelP4")
        self.horizontalLayout_8.addWidget(self.labelP4)
        self.lineEditP4 = QtWidgets.QLineEdit(self.optionsP4)
        self.lineEditP4.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEditP4.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditP4.setFont(font)
        self.lineEditP4.setObjectName("lineEditP4")
        self.horizontalLayout_8.addWidget(self.lineEditP4)
        self.colorP4 = QtWidgets.QToolButton(self.optionsP4)
        self.colorP4.setMinimumSize(QtCore.QSize(30, 30))
        self.colorP4.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.colorP4.setText("")
        self.colorP4.setObjectName("colorP4")
        self.horizontalLayout_8.addWidget(self.colorP4)
        self.verticalLayout_6.addWidget(self.optionsP4)
        self.ConfirmCancelButtons = QtWidgets.QWidget(self.playerOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConfirmCancelButtons.sizePolicy().hasHeightForWidth())
        self.ConfirmCancelButtons.setSizePolicy(sizePolicy)
        self.ConfirmCancelButtons.setStyleSheet("")
        self.ConfirmCancelButtons.setObjectName("ConfirmCancelButtons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ConfirmCancelButtons)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonBack = QtWidgets.QPushButton(self.ConfirmCancelButtons)
        self.pushButtonBack.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonBack.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButtonBack.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.horizontalLayout_3.addWidget(self.pushButtonBack)
        self.pushButtonStart = QtWidgets.QPushButton(self.ConfirmCancelButtons)
        self.pushButtonStart.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonStart.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonStart.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.horizontalLayout_3.addWidget(self.pushButtonStart)
        self.verticalLayout_6.addWidget(self.ConfirmCancelButtons)
        self.verticalLayout_4.addWidget(self.playerOptions)
        self.horizontalLayout.addWidget(self.optionsLayout)
        Menu.setCentralWidget(self.MenuWidget)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Ludo"))
        self.labelTitle.setText(_translate("Menu", "Ludo"))
        self.pushButtonPlay.setText(_translate("Menu", "Jogar"))
        self.pushButtonRules.setText(_translate("Menu", "Regras"))
        self.pushButtonHistory.setText(_translate("Menu", "Histórico"))
        self.pushButtonExit.setText(_translate("Menu", "Sair"))
        self.labelNumPlayers.setText(_translate("Menu", "  Número de jogadores:"))
        self.warningLabel.setText(_translate("Menu", "Nome ou cor de jogador inválido"))
        self.labelP1.setText(_translate("Menu", "P1:"))
        self.labelP2.setText(_translate("Menu", "P2:"))
        self.labelP3.setText(_translate("Menu", "P3:"))
        self.labelP4.setText(_translate("Menu", "P4:"))
        self.pushButtonBack.setText(_translate("Menu", "Voltar ao Menu"))
        self.pushButtonStart.setText(_translate("Menu", "Iniciar Partida"))
import Interface.Resources.resources_rc
