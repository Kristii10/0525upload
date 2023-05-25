from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindowCal import Ui_Dialog
import sys




def pic_click(event):
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("你按了圖片")
    message.exec_()
    print(event.x())
    print(event.y())
    print(event.button())
    
def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def press():
    x = ui.num1.text()
    y = ui.num2.text()
    #switch()
    # if ui.checkBox.isChecked():
    #     #x,y=y,x
    #     tmp=x   #演算法對調數字
    #     x=y
    #     y=tmp
    """if not is_float(x) or not is_float(y):
        message = QMessageBox()
        message.setWindowTitle("error")
        message.setInformativeText("請輸入數字")
        message.exec_()
        return
    if ui.radioButton.isChecked():
        ans = float(x)+float(y) 
    """
    # h=ui.comboBox.currentText() 
    # if h=="Chinese":
    #     ui.label.setText("答案是"+str(ans))
    # elif h=="English":
    #     ui.label.setText("The answer is"+str(ans))
    
    if ui.comboBox.currentIndex()==0: #設定中英文，Index是位置，從0開始
        introductionStr="答案是 "
    elif ui.comboBox.currentIndex()==1:
        introductionStr="answer is "
    else:
        introductionStr="answer is"
        #ui.label.setText(introductionStr +str(ans*ui.horizontalSlider.value()/100))
    
    if is_float(x) and is_float(y):
     
        if ui.radioButton.isChecked():
            ans = float(x)+float(y)
        elif ui.radioButton_2.isChecked():
            ans = float(x)-float(y)
        elif ui.radioButton_3.isChecked():
            ans = float(x)*float(y)
        elif ui.radioButton_4.isChecked():
            ans = float(x)/float(y)
        else:
            pass
        ui.label.setText(introductionStr +str(ans*ui.horizontalSlider.value()/100))
    
    else:
        message = QMessageBox()
        message.setWindowTitle("error")
        message.setInformativeText("請輸入數字")
        message.exec_()
    
    
    
    

def slider_change(): #滑動數值
    x=ui.horizontalSlider.value()
    print("change vlaue is "+ str(x))
    ui.progressBar.setValue(x)

def slider_release(): #放開
    message=QMessageBox()  #建立視窗
    message.setWindowTitle("sur")  #視窗左上角的文字
    message.setInformativeText("選擇的數值是"+ str(ui.horizontalSlider.value()))  #視窗跳出的東西
    message.exec_()



   

# def switch():
#     if ui.checkBox.isChecked():
#         tmp=x   #演算法對調數字
#         x=y
#         y=tmp
# def language(): #show string
#     if ui.comboBox=="Chinese":
#         ui.label.setText("答案是"+str(z))
#     elif ui.comboBox=="English":
#         ui.label.setText("The answer is"+str(z))
   
app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)

#用拉桿去控制答案的比例
ui.progressBar.setMaximum(100)
ui.progressBar.setMinimum(0)
 
ui.horizontalSlider.setMaximum(100) 
ui.horizontalSlider.setMinimum(0)
ui.horizontalSlider.valueChanged.connect(slider_change)#滑動時數值變化
ui.horizontalSlider.sliderReleased.connect(slider_release) #放開時

ui.flo.mouseReleaseEvent = pic_click
group1 = QButtonGroup(widge)
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton_2)
group1.addButton(ui.radioButton_3)
group1.addButton(ui.radioButton_4)

ui.radioButton.clicked.connect(press)
ui.radioButton_2.clicked.connect(press)
ui.radioButton_3.clicked.connect(press)
ui.radioButton_4.clicked.connect(press)
ui.pressButton.clicked.connect(press) 
#ui.checkBox.clicked.connect() #只有按下這個要馬上執行動作才要個指令
ui.comboBox.addItems(["Chinese","English"])

widge.show()
sys.exit(app.exec_())