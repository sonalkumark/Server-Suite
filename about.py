from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os
class about:
	def work(self):
		window_a=qt.QApplication(sys.argv)
		frame_a=qt.QWidget()
#		frame_a.setAutoFillBackground(True)
#		frame_a.setAttribute(QtCore.Qt.WA_TranslucentBackground, 60)
#		frame.setStyleSheet("""
#		QWidget
#		{
#		background-color:gray; 
#		}
#		""")
		label_title=qt.QLabel("<font color='red'>Creaters:",frame_a)
		about_data="""<font color='green' border'2px'>Saurabh Londhe<br>Sonalkumar Kadelwar<br>Sourabh Deshmukh<br>Ashish Chikhalikar"""
		label=qt.QLabel(about_data,frame_a)
		frame_a.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		frame_a.setWindowTitle("Server-Suite About")
		label_title.move(50,20)
		label.move(100,50)
		frame_a.setGeometry(100,100,400,200)
		frame_a.show()
		window_a.exec_()
	def __init__(self):
		self.work()
o=about()
