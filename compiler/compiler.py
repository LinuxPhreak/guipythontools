# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compiler.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tbUI = QtWidgets.QTabWidget(self.centralwidget)
        self.tbUI.setObjectName("tbUI")
        self.tbUIMaker = QtWidgets.QWidget()
        self.tbUIMaker.setObjectName("tbUIMaker")
        self.gridLayout = QtWidgets.QGridLayout(self.tbUIMaker)
        self.gridLayout.setObjectName("gridLayout")
        self.lblDestination = QtWidgets.QLabel(self.tbUIMaker)
        self.lblDestination.setObjectName("lblDestination")
        self.gridLayout.addWidget(self.lblDestination, 1, 0, 1, 1)
        self.txtSource = QtWidgets.QLineEdit(self.tbUIMaker)
        self.txtSource.setObjectName("txtSource")
        self.gridLayout.addWidget(self.txtSource, 0, 2, 1, 1)
        self.txtDestination = QtWidgets.QLineEdit(self.tbUIMaker)
        self.txtDestination.setObjectName("txtDestination")
        self.gridLayout.addWidget(self.txtDestination, 1, 2, 1, 1)
        self.lblSource = QtWidgets.QLabel(self.tbUIMaker)
        self.lblSource.setObjectName("lblSource")
        self.gridLayout.addWidget(self.lblSource, 0, 0, 1, 1)
        self.cbConvert = QtWidgets.QPushButton(self.tbUIMaker)
        self.cbConvert.setObjectName("cbConvert")
        self.gridLayout.addWidget(self.cbConvert, 2, 2, 1, 1)
        self.tbUI.addTab(self.tbUIMaker, "")
        self.tbVenv = QtWidgets.QWidget()
        self.tbVenv.setObjectName("tbVenv")
        self.tbUI.addTab(self.tbVenv, "")
        self.gridLayout_2.addWidget(self.tbUI, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tbUI.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI Python Tool"))
        self.lblDestination.setText(_translate("MainWindow", "Destination File"))
        self.lblSource.setText(_translate("MainWindow", "Source File"))
        self.cbConvert.setText(_translate("MainWindow", "Convert"))
        self.tbUI.setTabText(self.tbUI.indexOf(self.tbUIMaker), _translate("MainWindow", "Create UI"))
        self.tbUI.setTabText(self.tbUI.indexOf(self.tbVenv), _translate("MainWindow", "Create VENV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

