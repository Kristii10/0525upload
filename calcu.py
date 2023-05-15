from PyQt5.QtWidgets import* #*是為了一次全部include進來，但最保險的方式是一個一個import
from PyQt5.QtCore import*
from PyQt5.QtGui import*

from mainwindow import Ui_Dialog #把隔壁檔案import進來
import sys

def clicked_add():
    x=ui.num1.text()
    y=ui.num2.text()
    if x.isnumeric()== True:


    z=int(x)+int(y)
    message=QMessageBox()
    message.setWindowTitle("result")  #左上角
    message.setInformativeText(str(z))
    message.exec_()



app= QApplication(sys.argv) #argv #qt程式第一行一定要有這個，不然會報錯
#dialog要放到widge裡面
widge= QWidget()
ui=Ui_Dialog()
ui.setupUi(widge)

ui.addButton.clicked.connect(clicked_add) #藍字是object name

widge.show()
app.exec_()
sys.exit(app.exec_()) #成功結束或是失敗執行結束？
