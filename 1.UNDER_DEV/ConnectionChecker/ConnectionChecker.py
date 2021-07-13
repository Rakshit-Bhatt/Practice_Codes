# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RequestDemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 551)
        MainWindow.setMinimumSize(QtCore.QSize(650, 450))
        MainWindow.setStyleSheet("color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 gray, stop:1 dark)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Connectivity_button = QtWidgets.QPushButton(self.centralwidget)
        self.Connectivity_button.setGeometry(QtCore.QRect(290, 100, 171, 40))
        self.Connectivity_button.setToolTip("")
        self.Connectivity_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Connectivity_button.setStyleSheet("QPushButton\n"
"{\n"
"\n"
"font:75 8pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(40, 40, 40), stop:1 rgb(130, 130, 130) );\n"
"border-style: solid;\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover \n"
"{\n"
"    background-color: rgb(150, 150, 150);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.Connectivity_button.setObjectName("Connectivity_button")
        self.Connectivity_label = QtWidgets.QLabel(self.centralwidget)
        self.Connectivity_label.setGeometry(QtCore.QRect(200, 10, 359, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        
        self.Connectivity_label.setFont(font)
        self.Connectivity_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Connectivity_label.setAutoFillBackground(False)
        self.Connectivity_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:3px solid gray;\n"
"")
        self.Connectivity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Connectivity_label.setWordWrap(True)
        self.Connectivity_label.setIndent(0)
        self.Connectivity_label.setObjectName("Connectivity_label")
        
        self.URL_label = QtWidgets.QLabel(self.centralwidget)
        self.URL_label.setGeometry(QtCore.QRect(20, 160, 291, 41))
        self.URL_label.setToolTip("")
        self.URL_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.URL_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:3px solid gray;\n"
"")
        self.URL_label.setAlignment(QtCore.Qt.AlignCenter)
        self.URL_label.setObjectName("URL_label")
        self.Keyword_label = QtWidgets.QLabel(self.centralwidget)
        self.Keyword_label.setGeometry(QtCore.QRect(440, 160, 291, 41))
        self.Keyword_label.setToolTip("")
        self.Keyword_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Keyword_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:3px solid gray;\n"
"")
        self.Keyword_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Keyword_label.setObjectName("Keyword_label")
        self.Output_label = QtWidgets.QLabel(self.centralwidget)
        self.Output_label.setGeometry(QtCore.QRect(67, 226, 631, 241))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Output_label.setFont(font)
        self.Output_label.setToolTip("")
        self.Output_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:3px solid gray;\n"
"")
        self.Output_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Output_label.setWordWrap(True)
        self.Output_label.setIndent(1)
        self.Output_label.setObjectName("Output_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #CLEARING THE LABELS
        self.Keyword_label.setText("")
        self.URL_label.setText("")
        self.Output_label.setText("")
    

        self.Connectivity_button.clicked.connect(self.checker)

    def checker(self):
        site='http://www.google.com/'
        status_code=requests.get(site).status_code
        self.Connectivity_label.setText("")
        try:
            if status_code==200:
                res='Interent working fine.....'
                self.Connectivity_label.setText(res)
            else:
                res='Internet not working fine....'
                self.Connectivity_label.setText(res)
        except Exception as e:
            fault=("An error occured.....ERROR TYPE:", e)
            self.Connectivity_label.setText(fault)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Connectivity_button.setStatusTip(_translate("MainWindow", "Click here to check for the connectivity test."))
        self.Connectivity_button.setText(_translate("MainWindow", "CHECK CONNECTIVITY"))
        self.Connectivity_label.setStatusTip(_translate("MainWindow", "Widget to show for the output of your checker"))
        self.Connectivity_label.setText(_translate("MainWindow", "Click on the button below to get status:"))
        self.URL_label.setStatusTip(_translate("MainWindow", "Type the URL in address field to get headers."))
        self.URL_label.setText(_translate("MainWindow", "TYPE THE URL HERE CORRECTLY: "))
        self.Keyword_label.setStatusTip(_translate("MainWindow", "Enter the string to be searched for."))
        self.Keyword_label.setText(_translate("MainWindow", "ENTER THE SEARCH KEYWORDS:"))
        self.Output_label.setStatusTip(_translate("MainWindow", "Your searched URl/keywords will result here."))
        self.Output_label.setText(_translate("MainWindow", "HERE IS THE OUTPUT BEING SHOWN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())