from PyQt5.QtWidgets import* #*是為了一次全部include進來，但最保險的方式是一個一個import
from PyQt5.QtCore import*
from PyQt5.QtGui import*

from mainwindowCal import Ui_Dialog #把隔壁檔案import進來
import sys

def pic_click(event):
    message=QMessageBox()  #建立視窗
    message.setWindowTitle("error")  #視窗左上角的文字
    message.setInformativeText("You clicked on the wrong place")  #視窗跳出的東西
    message.exec_()
    print(event.x())  #點擊位置的x軸
    print(event.y())  #點擊位置的y軸
    print(event.button()) #左鍵1,右鍵2,滾輪4，因為是二進位1,10,100
    

# #def click_add(z):  #相加的計算機
#     x=ui.num1.text()   #line.edit
#     y=ui.num2.text()
  
    
    def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
    def press():
        x=ui.num1.text()   #line.edit
        y=ui.num2.text()
        # #if not is_float(x) or not is_float(y): #反邏輯
        #     message=QMessageBox()  #建立視窗
        #     message.setWindowTitle("error")  #視窗左上角的文字
        #     message.setInformativeText("請輸入數字")  #視窗跳出的東西
        #     message.exec_()
        #     return
        if ui.radioButton.isChecked():
            z=float(x)+float(y)
         
        elif ui.radioButton_2.isChecked():
            z=float(x)-float(y)
         
        elif ui.radioButton_3.isChecked():
            z=float(x)*float(y)
           
        elif ui.radioButton_4.isChecked():
            z=float(x)/float(y)
        ui.label.setText(str(z))



    # if x.isnumeric() == True and y.isnumeric() == True:  
    #     z= float(x)+float(y)
    #     ui.label.setText(str(z)) #label會產生出相加後答案
    # else:
    #     message= QMessageBox()
    #     message.setWindowTitle("error")  #左上角 #mac跑不出來
    #     message.setInformativeText("輸入錯誤，請再輸入一次")
    #     message.exec_()

# def click_radio():
#     x=ui.num1.text()   #line.edit
#     y=ui.num2.text()
#     if ui.radioButton.isChecked():
#         z=float(x)+float(y)
#         ui.label.setText(str(z)) 
#     elif ui.radioButton_2.isChecked():
#         z=float(x)-float(y)
#         ui.label.setText(str(z))
#     elif ui.radioButton_3.isChecked():
#         z=float(x)*float(y)
#         ui.label.setText(str(z))
#     elif ui.radioButton_4.isChecked():
#         z=float(x)/float(y)
#         ui.label.setText(str(z))
#     else: 
#         print("error")
    
   
app= QApplication(sys.argv) #argv #qt程式第一行一定要有這個，不然會報錯
#dialog要放到widge裡面
widge= QWidget()
ui=Ui_Dialog()
ui.setupUi(widge)

ui.pressButton.clicked.connect(click_add) #藍字是object name
ui.flo.mouseReleaseEvent=pic_click  #點擊圖片的設置

group1=QButtonGroup(widge)
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton_2)
group1.addButton(ui.radioButton_3)
group1.addButton(ui.radioButton_4)
ui.radioButton.clicked.connect(press)


ui.pushButton.clicked.connect(press)




widge.show() #這三行一定要在最下面，show之前就要完成上面那些設定
app.exec_()
sys.exit(app.exec_()) #成功結束或是失敗執行結束？
