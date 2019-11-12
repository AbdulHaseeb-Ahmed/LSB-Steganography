# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from encodewindow import Ui_EncodeWindow
from decodewindow import Ui_DecodeWindow
import math
import random

class Ui_MainWindow(object):
    def openEncodeWindow(self):
        self.window = QtWidgets.QDialog()
        m = 128
        a_val = False
        a = 0
        while(a_val == False):
            a = random.randint(0, m)
            if(math.gcd(a,m) == 1):
                a_val = True
        b = random.randint(0, m - 1)
        a_inverse = 0
        for i in range(0, m):
            if(i * a % m == 1):
                a_inverse = i
                break
        global key
        key = []
        key.append(m)
        key.append(a)
        key.append(b)
        key.append(a_inverse)
        self.keystring = str(key)
        self.ui = Ui_EncodeWindow(self.keystring[1:-1])
        self.ui.setupUi(self.window)
        self.window.show()

    def openDecodeWindow(self):
        self.window = QtWidgets.QDialog()
        self.keystring = str(key)
        self.ui = Ui_DecodeWindow(self.keystring[1:-1])
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Welcome = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(49)
        self.Welcome.setFont(font)
        self.Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome.setObjectName("Welcome")
        self.verticalLayout_2.addWidget(self.Welcome)
        self.label_mainimage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mainimage.sizePolicy().hasHeightForWidth())
        self.label_mainimage.setSizePolicy(sizePolicy)
        self.label_mainimage.setText("")
        self.label_mainimage.setPixmap(QtGui.QPixmap("MainImage.jpeg"))
        self.label_mainimage.setScaledContents(True)
        self.label_mainimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mainimage.setObjectName("label_mainimage")
        self.verticalLayout_2.addWidget(self.label_mainimage)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Encode = QtWidgets.QPushButton(self.centralwidget)
        self.Encode.setObjectName("Encode")
        self.Encode.clicked.connect(self.openEncodeWindow)
        
        self.horizontalLayout.addWidget(self.Encode)
        self.Decode = QtWidgets.QPushButton(self.centralwidget)
        self.Decode.setObjectName("Decode")
        self.Decode.clicked.connect(self.openDecodeWindow)
        
        self.horizontalLayout.addWidget(self.Decode)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Welcome.setText(_translate("MainWindow", "Welcome to LSB Stegonagraphy"))
        self.Encode.setText(_translate("MainWindow", "Encode"))
        self.Decode.setText(_translate("MainWindow", "Decode"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

