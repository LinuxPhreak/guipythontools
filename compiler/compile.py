#!/usr/bin/env python3
import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from compiler import Ui_MainWindow

class compiler(Ui_MainWindow):
	def __init__(self, MainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(MainWindow)

		self.cbConvert.clicked.connect(self.mkGui)

	def mkGui(self):
		srcFile = self.txtSource.text()
		destFile = self.txtDestination.text()

		subprocess.run(["/usr/bin/pyuic5", "-x", srcFile, "-o", destFile])
		
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    prog = compiler(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())