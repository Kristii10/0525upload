from PyQt5.QtWidgets import* #*是為了一次全部include進來，但最保險的方式是一個一個import
from PyQt5.QtCore import*
from PyQt5.QtGui import*

from mainwindow import Ui_Dialog #把隔壁檔案import進來
import sys
def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def clicked_add():  #相加的計算機，button的功能
    text1=ui.lineEdit_2.text() #lineEdit是string格式，因為要相加，所要要轉成數值
    text2=ui.lineEdit_3.text()
    if is_float(text1)and is_float(text2): #is_float是用來確認數值
  
        var1 =float(text1) #string變成float
        var2 =float(text2)
        ui.label.setText(str(var1+var2)) #labe會產生出相加後答案
    else:
        message= QMessageBox()
        message.setWindowTitle("error")  #左上角 #mac跑不出來
        message.setInformativeText("輸入錯誤，請再輸入一次")
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
