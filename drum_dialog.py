# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drum_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 121)
        Dialog.setStyleSheet("QDialog {\n"
"    background: #242527;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"    font: 75 11pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"QComboBox {\n"
"    background: #FFFFFF;\n"
"    border-radius: 2px;\n"
"    font: 16px \"Bahnschrift Light\";\n"
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
"QLineEdit {\n"
"    background: #FFFFFF;\n"
"    border-radius: 2px;\n"
"    font: 16px \"Bahnschrift Light\";\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: transparent;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QDialogButtonBox::Ok {\n"
"    background: #FFFFFF;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")

        self.base_track_label = QtWidgets.QLabel(Dialog)
        self.base_track_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.base_track_label.setObjectName("base_track_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.base_track_label)

        self.base_track_combobox = QtWidgets.QComboBox(Dialog)
        self.base_track_combobox.setObjectName("base_track_combobox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.base_track_combobox)

        self.type_label = QtWidgets.QLabel(Dialog)
        self.type_label.setObjectName("type_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.type_label)

        self.type_combobox = QtWidgets.QComboBox(Dialog)
        self.type_combobox.setObjectName("type_combobox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.type_combobox)

        self.style_label = QtWidgets.QLabel(Dialog)
        self.style_label.setObjectName("style_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.style_label)

        self.style_combobox = QtWidgets.QComboBox(Dialog)
        self.style_combobox.setObjectName("style_combobox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.style_combobox)

        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.name_label)

        self.name_line_edit = QtWidgets.QLineEdit(Dialog)
        self.name_line_edit.setObjectName("name_line_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.name_line_edit)

        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("background: #ffffff;\n"
"max-height: 24;\n"
"font: 75 9pt \"Bahnschrift Light\";\n"
"")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", 'Create new track'))
        self.base_track_label.setText(_translate("Dialog", "Base track"))
        self.type_label.setText(_translate("Dialog", "Type"))
        self.style_label.setText(_translate("Dialog", "Style"))
        self.name_label.setText(_translate("Dialog", "Name"))

        self.type_combobox.addItem("Drums")
        self.type_combobox.addItem("Bass guitar")
        self.style_combobox.addItem("Rock")
        self.style_combobox.addItem("Metal")

        app_icon = QtGui.QIcon()
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(16, 16))
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(24, 24))
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(32, 32))
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(48, 48))
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(256, 256))
        self.setWindowIcon(app_icon)

