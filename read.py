pyuic5 -x DialogFirst.ui -o mainwindow.py


pyuic5 -x second.ui -o mainwindowCal.py


#for qtlinguist
.\lupdate.exe test.ui


t= QTranslator()
t.load("chinese.qm")
app.installTranslator(t)