# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topy.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import resources_cs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background: #F4F4F4;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background: #242527;\n"
"    color: #FAFAFA;\n"
"    font: 9pt \"Bahnschrift Light\";\n"
"    min-height: 22px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #35363A;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    font: 9pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background: #FFFFFF;\n"
"    padding-right: 8px;\n"
"    border: 0px solid #FDFFFC;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #242527;\n"
"    font: 75 12pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"QComboBox {\n"
"    background: #FDFFFC;\n"
"    border-radius: 2px;\n"
"    font: 15px \"Bahnschrift Light\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border-style: solid;\n"
"    border: 0px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: transparent;\n"
"    border: 0px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.GuitarTracks = QtWidgets.QVBoxLayout()
        self.GuitarTracks.setObjectName("GuitarTracks")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.GuitarTracks.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.GuitarTracks)
        self.DrumTracks = QtWidgets.QVBoxLayout()
        self.DrumTracks.setObjectName("DrumTracks")
        self.AddTrack = QtWidgets.QGroupBox(self.centralwidget)
        self.AddTrack.setMinimumSize(QtCore.QSize(0, 50))
        self.AddTrack.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AddTrack.setStyleSheet("QGroupBox {\n"
"    padding-right: -8px;\n"
"    background: transparent;\n"
"}")
        self.AddTrack.setTitle("")
        self.AddTrack.setObjectName("AddTrack")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.AddTrack)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.AddTrack_button = QtWidgets.QPushButton(self.AddTrack)
        self.AddTrack_button.setMaximumSize(QtCore.QSize(40, 40))
        self.AddTrack_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/плюс.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddTrack_button.setIcon(icon2)
        self.AddTrack_button.setIconSize(QtCore.QSize(40, 40))
        self.AddTrack_button.setFlat(True)
        self.AddTrack_button.setObjectName("AddTrack_button")
        self.horizontalLayout_4.addWidget(self.AddTrack_button)
        self.DrumTracks.addWidget(self.AddTrack)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.DrumTracks.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.DrumTracks)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 28))
        self.menubar.setMinimumSize(QtCore.QSize(0, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menuFile.addAction(self.action_2)
        self.menuFile.addAction(self.action_3)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_2.setText(_translate("MainWindow", "Open"))
        self.action_3.setText(_translate("MainWindow", "Save"))

