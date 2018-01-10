import sys,platform
from PyQt4 import QtGui
#-----------------------------------------------
def osdetect():
        temp=platform.linux_distribution()
	ver=temp[0]+" "+temp[1]
	return ver
"""
	if "centos" in os:
		return "CentOS"
	elif "fedora" in os:
		return "Fedora"
   """    # return os
#---------------------------------------------
app=QtGui.QApplication(sys.argv)
frame=QtGui.QWidget()
label1=QtGui.QLabel(frame)
label2=QtGui.QLabel(frame)
label3=QtGui.QLabel(frame)
cbox=QtGui.QCheckBox("Is Detected OS is incorrect?",frame)
detectedos=osdetect()
if detectedos :
	label2.setText("<font color='green'>"+detectedos+" </font>")
else:
	label2.setText("<font color='red'>Not Detected</font>")
label1.setText("OS Detected :")
label2.move(100,0)
label3.setText("if detected OS is correct then continue , otherwise <br> Choose OS : ")
label3.move(20,20)
cbox.move(30,60)

frame.setGeometry(100,100,500,500)
frame.setWindowTitle("Touchstart Server Configuration Tool")
frame.show()
if cbox.isChecked()==True:
	label4=QtGui.QLabel(frame)
	label4.setText("<font color='blue'>go for it</font>")
	label4.move(100,90)
app.exec_()
