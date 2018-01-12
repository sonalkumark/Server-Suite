from PyQt4 import QtGui as qt
import os,sys
class help:
    def __init__(self):
        w=qt.QApplication(sys.argv)
        frame=qt.QWidget()
        label1=qt.QLabel("< img src='images/back-2.png' height='500' width='500'>",frame)
        label=qt.QLabel("< img src='images/help.png' height='100' width='150''>",frame)
        #help_text=qt.QLabel("<font color='black' size=11 face='arial'>Help</font>",frame)
        #help_text.move(110,50)
        label.move(50,50)
        frame.setFixedSize(500,500)
        frame.setGeometry(100,100,500,500)
        frame.show()
        w.exec_()
o=help()
