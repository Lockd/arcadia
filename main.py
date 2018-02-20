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
        self.ui.checkBox.stateChanged.connect(self.state_for_check1)
        self.ui.checkBox_2.stateChanged.connect(self.CheckLine)
        
    #UI fuctions
    def CheckLine(self):
        if self.ui.checkBox_2.isChecked() & self.ui.checkBox.isChecked():
            if self.ui.checkBox.isChecked():
                self.ui.textEdit.textChanged.connect(self.Translate_check12)
            else:
                self.ui.textEdit_2.setText("")
            
        elif self.ui.checkBox.isChecked():
            Result = self.ui.textEdit.toPlainText()
            self.ui.textEdit.textChanged.connect(self.Translate_check1)
            
        elif self.ui.checkBox_2.isChecked():
            self.ui.pushButton.clicked.connect(self.Translate)                        
        else:
            self.ui.pushButton.clicked.connect(self.Translate)
        return
            
                                            
    def Translate_check12(self):
        if self.ui.checkBox_2.isChecked():
            Result = self.ui.textEdit.toPlainText()
            words = Result.split()
            global shorten_symbols
            global shorten
            shorten_symbols = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
            shorten = ['but', 'can', 'do' ,'every', 'from', 'go', 'have', 'just', 'knowledge', 'like', 'more', 'not', 'people', 'quiet', 'rather', 'so', 'that', 'us', 'very', 'it', 'you', 'as', 'will']
            for word in words:
                counter=0
                for short in shorten:
                    if (word.find(short) != -1):
                        word_index=words.index(word)
                        words[word_index] = word.replace(short, shorten_symbols[counter])
                    else:
                        pass
                    counter+=1
            Result = ''
            for word in words:
                Result += word + ' '
            self.ui.textEdit_2.setText(Result)
        else:
            self.ui.textEdit_2.setText("")
            Result = self.ui.textEdit.toPlainText()
            self.ui.textEdit_2.setText(Result)
        if self.ui.checkBox.isChecked()==0:
            self.ui.textEdit_2.setText("")
        return

    
    def Translate(self):
        if self.ui.checkBox_2.isChecked():
            Result = self.ui.textEdit.toPlainText()
            words = Result.split()
            global shorten_symbols
            global shorten
            shorten_symbols = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
            shorten = ['but', 'can', 'do' ,'every', 'from', 'go', 'have', 'just', 'knowledge', 'like', 'more', 'not', 'people', 'quiet', 'rather', 'so', 'that', 'us', 'very', 'it', 'you', 'as', 'will']
            for word in words:
                counter=0
                for short in shorten:
                    if (word.find(short) != -1):
                        word_index=words.index(word)
                        words[word_index] = word.replace(short, shorten_symbols[counter])
                    else:
                        pass
                    counter+=1
            Result = ''
            for word in words:
                Result += word + ' '
            self.ui.textEdit_2.setText(Result)
        else:
            self.ui.textEdit_2.setText("")
            Result = self.ui.textEdit.toPlainText()
            self.ui.textEdit_2.setText(Result)
        return
            
    def Translate_check1(self):
        if self.ui.checkBox.isChecked():
            self.ui.textEdit_2.setText("")
            Result = self.ui.textEdit.toPlainText()
            if self.ui.checkBox.isChecked():
                self.ui.textEdit_2.setText(Result)
        else:
            self.ui.textEdit_2.setText("")
            
        return

    def state_for_check1(self):
        if self.ui.checkBox.isChecked():
            self.ui.pushButton.setEnabled(0)
            Result = self.ui.textEdit.toPlainText()
        else:
            self.ui.pushButton.setEnabled(1)
        return
            
    def Clear(self):
        self.ui.textEdit.setText("")
        self.ui.textEdit_2.setText("")
        return
        
    
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
