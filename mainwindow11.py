# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogFirst.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: rgb(255, 201, 214);")
        self.pressMeButton = QtWidgets.QPushButton(Dialog)
        self.pressMeButton.setGeometry(QtCore.QRect(230, 160, 113, 32))
        self.pressMeButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pressMeButton.setStyleSheet("background-color: rgb(130, 135, 139);\n"
"font: 11pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 255, 255);")
        self.pressMeButton.setObjectName("pressMeButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 70, 151, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \".AppleSystemUIFont\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.helloButton = QtWidgets.QPushButton(Dialog)
        self.helloButton.setGeometry(QtCore.QRect(50, 160, 113, 32))
        self.helloButton.setStyleSheet("background-color: rgb(130, 135, 139);\n"
"font: 11pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 255, 255);")
        self.helloButton.setObjectName("helloButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 120, 113, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(12, 12, 12);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 60, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pressMeButton.setText(_translate("Dialog", "press me"))
        self.label.setText(_translate("Dialog", "please enter value"))
        self.helloButton.setText(_translate("Dialog", "show string"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
