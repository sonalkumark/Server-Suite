#!/usr/bin/python
import os
from PyQt4 import QtGui as qt
import sys,platform
class serv:
	def go_for_server(self,frame,detected_os):
		os.system("python get_distro.py "+detected_os)
	def get_os(self,frame,combobox):
		self.selected_os=combobox.currentText()
		selected_os=str(self.selected_os)
		os.system("python get_distro.py "+selected_os)
	def show_about(self,frame,flag):
		os.system("python about.py")
	def show_update(self,frame,flag):
		os.system("python update.py")
	def detectos(self):
		temp=platform.linux_distribution()
		ver=temp[0]+" "+temp[1]
		return ver
	def show_help(self,frame):
		os.system("python help.py")

	def __init__(self):
		flag=True
		window=qt.QApplication(sys.argv)
		frame=qt.QWidget()
		label=qt.QLabel("< img src='images/back-6.jpg' height='500' width='500'>",frame)
		pic = qt.QLabel("<img src='images/logo128x128.png' height='50' width='50' >",frame)
		label1=qt.QLabel("Detected OS: ",frame)
		detected_os=self.detectos()
		label2=qt.QLabel("<font color='green'>"+detected_os+"</font>",frame)
		label3=qt.QLabel("Choose OS :",frame)
		label3.setHidden(True)
		check_update=qt.QPushButton("Check for update..",frame)
		about=qt.QPushButton("About",frame)
		help_btn=qt.QPushButton("Help",frame)
		cbox=qt.QCheckBox("If detected OS is not correct . .",frame)
		combobox=qt.QComboBox(frame)
		combobox.addItem("Fedora")
		combobox.addItem("Ubuntu")
		combobox.addItem("CentOS")
		combobox.setHidden(True)
		btn1=qt.QPushButton("OK",frame)
		btn2=qt.QPushButton("OK",frame)
		btn1.setHidden(True)
		btn1.clicked.connect(lambda:self.get_os(frame,combobox))
		btn2.clicked.connect(lambda:self.go_for_server(frame,detected_os))
		cbox.stateChanged.connect(lambda:self.cboxchecked(label3,combobox,cbox,btn1,btn2))
		about.clicked.connect(lambda:self.show_about(frame,flag))
		check_update.clicked.connect(lambda:self.show_update(frame,flag))
		help_btn.clicked.connect(lambda:self.show_help(frame))
		pic.move(235,30)
		label1.move(170,100)
		label2.move(270,100)
		cbox.move(150,150)
		label3.move(170,205)
		combobox.move(250,200)
		btn1.move(220,250)
		btn2.move(220,250)
		help_btn.move(40,450)
		about.move(215,450)
		check_update.move(350,450)
		frame.setWindowIcon(qt.QIcon("images/logo.svg"))
		frame.setWindowTitle("Server-Suite")
		frame.setFixedSize(500,500)
		frame.setGeometry(100,100,500,500)
		frame.show()
		window.exec_()

	def cboxchecked(self,label3,combobox,cbox,btn1,btn2):
			if cbox.isChecked() == True:
				#print "box is selected"
				label3.setHidden(False)
				combobox.setHidden(False)
				btn1.setHidden(False)
				btn2.setHidden(True)
			else:
				#print "box is deselected"
				label3.setHidden(True)
				combobox.setHidden(True)
				btn1.setHidden(True)
				btn2.setHidden(False)
	def set_button_false(self,frame):
		self.git_hub.setEnable(False)
		self.about.setEnable(False)
		self.check_update.setEnable(False)

obj=serv()
