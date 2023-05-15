from PyQt5.QtWidgets import* #*是為了一次全部include進來，但最保險的方式是一個一個import
from PyQt5.QtCore import*
from PyQt5.QtGui import*

from mainwindow11 import Ui_Dialog #把隔壁檔案import進來
import sys

def clicked_press_me():
    x=ui.lineEdit_2.text() #以string讀取輸入line edit的x
    message=QMessageBox()  #建立視窗
    message.setWindowTitle("sur")  #視窗左上角的文字
    message.setInformativeText(x)
    message.exec_()

def clicked_hello(): #按show string按鈕會在label出現hello
    ui.label.setText("hello") 
    print("hello")

app= QApplication(sys.argv) #argv #qt程式第一行一定要有這個，不然會報錯
#dialog要放到widge裡面
widge= QWidget()
ui=Ui_Dialog()
ui.setupUi(widge)

ui.pressMeButton.clicked.connect(clicked_press_me) #藍字是object name
ui.helloButton.clicked.connect(clicked_hello) #藍字是object name
widge.show()
app.exec_()
sys.exit(app.exec_()) #成功結束或是失敗執行結束？