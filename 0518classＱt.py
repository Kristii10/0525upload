from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

from mainwindow import Ui_Dialog #把隔壁檔案import進來
import sys

class Mywindow(QMainWindow):
    def __init__(self): #設定初始值
        super().__init__() #super：呼叫副類別的init的執行動作＃super在java很常見
        self.ui=Ui_Dialog() 
        self.ui.setupUi(self) #要放在ＱＭainwindow裡，所以用self, instead of widge
    
        self.group1= QButtonGroup(self)
        group1.addButton(ui.radioButton)
        group1.addButton(ui.radioButton_2)
        group1.addButton(ui.radioButton_3)
        group1.addButton(ui.radioButton_4)


        self.ui.pressMeButton.clicked.connect(clicked_press_me) #從這段開始修改，才是重點#當我點下去就會跟某個define相連
        self.ui.helloButton.clicked.connect(clicked_hello) 
        
    
    
    
    
    def clicked_hello(self): #變成class裡面的def
        print("hello") 
        message=QMessageBox()  #建立視窗
        message.setWindowTitle("sur")  #視窗左上角的文字
        message.setInformativeText(x) 
        
    def clicked_press_me():
        ui.lineEdit_2.text() #以string讀取輸入line edit的x
    #視窗跳出的東西
    message.exec_()

if __name__=="__main__":   #GUI=UI=HMI
    app=QApplication(sys.argv)
    myWindow= Mywindow()
    myWindow.show()
    sys.exit(app.exec_())


if a and b and c and d and e and f and g:
