#匯入套件
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# * 代表會入模組內的所有東西

from plus_test_mainwindow import Ui_Dialog    #從mainwindow.py裡的東西import過來
import sys


"""
def clicked_add():
    x = ui.lineEdit_left.text()    #抓取在使用者輸入的地方所輸入的東西，並轉成字串
    y = ui.lineEdit_right.text()
    try:
        x = float(x)
        y = float(y)
        z = x + y
        ui.ans.setText(str(z))
    except:
        message = QMessageBox()    #這東西會產生一個小視窗(EX:輸入錯誤會彈出 顯示錯誤 的視窗)
        message.setWindowTitle("ERROR")    #設定跳出來的視窗左上角的視窗標題
        message.setInformativeText("輸入有誤，請重新輸入")    #設定跳出來的視窗顯示的內文
        message.exec_()
"""


def clicked_add():
    x = ui.lineEdit_left.text()    #抓取在使用者輸入的地方所輸入的東西，並轉成字串
    y = ui.lineEdit_right.text()
    if x.isnumeric() == True and y.isnumeric() == True:    #isnumeric() 方法检测字符串是否只由数字组成，如果字符串中只包含数字字符，则返回 True，否则返回 False。
            x = float(x)
            y = float(y)
            z = x + y
            ui.ans.setText(str(z))  
    else:
        message = QMessageBox()    #這東西會產生一個小視窗(EX:輸入錯誤會彈出 顯示錯誤 的視窗)
        message.setWindowTitle("ERROR")    #設定跳出來的視窗左上角的視窗標題
        message.setInformativeText("輸入有誤，請重新輸入")    #設定跳出來的視窗顯示的內文
        message.exec_()

app = QApplication(sys.argv)    #QT的程式第一行一定要有這個，固定格式

#要把Dialog放到widge裡面
#先生成一個widge
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)


ui.addButtom.clicked.connect(clicked_add)    #連結.ui裡面的按鈕  >>>  意思是當我點擊PressMeButtom按鈕的時候，要連結到我設定的程式(function)
#connect是一個連結function用的function


widge.show()
sys.exit(app.exec_())     #結束介面之後，會回傳關閉成功還失敗
#以上都是固定用法