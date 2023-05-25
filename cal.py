from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from fractions import Fraction
from mainwindow_1 import Ui_Dialog
import sys
import time
app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)

ui.lineEdit.setAlignment(Qt.AlignCenter)
ui.lineEdit_2.setAlignment(Qt.AlignCenter)
#ui.lineEdit_3.setAlignment(Qt.AlignCenter)

#______________________________________________________________________________
#______________________________________________________________________________

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
#________________________________________________
"""以下為點選radionbutton直接做加減乘除"""
#________________________________________________
def randio_click():
    x=ui.lineEdit.text()
    y=ui.lineEdit_2.text()
    

    if x.strip() == '' or y.strip() == '':
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setInformativeText("请输入 x 和 y 的值")
        message.exec_()
        return

    if  is_float(x) and is_float(y):
        x=float(ui.lineEdit.text())
        y=float(ui.lineEdit_2.text())
    

    else:
        message=QMessageBox()
        message.setWindowTitle("errorrrrrrrrrrrrrrrrr")
        message.setInformativeText("輸入的 x 或 y 不是一个數字")
        message.exec_()
        return

    if (ui.radioButton.isChecked()) :
        result = x + y
    elif (ui.radioButton_2.isChecked()):
        result = x - y
    elif (ui.radioButton_3.isChecked()) :
        result = x * y
    elif (ui.radioButton_4.isChecked()):
        result = x / y
    else:
        return False

    ui.label.setText(str(result))

#__________________________________________________________________________
"""以下為按下 Add按鈕"""
#__________________________________________________________________________
def perform_operation(x,y):
    if (ui.radioButton.isChecked()) and (is_float(x) or is_float(y)):
        #s=x+y
        ui.label.setText(str(x+y))
        return x+y
    elif (ui.radioButton_2.isChecked()) and (is_float(x) or is_float(y)):
        ui.label.setText(str(x-y))
        return x-y
    elif (ui.radioButton_3.isChecked()) and (is_float(x) or is_float(y)): 
        ui.label.setText(str(x*y))
        return x*y
    elif (ui.radioButton_4.isChecked()) and (is_float(x) or is_float(y)):
        ui.label.setText(str(x/y))
        return x/y
    return False

def clicked_add():

    x=float(ui.lineEdit.text())
    y=float(ui.lineEdit_2.text())
    result=perform_operation(x,y)
    #n=ui.lineEdit_3.text()
    if  result is not None:
        print(result)
        ui.label.setText(str(result))
    else:
        message=QMessageBox()
        message.setWindowTitle("errorrrrrrrrrrrrrrrrr")
        message.setInformativeText("輸入的 x 或 y 不是一个數字")
        message.exec_()

#____________________________________________________
"""如峰老師的 radioButton直接顯示答案"""
#____________________________________________________
def press():
    x=ui.lineEdit.text()
    y=ui.lineEdit_2.text()
    """
    if not is_float(x) or not is_float(y):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setInformativeText("请输入 x 和 y 的值")
        message.exec_()
        return
    if ui.radioButton.isCheckable():
        ans=float(x)+float(y)
    """
    if is_float(x)and is_float(y):
        if ui.radioButton.isChecked():
            ans=float(x)+float(y)
        elif ui.radioButton_2.isChecked():
            ans=float(x)-float(y)
        elif ui.radioButton_3.isChecked():
            ans=float(x)*float(y)
        elif ui.radioButton_4.isChecked():
            ans=float(x)/float(y)
        ui.label.setText(str(ans))
    
#____________________________________________________________________
"""以下為 按下圖片"""
#____________________________________________________________________

def pic_click(event):
    message=QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("你案的圖片")
    message.exec_()
#___________________________________________________________


#___________________________________________________________
"""按下數值對調後 x y 對調做運算"""
#___________________________________________________________
def check_click():
    x=float(ui.lineEdit.text())
    y=float(ui.lineEdit_2.text())
    tmp=x
    x=y
    y=tmp
        
    ui.lineEdit.setText(str(x))
    ui.lineEdit_2.setText(str(y))

    if (ui.radioButton.isChecked()) and (is_float(x) or is_float(y)):
        #s=x+y
        ui.label.setText(str(x+y))
        return x+y
    elif (ui.radioButton_2.isChecked()) and (is_float(x) or is_float(y)):
        ui.label.setText(str(x-y))
        return x-y
    elif (ui.radioButton_3.isChecked()) and (is_float(x) or is_float(y)): 
        ui.label.setText(str(x*y))
        return x*y
    elif (ui.radioButton_4.isChecked()) and (is_float(x) or is_float(y)):
        ui.label.setText(str(x/y))
        return x/y
    return False

def clicked_add():

    x=float(ui.lineEdit.text())
    y=float(ui.lineEdit_2.text())
    result=perform_operation(x,y)
    #n=ui.lineEdit_3.text()
    if  result is not None:
        print(result)
        ui.label.setText(str(result))
    else:
        message=QMessageBox()
        message.setWindowTitle("errorrrrrrrrrrrrrrrrr")
        message.setInformativeText("輸入的 x 或 y 不是一个數字")
        message.exec_()
#____________________________________________________________________
"""變成分子分母 如果是整數就顯示整數"""
#____________________________________________________________________

