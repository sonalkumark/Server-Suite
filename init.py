from PyQt4 import QtGui as qt
import sys,platform
class serv:
	def get_os(self,frame,combobox):
		self.selected_os=combobox.currentText()
		print self.selected_os
	def detectos(self):
		temp=platform.linux_distribution()
		ver=temp[0]+" "+temp[1]
		return ver

	def __init__(self):
		window=qt.QApplication(sys.argv)
		frame=qt.QWidget()
		pic = qt.QLabel("<img src='logo.png' height='50' width='50' >",frame)
		label1=qt.QLabel("Detected OS: ",frame)
		detected_os=self.detectos()
		label2=qt.QLabel("<font color='green'>"+detected_os+"</font>",frame)
		label3=qt.QLabel("Choose OS :",frame)
		label3.setHidden(True)
		check_update=qt.QPushButton("Check for update..",frame)
		about=qt.QPushButton("About",frame)
		git_hub=qt.QPushButton("GitHub",frame)
		cbox=qt.QCheckBox("If detected OS is not correct . .",frame)
		combobox=qt.QComboBox(frame)
		combobox.addItem("Fedora")
		combobox.addItem("Ubuntu")
		combobox.addItem("CentOS")
		combobox.setHidden(True)
		btn1=qt.QPushButton("OK",frame)
		btn1.clicked.connect(lambda:self.get_os(frame,combobox))
		cbox.stateChanged.connect(lambda:self.cboxchecked(label3,combobox,cbox))
		pic.move(235,30)
		label1.move(170,100)
		label2.move(270,100)
		cbox.move(150,150)
		label3.move(170,205)
		combobox.move(250,200)
		btn1.move(220,250)
		git_hub.move(40,450)
		about.move(215,450)
		check_update.move(350,450)
		frame.setWindowIcon(qt.QIcon("ico.png"))
		frame.setWindowTitle("Config tool")
		frame.setGeometry(100,100,500,500)
		frame.show()
		window.exec_()

	def cboxchecked(self,label3,combobox,cbox):
			if cbox.isChecked() == True:
				#print "box is selected"
				label3.setHidden(False)	
				combobox.setHidden(False)
			else:
				#print "box is deselected"
				label3.setHidden(True)	
				combobox.setHidden(True)

obj=serv()
