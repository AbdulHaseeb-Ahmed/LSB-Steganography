# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encodewindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PIL import Image
import math
import random

class Ui_EncodeWindow(object):
    def __init__(self, keystring):
        self.keystring = keystring
        print("Key from main window into Encoder: " + keystring)
    def setupUi(self, EncodeWindow):
        EncodeWindow.setObjectName("EncodeWindow")
        EncodeWindow.resize(1246, 646)
        self.gridLayout = QtWidgets.QGridLayout(EncodeWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Titleofwindow = QtWidgets.QLabel(EncodeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Titleofwindow.sizePolicy().hasHeightForWidth())
        self.Titleofwindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.Titleofwindow.setFont(font)
        self.Titleofwindow.setAlignment(QtCore.Qt.AlignCenter)
        self.Titleofwindow.setObjectName("Titleofwindow")
        self.verticalLayout_4.addWidget(self.Titleofwindow)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image_1 = QtWidgets.QLabel(EncodeWindow)
        self.Image_1.setMinimumSize(QtCore.QSize(600, 400))
        self.Image_1.setText("")
        self.Image_1.setPixmap(QtGui.QPixmap("imageopt1.jpeg"))
        self.Image_1.setScaledContents(True)
        self.Image_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Image_1.setObjectName("Image_1")
        self.verticalLayout.addWidget(self.Image_1)
        self.Option_1 = QtWidgets.QRadioButton(EncodeWindow)
        self.Option_1.setObjectName("Option_1")
        self.verticalLayout.addWidget(self.Option_1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Image_2 = QtWidgets.QLabel(EncodeWindow)
        self.Image_2.setMinimumSize(QtCore.QSize(600, 400))
        self.Image_2.setText("")
        self.Image_2.setPixmap(QtGui.QPixmap("imageopt2.jpeg"))
        self.Image_2.setScaledContents(True)
        self.Image_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Image_2.setObjectName("Image_2")
        self.verticalLayout_2.addWidget(self.Image_2)
        self.Option_2 = QtWidgets.QRadioButton(EncodeWindow)
        self.Option_2.setObjectName("Option_2")
        self.verticalLayout_2.addWidget(self.Option_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Message_to_user = QtWidgets.QLabel(EncodeWindow)
        self.Message_to_user.setObjectName("Message_to_user")
        self.verticalLayout_3.addWidget(self.Message_to_user)

        self.Message_input = QtWidgets.QLineEdit(EncodeWindow)
        self.Message_input.setPlaceholderText("Enter message to hide")
        
        self.Message_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Message_input.setAlignment(QtCore.Qt.AlignCenter)
        self.Message_input.setObjectName("Message_input")
        self.verticalLayout_3.addWidget(self.Message_input, 0, QtCore.Qt.AlignVCenter)

        self.Enter_message = QtWidgets.QPushButton(EncodeWindow)
        self.Enter_message.setObjectName("Enter_message")
        self.Enter_message.clicked.connect(lambda: self.show_encodevalidation_popup(self.Option_1.isChecked(), self.Option_2.isChecked()))
        
        self.verticalLayout_3.addWidget(self.Enter_message, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.encodingbutton = QtWidgets.QPushButton(EncodeWindow)
        self.encodingbutton.setObjectName("encodingbutton")
        self.encodingbutton.clicked.connect(lambda: self.show_encodingdone_popup(self.Option_1.isChecked(), self.Option_2.isChecked()))
        
        self.verticalLayout_3.addWidget(self.encodingbutton, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(EncodeWindow)
        QtCore.QMetaObject.connectSlotsByName(EncodeWindow)

    def show_encodevalidation_popup(self, opt1, opt2):
        global image1
        global image2
        image1 = Image.open('Image1.png', 'r')
        image2 = Image.open('Image2.png', 'r')
        image1pixels = list(image1.getdata())
        image2pixels = list(image2.getdata())
        msg = QMessageBox()
        msg.setWindowTitle("Getting Message")
        global secmessage
        global imageoption
        secmessage = self.Message_input.text()
        total_bits = len(secmessage) * 8
        if(opt1 == True):
            if(total_bits < len(image1pixels) and total_bits > 1):
                msg.setText("Your message is: " + self.Message_input.text() + "\n" + "You chose Image 1\n" + "Please press the encode button now!")
                imageoption = image1
            elif(total_bits > len(image1pixels)):
                msg.setText("Your message is: " + self.Message_input.text() + " : will NOT fit in the image!\n" + "Please enter new message!")
            elif(total_bits == 0):
                msg.setText("Please enter a message!")
        elif(opt2 == True):
            if(total_bits < len(image2pixels) and total_bits > 1):
                msg.setText("Your message is: " + self.Message_input.text() + "\n" + "You chose Image 2\n" + "Please press the encode button now!")
                imageoption = image2
            elif(total_bits > len(image2pixels)):
                msg.setText("Your message is: " + self.Message_input.text() + " : will NOT fit in the image!\n" + "Please enter new message!")
            elif(total_bits == 0):
                msg.setText("Please enter a message!")
        elif(total_bits == 0):
            msg.setText("Please enter a message and choose an image!")
        elif((opt1 == False) and (opt2 == False) and total_bits > 1):
            msg.setText("Please choose an image to use!")
        x = msg.exec_()

    def show_encodingdone_popup(self, opt1, opt2):
        msg = QMessageBox()
        msg.setWindowTitle("Encoding Message")
        ordersecmessage = self.Message_input.text()
        print(ordersecmessage)
        
        if((len(ordersecmessage) == 0 or ordersecmessage == None) and (opt1 == False and opt2 == False)):
            msg.setText("Enter a message and chose an image!")
        elif((len(ordersecmessage) == 0 or ordersecmessage == None) and (opt1 == True or opt2 == True)):
            msg.setText("Enter a message!")
        elif((len(ordersecmessage) > 1) and (opt1 == False and opt2 == False)):
            msg.setText("Choose an image!")
        elif((len(secmessage) > 1 or len(ordersecmessage) > 1) and (opt1 == True or opt2 == True)):
            imagepixels = list(imageoption.getdata())
            sec_message_binary = []

            # apply affine cipher encryption
            key = self.keystring
            keyvalues = key.split(", ")
            m = int(keyvalues[0])
            a = int(keyvalues[1])
            b = int(keyvalues[2])
            a_inverse = int(keyvalues[3])
            cipher = []
            for character in secmessage:
                decimal = ord(character)
                enequ = ((a * decimal) + b) % m
                characterval = chr(enequ)
                cipher.append(characterval)
            message = ''.join(cipher)
            
            # changing each charachter in the message to it binary equivalent
            for character in message:
                sec_message_binary.append(format(ord(character), '08b'))
            sec_message_binary.append('00000100')
            print(sec_message_binary)

            # changing all the decimal values of each pixel in the image to its binary equivalent
            bin_pixels = []
            for pixel in range(0, len(imagepixels)):
                List = []
                List.append(format(imagepixels[pixel][0], '08b'))
                List.append(format(imagepixels[pixel][1], '08b'))
                List.append(format(imagepixels[pixel][2], '08b'))
                bin_pixels.append(List)
            print("All the pixels in the image have been converted from decimal to binary vlaues")
            print(bin_pixels[0:9])

            # creating list with a all the bits of the message in a continous fashion
            sec_message_concat = []
            for i in range(0, len(sec_message_binary)):
                for j in range(0, 8):
                    sec_message_concat.append(sec_message_binary[i][j])
            print("All the bits of the secret message concatenated together is: ")
            print(sec_message_concat)

            # number of pixels to change in image
            P2Change = 0
            if(len(sec_message_concat) % 3 != 0):
                P2Change = int(len(sec_message_concat)/3) + 1
            else:
                P2Change = int(len(sec_message_concat)/3)
            print("The number of pixels to change in the image is (each pixel will have 3 changes as there are 3 colors in each pixel rgb): ")
            print(P2Change)

            # before encoding the pixels that will change in binary format
            print("Before encoding the image with the message, the pixel values in binary are:")
            for i in range(0, P2Change):
                print(bin_pixels[i])

            # before encoding the pixels that will change in decimal format
            print("Before encoding the image with the message the pixel values in decimal are:")
            dec_pixels_before = []
            for i in range(0,P2Change):
                dec = []
                dec.append(int(bin_pixels[i][0], 2))
                dec.append(int(bin_pixels[i][1], 2))
                dec.append(int(bin_pixels[i][2], 2))
                dec_pixels_before.append(dec)
            for i in range(0, P2Change):
                print(dec_pixels_before[i])

            # inserting message into image
            bit_index = 7
            index = 0
            for pixel in range(0, P2Change):
                for rgb_index in range(0, 3):
                    if(index == len(sec_message_concat)):
                        break
                    if(bin_pixels[pixel][rgb_index][bit_index] != sec_message_concat[index]):
                        bin_pixels[pixel][rgb_index] = bin_pixels[pixel][rgb_index][:-1] + sec_message_concat[index]
                    index += 1
            print("The pixels have been altered to hold the message!")
            print(bin_pixels[0:16])

            # after encoding the pixels in binary format
            print("After encodning the image with the message the pixel values in binary are:")
            for i in range(0, P2Change):
                print(bin_pixels[i])

            # after encoding the pixels in decimal format
            print("After encoding the image with the message the pixel values in decimal are:")
            dec_pixels_after = []
            for i in range(0, P2Change):
                dec = []
                dec.append(int(bin_pixels[i][0], 2))
                dec.append(int(bin_pixels[i][1], 2))
                dec.append(int(bin_pixels[i][2], 2))
                dec_pixels_after.append(dec)
            for i in range(0, P2Change):
                print(dec_pixels_after[i])

            # creating new pixels for the new stego image
            dec_pixels_after_all = []
            for i in range(0, len(bin_pixels)):
                dec = []
                dec.append(int(bin_pixels[i][0], 2))
                dec.append(int(bin_pixels[i][1], 2))
                dec.append(int(bin_pixels[i][2], 2))
                dec_pixels_after_all.append(tuple(dec))

            # create new stego image
            if(opt1 == True):
                image_out = Image.new(image1.mode, image1.size)
                image_out.putdata(dec_pixels_after_all)
                NewImageName = 'imageopt1stego.png'
                image_out.save(NewImageName)
                NewWinImageName = 'imageopt1stego.jpeg'
                image_out.save(NewWinImageName)
                msg.setText("Encoding is done, the stego image is " + NewWinImageName + " and your message of '" + secmessage + "' has been encrypted to '" + message + "' and has been placed in the image!")
            elif(opt2 == True):
                image_out = Image.new(image2.mode, image2.size)
                image_out.putdata(dec_pixels_after_all)
                NewImageName = 'imageopt2stego.png'
                image_out.save(NewImageName)
                NewWinImageName = 'imageopt2stego.jpeg'
                image_out.save(NewWinImageName)
                msg.setText("Encoding is done, the stego image is " + NewWinImageName + " and your message of '" + secmessage + "' has been encrypted to '" + message + "' and has been placed in the image!")
        x = msg.exec_()
        


    def retranslateUi(self, EncodeWindow):
        _translate = QtCore.QCoreApplication.translate
        EncodeWindow.setWindowTitle(_translate("EncodeWindow", "Dialog"))
        self.Titleofwindow.setText(_translate("EncodeWindow", "     Encode Your Message Into The Image"))
        self.Option_1.setText(_translate("EncodeWindow", "Option 1"))
        self.Option_2.setText(_translate("EncodeWindow", "Option 2"))
        self.Message_to_user.setText(_translate("EncodeWindow", "Enter Secret Message in Text Box Below First:"))
        self.Enter_message.setText(_translate("EncodeWindow", "Enter Message"))
        self.encodingbutton.setText(_translate("EncodeWindow", "Encode Message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EncodeWindow = QtWidgets.QDialog()
    ui = Ui_EncodeWindow()
    ui.setupUi(EncodeWindow)
    EncodeWindow.show()
    sys.exit(app.exec_())

