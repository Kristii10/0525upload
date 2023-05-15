from PyQt5.QtWidgets import* #*是為了一次全部include進來，但最保險的方式是一個一個import
from PyQt5.QtCore import*
from PyQt5.QtGui import*

from mainwindow import Ui_Dialog #把隔壁檔案import進來
import sys

app= QApplication(sys.argv) #argv #qt程式第一行一定要有這個，不然會報錯
#dialog要放到widge裡面
widge= QWidget()
ui=Ui_Dialog()
ui.setupUi(widge)
widge.show()
app.exec_() #執行畫面
