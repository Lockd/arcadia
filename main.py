import sys
import os, msvcrt

from translator import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Translate)
        self.ui.pushButton_2.clicked.connect(self.Clear)
        self.ui.checkBox.stateChanged.connect(self.CheckLine)
        
        #if self.ui.checkBox.isChecked():            
            #self.ui.textEdit.textChanged.connect(self.Translate)
       

            
    #UI fuctions
    def Clear(self):
        self.ui.textEdit.setText("")
        self.ui.textEdit_2.setText("")
                                        
    def Translate(self):
        if self.ui.checkBox_2.isChecked():
            self.ui.textEdit.setText('второй чек')
        else:
            self.ui.textEdit_2.setText("")
            Result = self.ui.textEdit.toPlainText()
            self.ui.textEdit_2.setText(Result)

    def Translate_check1(self):
        if self.ui.checkBox.isChecked():
            self.ui.textEdit_2.setText("")
            Result = self.ui.textEdit.toPlainText()
            self.ui.textEdit_2.setText(Result)
        else:
            self.ui.textEdit_2.setText("")

        
    def CheckLine(self):
        if self.ui.checkBox.isChecked():
            self.ui.pushButton.setEnabled(0)
            Result = self.ui.textEdit.toPlainText()
            self.ui.textEdit_2.setText(Result)            
            self.ui.textEdit.textChanged.connect(self.Translate_check1)
        else:
            self.ui.pushButton.setEnabled(1)

    
        
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
