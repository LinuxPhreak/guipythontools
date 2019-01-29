#!/usr/bin/env python3
import sys
import os
import platform
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

		if (srcFile != '' and destFile != ''):
			subprocess.run(["pyuic5", "-x", srcFile, "-o", destFile])
			subprocess.run(["notify-send", '"GUI Python file created"', '"UI file: '+srcFile+'\n Py file: '+destFile+'"'])
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)

			msg.setText("PyQt5 file has been generated at "+destFile)
			msg.setWindowTitle("File Created Successfully")
			msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
			msg.exec_()
		else:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)

			msg.setText("You must enter paths to for the files")
			msg.setWindowTitle("Empty file paths")
			msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
			msg.exec_()
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    prog = compiler(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())