# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 347)
        Dialog.setStyleSheet("background-color: rgb(237, 204, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.pressButton = QtWidgets.QPushButton(Dialog)
        self.pressButton.setGeometry(QtCore.QRect(180, 220, 113, 32))
        self.pressButton.setObjectName("pressButton")
        self.num1 = QtWidgets.QLineEdit(Dialog)
        self.num1.setGeometry(QtCore.QRect(80, 140, 113, 21))
        self.num1.setStyleSheet("color: rgb(10, 10, 10);")
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QLineEdit(Dialog)
        self.num2.setGeometry(QtCore.QRect(250, 140, 113, 21))
        self.num2.setStyleSheet("color: rgb(6, 6, 6);")
        self.num2.setObjectName("num2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 60, 101, 16))
        self.label.setStyleSheet("font: italic 18pt \"Gill Sans\";")
        self.label.setObjectName("label")
        self.flo = QtWidgets.QLabel(Dialog)
        self.flo.setGeometry(QtCore.QRect(10, -10, 91, 131))
        self.flo.setText("")
        self.flo.setPixmap(QtGui.QPixmap("blueflower.webp"))
        self.flo.setScaledContents(True)
        self.flo.setObjectName("flo")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(100, 180, 100, 20))
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 180, 100, 20))
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 180, 100, 20))
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(220, 180, 100, 20))
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(340, 70, 87, 20))
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(320, 20, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(180, 100, 118, 23))
        self.progressBar.setStyleSheet("background-color: rgb(255, 234, 237);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(150, 280, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(390, 130, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pressButton.setText(_translate("Dialog", "press"))
        self.label.setText(_translate("Dialog", "Result"))
        self.radioButton.setText(_translate("Dialog", "+"))
        self.radioButton_2.setText(_translate("Dialog", "-"))
        self.radioButton_3.setText(_translate("Dialog", "*"))
        self.radioButton_4.setText(_translate("Dialog", "/"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())