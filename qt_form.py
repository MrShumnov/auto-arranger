import sys
import form as design
from PyQt5 import QtWidgets, QtCore, QtGui
import resources_cs
import drum_dialog
import tab_files as tf
import drum_data
import guitarpro
import bass_data


class Dialog(QtWidgets.QDialog, drum_dialog.Ui_Dialog):
    def __init__(self, guitarTracks):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.name_line_edit.setText('NewTrack')

        for i in guitarTracks:
            self.base_track_combobox.addItem(i.name)

        self.buttonBox.accepted.connect(self.Ok)

    def Ok(self):
        self.flag = True


class GuitarTrack(QtWidgets.QGroupBox):
    def __init__(self, name, parent=None):
        QtWidgets.QGroupBox.__init__(self, parent=parent)
        self.name = name
        self.setMinimumSize(QtCore.QSize(400, 50))
        self.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setTitle("")
        self.setFlat(True)

        horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        horizontalLayout_2.setSpacing(11)
        horizontalLayout_2.setObjectName("horizontalLayout_2")

        GuitarTrack_icon = QtWidgets.QPushButton(self)
        GuitarTrack_icon.setMaximumSize(QtCore.QSize(40, 40))
        GuitarTrack_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/гитара бел.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GuitarTrack_icon.setIcon(icon)
        GuitarTrack_icon.setIconSize(QtCore.QSize(40, 40))
        GuitarTrack_icon.setFlat(True)
        GuitarTrack_icon.setObjectName(name + "_icon")
        horizontalLayout_2.addWidget(GuitarTrack_icon)

        GuitarTrack_name = QtWidgets.QLabel(self)
        GuitarTrack_name.setText(name)
        GuitarTrack_name.setObjectName(name + "_name")
        horizontalLayout_2.addWidget(GuitarTrack_name)

        self.layout().setContentsMargins(0, 0, 0, 0)


class NewTrack(QtWidgets.QGroupBox):
    def __init__(self, name, baseTrack, type, parent=None):
        QtWidgets.QGroupBox.__init__(self, parent=parent)
        self.name = name
        self.baseTrack = baseTrack
        self.setMinimumSize(QtCore.QSize(400, 50))
        self.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setTitle("")
        self.setFlat(True)
        # self.setObjectName(name)

        horizontalLayout_3 = QtWidgets.QHBoxLayout(self)
        horizontalLayout_3.setSpacing(11)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.layout().setContentsMargins(10, 0, 0, 0)
        DrumTrack_icon = QtWidgets.QPushButton(self)
        DrumTrack_icon.setMaximumSize(QtCore.QSize(40, 40))
        DrumTrack_icon.setText("")
        icon1 = QtGui.QIcon()
        if type == 0:
            icon1.addPixmap(QtGui.QPixmap(":/newPrefix/барабаны.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon1.addPixmap(QtGui.QPixmap(":/newPrefix/бас бел.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DrumTrack_icon.setIcon(icon1)
        DrumTrack_icon.setIconSize(QtCore.QSize(40, 40))
        DrumTrack_icon.setFlat(True)
        DrumTrack_icon.setObjectName(name + "_icon")
        horizontalLayout_3.addWidget(DrumTrack_icon)

        DrumTrack_name = QtWidgets.QLabel(self)
        DrumTrack_name.setObjectName(name + "_name")
        DrumTrack_name.setText(name)
        horizontalLayout_3.addWidget(DrumTrack_name)

        #DrumTrack_style = QtWidgets.QComboBox(self)
        #DrumTrack_style.setMinimumSize(QtCore.QSize(100, 0))
        #DrumTrack_style.setMaximumSize(QtCore.QSize(200, 16777215))
        #DrumTrack_style.setLayoutDirection(QtCore.Qt.LeftToRight)
        #DrumTrack_style.setObjectName(name + "_style")
        #DrumTrack_style.addItem("Rock")
        #DrumTrack_style.addItem("Metal")
        #horizontalLayout_3.addWidget(DrumTrack_style)


class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.guitarTracksList = []
        self.drumTracksList = []
        self.bassTracksList = []
        self.fname = ''
        self.AddTrack.layout().setContentsMargins(0, 0, 0, 0)

        self.action_2.triggered.connect(self.open_file)
        self.action_3.triggered.connect(self.save_file)
        self.AddTrack_button.clicked.connect(self.add_track)

        self.AddTrack.close()

        app_icon = QtGui.QIcon()
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(16, 16))
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(24, 24))
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(32, 32))
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(48, 48))
        app_icon.addFile(':/newPrefix/icon.png', QtCore.QSize(256, 256))
        self.setWindowIcon(app_icon)

    def add_track(self):
        drum_param = Dialog(self.guitarTracksList)
        drum_param.exec_()

        if drum_param.flag:
            nt = NewTrack(drum_param.name_line_edit.text(), drum_param.base_track_combobox.currentIndex(), drum_param.type_combobox.currentIndex())
            if drum_param.type_combobox.currentIndex() == 0:
                self.drumTracksList.append(nt)
            else:
                self.bassTracksList.append(nt)
            self.DrumTracks.insertWidget(len(self.drumTracksList) + len(self.bassTracksList) - 1, nt)

        # print('Yes!')

    def save_file(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file', 'c:\\', "GuitarPro files (*.gp3 *.gp4 *.gp5)")

        if fname[0] != '':
            guitars = []
            tab1 = guitarpro.parse(self.path)
            for i in self.guitarTracksList:
                for j in tab1.tracks:
                    if i.name == j.name:
                        guitars.append(j)

            tab = guitarpro.models.Song()
            tab.tempo = guitars[0].song.tempo
            tab.version = 'FICHIER GUITAR PRO v3.00'
            tab.tracks = guitars
            nnd = Neural_network_drums.NeuralNetwork('weights/rock_drums.h5')
            nnb = Neural_network_bass.NeuralNetwork('weights/rock_bass.h5')
            for i in self.drumTracksList:
                predict = nnd.Predict(self.Tab.guitarTracks[i.baseTrack])
                drum_data.addTrack(guitars[0], predict, i.name, tab)
            for i in self.bassTracksList:
                predict, first_string, key, mm = nnb.Predict(self.Tab.guitarTracks[i.baseTrack], self.path)
                bass_data.addTrack(guitars[0], predict, i.name, tab, first_string, key, mm)

            guitarpro.write(tab, fname[0])

    def open_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "GuitarPro files (*.gp3 *.gp4 *.gp5)")

        if fname[0] != '':
            self.AddTrack.show()
            for i in self.guitarTracksList:
                self.GuitarTracks.removeWidget(i)
                i.deleteLater()
            self.guitarTracksList = []

            for i in self.drumTracksList:
                self.DrumTracks.removeWidget(i)
                i.deleteLater()
            self.drumTracksList = []

            for i in self.bassTracksList:
                self.DrumTracks.removeWidget(i)
                i.deleteLater()
            self.bassTracksList = []

            tab = tf.Tab(fname[0])
            for i in tab.guitarTracks:
                ngt = GuitarTrack(i.name)
                self.guitarTracksList.append(ngt)
                self.GuitarTracks.insertWidget(len(self.guitarTracksList) - 1, ngt)

            self.Tab = tab
            self.path = fname[0]
        # print('open file!')


app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
splash_pix = QtGui.QPixmap(':/newPrefix/icon.png')
splash = QtWidgets.QSplashScreen(splash_pix)
splash.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
splash.setMask(splash_pix.mask())
splash.show()

import Neural_network_drums
import Neural_network_bass
app.processEvents()

window = MainApp()
window.show()
splash.close()
app.exec_()
