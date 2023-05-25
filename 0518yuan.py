#匯入套件
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# * 代表會入模組內的所有東西

from little_computer_0517_mainwindow import Ui_Dialog    #從mainwindow.py裡的東西import過來
import sys


def show_error_box():
    message = QMessageBox()    #這東西會產生一個小視窗(EX:輸入錯誤會彈出 顯示錯誤 的視窗)
    message.setWindowTitle("ERROR")    #設定跳出來的視窗左上角的視窗標題
    message.setInformativeText("輸入有誤，請重新輸入")    #設定跳出來的視窗顯示的內文
    message.exec_()


x=""
y=""

def try_get():
    global x
    global y
    try:
        x = ui.lineEdit_left.text()    #抓取在使用者輸入的地方所輸入的東西，並轉成字串
        y = ui.lineEdit_right.text()
        x = float(x)    #抓取在使用者輸入的地方所輸入的東西，並轉成字串
        y = float(y)
        return True
    except:
        show_error_box()
        return False

"""
def set_add():
    global x
    global y
    if try_get() == True:
        z = x + y
        ui.ans.setText(str(z))


def set_minus():
    global x
    global y
    if try_get() == True:
        z = x - y
        ui.ans.setText(str(z))


def set_multi():
    global x
    global y
    if try_get() == True:
        z = x * y
        ui.ans.setText(str(z))


def set_divid():
    global x
    global y
    if try_get() == True:
        try:
            z = x / y
            ui.ans.setText(str(z))
        except:
            show_error_box()
"""


def check_change():
    global x
    global y
    if ui.change_box.isChecked() == True:
        tmp = x
        x = y
        y = tmp
        #也可以這樣寫  x,y = y,x


def check_combobox():
    combo_text = ui.comboBox.currentText()
    if combo_text == "中文":
        return "答案是 : "
    else:
        return "answer is : "

def change_start(i):
    if i == 0:
        ui.ans.setText("-- 開始 --")
    else:
        ui.ans.setText("-- START --")

def clicked_enter():
    global x
    global y
    if try_get() == True:
        check_change()
        if ui.plus.isChecked():
            z = x + y
            ui.ans.setText(check_combobox()+str(z))   
        elif ui.minus.isChecked():
            z = x - y
            ui.ans.setText(check_combobox()+str(z))
        elif ui.multi.isChecked():
            z = x * y
            ui.ans.setText(check_combobox()+str(z))
        elif ui.divid.isChecked():
            try:
                z = x / y
                ui.ans.setText(check_combobox()+str(z))
            except:
                show_error_box()
        else:
            show_error_box()



app = QApplication(sys.argv)    #QT的程式第一行一定要有這個，固定格式

#要把Dialog放到widge裡面
#先生成一個widge
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)


ui.addButtom.clicked.connect(clicked_enter)    #連結.ui裡面的按鈕  >>>  意思是當我點擊PressMeButtom按鈕的時候，要連結到我設定的程式(function)
#connect是一個連結function用的function

group1 = QButtonGroup(widge)
group1.addButton(ui.plus)
group1.addButton(ui.minus)
group1.addButton(ui.multi)
group1.addButton(ui.divid)


ui.plus.clicked.connect(clicked_enter)
ui.minus.clicked.connect(clicked_enter)
ui.multi.clicked.connect(clicked_enter)
ui.divid.clicked.connect(clicked_enter)

"""
ui.plus.clicked.connect(set_add)
ui.minus.clicked.connect(set_minus)
ui.multi.clicked.connect(set_multi)
ui.divid.clicked.connect(set_divid)
"""

#設定下拉式選單內容
ui.comboBox.addItems(["中文","英文"])
#下拉式選單選取時也能連結function
ui.comboBox.activated.connect(change_start)


widge.show()
sys.exit(app.exec_())     #結束介面之後，會回傳關閉成功還失敗
#以上都是固定用法
