from PyQt5.QtWidgets import* #*是為了一次全部include進來，但最保險的方式是一個一個import
from PyQt5.QtCore import*
from PyQt5.QtGui import*

from mainwindow import Ui_Dialog #把隔壁檔案import進來
import sys
def pic_click(event):
    message=QMessageBox()  #建立視窗
    message.setWindowTitle("surprise")  #視窗左上角的文字
    message.setInformativeText("你按了圖片")  #視窗跳出的東西
    message.exec_()
    event.x()
    event.y()
    event.button()

def clicked_press_me():
    x=ui.lineEdit_2.text() #以string讀取輸入line edit的x
    message=QMessageBox()  #建立視窗
    message.setWindowTitle("sur")  #視窗左上角的文字
    message.setInformativeText(x)  #視窗跳出的東西
    message.exec_()

def clicked_hello(): #按show string按鈕會在label出現hello
    ui.label.setText("hello") 
    print(ui.radioButton.isChecked()) #偵測有沒有勾
    print(ui.comboBox.currentText()) #讀取選項的字串
    print(ui.comboBox.currentIndex())#讀取選項的位置從0跟上
    ui.progressBar.setValue(40)
 
def change(i):
    print(i)
    ui.progressBar.setValue(90) #點下combo box就會變90


def slider_change(): 
    x=ui.horizontalSlider.value()
    print("change vlaue is "+ str(x))

def slider_release():
    message=QMessageBox()  #建立視窗
    message.setWindowTitle("sur")  #視窗左上角的文字
    message.setInformativeText("選擇的數值是"+ str(ui.horizontalSlider.value()))  #視窗跳出的東西
    message.exec_()


app= QApplication(sys.argv) #argv #qt程式第一行一定要有這個，不然會報錯
#dialog要放到widge裡面
widge= QWidget()
ui=Ui_Dialog()  #把這個放到widge
ui.setupUi(widge)


ui.progressBar.setMaximum(100)
ui.progressBar.setMinimum(0)
ui.progressBar.setValue(3) #3%
ui.horizontalSlider.setMaximum(110) 
ui.horizontalSlider.setMinimum(-3)
ui.horizontalSlider.valueChanged.connect(slider_change)#滑動時數值變化
ui.horizontalSlider.sliderReleased.connect(slider_release)

ui.pressMeButton.clicked.connect(clicked_press_me) #藍字是object name ＃建立button，虛要跟mainwindow2的object name 一樣
ui.helloButton.clicked.connect(clicked_hello) #藍字是object name
ui.pic.mouseReleaseEvent=pic_click #按圖片的設定＃pic是圖片名字
ui.comboBox.addItems(["cat","dog","pig"])

ui.comboBox.activated.connect(change)

widge.show()
app.exec_()
sys.exit(app.exec_()) #成功結束或是失敗執行結束？