def chicked_number():
    x=float(ui.lineEdit.text())
    y=float(ui.lineEdit_2.text())
    label_text = ui.label.text()
    values = label_text.split("/")  # 假设文本是分子分母形式，以斜杠分隔
    numerator = x
    denominator = y
    if len(values) == 2:
        try:
            numerator = float(values[0])
            denominator = float(values[1])
        except ValueError:
            pass  # 如果无法转换为浮点数，忽略错误
    
    ui.label_2.setText(f"{numerator}/{denominator}")

    if numerator % denominator==0:
        ui.label_2.setText("答案是整數 "+f"{numerator}/{denominator}")

    
    #numerator, denominator = denominator, numerator  # 对调数值
    #ui.label_2.setText(f"{numerator}/{denominator}")



ui.checkBox_2.clicked.connect(chicked_number)

#______________________________________________________
"""顯示comboBox的文字跟位子"""
#______________________________________________________

def click_comboBox():
    x=ui.lineEdit.text()
    y=ui.lineEdit_2.text()
   
    if is_float(x)and is_float(y):
        if ui.radioButton.isChecked():
            ans=float(x)+float(y)
        elif ui.radioButton_2.isChecked():
            ans=float(x)-float(y)
        elif ui.radioButton_3.isChecked():
            ans=float(x)*float(y)
        elif ui.radioButton_4.isChecked():
            ans=float(x)/float(y)
        ui.label.setText(str(ans))

    if ui.comboBox.currentText()=='英文':
        ui.label.setText("ans is"+str(ans))
    else:
        ui.label.setText("答案"+str(ans))

    #ui.label.setText("hello")

   

    print(ui.comboBox.currentText())
    print(ui.comboBox.currentIndex())
#______________________________________________________

"""直接點選checkbox就改變label內的文字"""
#________________________________________
def checkBox_chang(index):
    x=ui.lineEdit.text()
    y=ui.lineEdit_2.text()
   
    if is_float(x)and is_float(y):
        if ui.radioButton.isChecked():
            ans=float(x)+float(y)
        elif ui.radioButton_2.isChecked():
            ans=float(x)-float(y)
        elif ui.radioButton_3.isChecked():
            ans=float(x)*float(y)
        elif ui.radioButton_4.isChecked():
            ans=float(x)/float(y)
        ui.label.setText(str(ans))

    if index == 0:
        ui.label.setText("ans is " + str(ans))
    elif index == 1:
        ui.label.setText("答案 " + str(ans))

def click_show():
     ui.progressBar.setValue(40)

def slider_change():
    x=ui.horizontalSlider.value()
    ui.progressBar.setValue(x)
    print('change value is'+ str(x))

def slider_realease():
    x=ui.lineEdit.text()
    y=ui.lineEdit_2.text()
   
    if is_float(x)and is_float(y):
        if ui.radioButton.isChecked():
            ans=float(x)+float(y)
        elif ui.radioButton_2.isChecked():
            ans=float(x)-float(y)
        elif ui.radioButton_3.isChecked():
            ans=float(x)*float(y)
        elif ui.radioButton_4.isChecked():
            ans=float(x)/float(y)
        ui.label.setText(str(ans))
    v1=(ans*ui.horizontalSlider.value())/100

    ui.label_4.setText(str(v1)+"%")
    ui.progressBar.setValue(ui.horizontalSlider.value())
    
    v2=ans*v1
    ui.label.setText("比例*ans "+str(v2))
    # message=QMessageBox()
    # message.setWindowTitle("errorrrrrrrrrrrrrrrrr")
    # message.setInformativeText("你選擇的數值是 "+str(ui.horizontalSlider.value()))
    # message.exec_()
#______________________



#____________________________________________
"""按鈕設定"""
#____________________________________________

ui.progressBar.setMaximum(100)
ui.progressBar.setMinimum(0)
ui.progressBar.setValue(0)
ui.horizontalSlider.setMaximum(100)
ui.horizontalSlider.setMinimum(0)
ui.horizontalSlider.valueChanged.connect(slider_change)
ui.horizontalSlider.sliderReleased.connect(slider_realease)


ui.pushButton_3.clicked.connect(click_show)
ui.comboBox.activated.connect(checkBox_chang)
ui.checkBox.clicked.connect(check_click)

ui.pic.mouseReleaseEvent = pic_click

ui.pushButton.clicked.connect(clicked_add)
ui.pushButton_2.clicked.connect(click_comboBox)

ui.radioButton.clicked.connect(randio_click)
ui.radioButton_2.clicked.connect(randio_click)
ui.radioButton_3.clicked.connect(randio_click)
ui.radioButton_4.clicked.connect(randio_click)

ui.radioButton.clicked.connect(press)
ui.radioButton_2.clicked.connect(press)
ui.radioButton_3.clicked.connect(press)
ui.radioButton_4.clicked.connect(press)

ui.comboBox.addItems(["英文","中文"])
#__________________________________________________
"""radioButton group設定"""
#__________________________________________________
group1=QButtonGroup(widge)
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton_2)
group1.addButton(ui.radioButton_3)
group1.addButton(ui.radioButton_4)


widge.show()
sys.exit(app.exec_()) #紀錄成功執行還是失敗
#app.exec_()


#valuey=y.isnumeric() #isnumeric()是否是數字
#valuex=x.isnumeric() #isnumeric()是否是數字
