# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decodewindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
from PIL import Image
import math
import random

class Ui_DecodeWindow(object):
    def __init__(self, keystring):
        self.keystring = keystring
        print("Key from main window into Decoder: " + keystring)
    def setupUi(self, DecodeWindow):
        DecodeWindow.setObjectName("DecodeWindow")
        DecodeWindow.resize(1200, 750)
        self.gridLayout = QtWidgets.QGridLayout(DecodeWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.title = QtWidgets.QLabel(DecodeWindow)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_5.addWidget(self.title)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_org = QtWidgets.QLabel(DecodeWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_org.setFont(font)
        self.label_org.setObjectName("label_org")
        self.horizontalLayout_3.addWidget(self.label_org, 0, QtCore.Qt.AlignHCenter)
        self.label_stego = QtWidgets.QLabel(DecodeWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_stego.setFont(font)
        self.label_stego.setObjectName("label_stego")
        self.horizontalLayout_3.addWidget(self.label_stego, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.org_image = QtWidgets.QLabel(DecodeWindow)
        self.org_image.setText("")
        self.org_image.setScaledContents(True)
        self.org_image.setObjectName("org_image")
        self.verticalLayout_2.addWidget(self.org_image)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.stego_image = QtWidgets.QLabel(DecodeWindow)
        self.stego_image.setText("")
        self.stego_image.setScaledContents(True)
        self.stego_image.setObjectName("stego_image")
        self.verticalLayout_6.addWidget(self.stego_image)

        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.messagetouser = QtWidgets.QLabel(DecodeWindow)
        self.messagetouser.setMaximumSize(QtCore.QSize(16777215, 30))
        self.messagetouser.setObjectName("messagetouser")
        self.verticalLayout_4.addWidget(self.messagetouser)
        self.lineEdit = QtWidgets.QLineEdit(DecodeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit, 0, QtCore.Qt.AlignVCenter)
        self.validimagebutton = QtWidgets.QPushButton(DecodeWindow)
        self.validimagebutton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.validimagebutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.validimagebutton.setObjectName("validimagebutton")
        self.validimagebutton.clicked.connect(self.validImage)

        self.verticalLayout_4.addWidget(self.validimagebutton, 0, QtCore.Qt.AlignHCenter)
        self.decodebutton = QtWidgets.QPushButton(DecodeWindow)
        self.decodebutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.decodebutton.setObjectName("decodebutton")
        self.decodebutton.clicked.connect(self.getImageandMess)

        self.verticalLayout_4.addWidget(self.decodebutton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(DecodeWindow)
        QtCore.QMetaObject.connectSlotsByName(DecodeWindow)

    def validImage(self):
        msg = QMessageBox()
        msg.setWindowTitle("Getting Image")
        global message
        message = self.lineEdit.text()
        if (os.path.exists(message) and "1stego.jpeg" in message):
            self.org_image.setPixmap(QtGui.QPixmap("imageopt1.jpeg"))
            self.stego_image.setPixmap(QtGui.QPixmap("imageopt1stego.jpeg"))

            self.org_image.show()
            self.stego_image.show()
        elif (os.path.exists(message) and "2stego.jpeg" in message):
            self.org_image.setPixmap(QtGui.QPixmap("imageopt2.jpeg"))
            self.stego_image.setPixmap(QtGui.QPixmap("imageopt2stego.jpeg"))

            self.org_image.show()
            self.stego_image.show()
        elif (message == None or len(message) == 0 or "1stego.jpeg" not in message or "2stego.jpeg" not in message):
            msg = QMessageBox()
            msg.setWindowTitle("Getting Message")
            msg.setText("Must enter a valid image name!")
            x = msg.exec_()
        else:
            msg.setText("No such image in folder!")
            x = msg.exec_()

    def getImageandMess(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        if ("1stego.jpeg" in message):
            image1 = Image.open('imageopt1stego.png', 'r')
            image1pixels = list(image1.getdata())
            # binary pixel values to decimal values
            bin_pixels = []
            for pixel in range(0, len(image1pixels)):
                List = []
                List.append(format(image1pixels[pixel][0], '08b'))
                List.append(format(image1pixels[pixel][1], '08b'))
                List.append(format(image1pixels[pixel][2], '08b'))
                bin_pixels.append(List)

            # extract message
            secret_message_bits = []
            for i in range(0, 100):
                for j in range(0, 3):
                    secret_message_bits.append(bin_pixels[i][j][7])
            secret_message_binary = []
            index = 0
            pixel_val = []
            for i in range(0, len(secret_message_bits)):
                pixel_val.append(secret_message_bits[i])
                index += 1
                if (index == 8):
                    result = "".join(pixel_val)
                    secret_message_binary.append(result)
                    index = 0
                    pixel_val.clear()
            secret_message_decimal = []
            for i in range(0, len(secret_message_binary)):
                secret_message_decimal.append(int(secret_message_binary[i], 2))
            secret_message_ASCII = []
            for i in range(0, len(secret_message_decimal)):
                asciichar = chr(int(secret_message_decimal[i]))
                if (int(secret_message_decimal[i]) == 4):
                    break
                else:
                    secret_message_ASCII.append(asciichar)
            plaintext_message = "".join(secret_message_ASCII)

            # apply affine cipher decryption
            key = self.keystring
            keyvalues = key.split(", ")
            m = int(keyvalues[0])
            a = int(keyvalues[1])
            b = int(keyvalues[2])
            a_inverse = int(keyvalues[3])
            englishtext = []
            for character in plaintext_message:
                decimal = ord(character)
                deequ = (a_inverse * (decimal - b)) % m
                characterval = chr(deequ)
                englishtext.append(characterval)
            plaintext = ''.join(englishtext)
            msg.setText("The secret message hidden in the image was: '" + plaintext + "' which was encrypted as '" + plaintext_message + "'")
        elif ("2stego.jpeg" in message):
            image2 = Image.open('imageopt2stego.png', 'r')
            image2pixels = list(image2.getdata())
            # binary pixel values to decimal values
            bin_pixels = []
            for pixel in range(0, len(image2pixels)):
                List = []
                List.append(format(image2pixels[pixel][0], '08b'))
                List.append(format(image2pixels[pixel][1], '08b'))
                List.append(format(image2pixels[pixel][2], '08b'))
                bin_pixels.append(List)

            # extract message
            secret_message_bits = []
            for i in range(0, 100):
                for j in range(0, 3):
                    secret_message_bits.append(bin_pixels[i][j][7])
            secret_message_binary = []
            index = 0
            pixel_val = []
            for i in range(0, len(secret_message_bits)):
                pixel_val.append(secret_message_bits[i])
                index += 1
                if (index == 8):
                    result = "".join(pixel_val)
                    secret_message_binary.append(result)
                    index = 0
                    pixel_val.clear()
            secret_message_decimal = []
            for i in range(0, len(secret_message_binary)):
                secret_message_decimal.append(int(secret_message_binary[i], 2))
            secret_message_ASCII = []
            for i in range(0, len(secret_message_decimal)):
                asciichar = chr(int(secret_message_decimal[i]))
                if (int(secret_message_decimal[i]) == 4):
                    break
                else:
                    secret_message_ASCII.append(asciichar)
            plaintext_message = "".join(secret_message_ASCII)
            
            # apply affine cipher decryption
            key = self.keystring
            keyvalues = key.split(", ")
            m = int(keyvalues[0])
            a = int(keyvalues[1])
            b = int(keyvalues[2])
            a_inverse = int(keyvalues[3])
            englishtext = []
            for character in plaintext_message:
                decimal = ord(character)
                deequ = (a_inverse * (decimal - b)) % m
                characterval = chr(deequ)
                englishtext.append(characterval)
            plaintext = ''.join(englishtext)
            msg.setText("The secret message hidden in the image was: '" + plaintext + "' which was encrypted as '" + plaintext_message + "'")
        else:
            msg.setText("Must first enter image name!")
        x = msg.exec_()

    def retranslateUi(self, DecodeWindow):
        _translate = QtCore.QCoreApplication.translate
        DecodeWindow.setWindowTitle(_translate("DecodeWindow", "Dialog"))
        self.title.setText(_translate("DecodeWindow", "Decode Image To Get Your Message"))
        self.label_org.setText(_translate("DecodeWindow", "Original Image"))
        self.label_stego.setText(_translate("DecodeWindow", "Stego Image"))
        self.messagetouser.setText(_translate("DecodeWindow", "Enter Image Name in Text Box Below First:"))
        self.validimagebutton.setText(_translate("DecodeWindow", "Find Image"))
        self.decodebutton.setText(_translate("DecodeWindow", "Decode"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DecodeWindow = QtWidgets.QDialog()
    ui = Ui_DecodeWindow()
    ui.setupUi(DecodeWindow)
    DecodeWindow.show()
    sys.exit(app.exec_())

