import sys
import os, msvcrt
import unittest as unit

from translator import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #connecting each part of UI to translation methods
        self.ui.pushButton.clicked.connect(self.Translate)
        self.ui.pushButton_2.clicked.connect(self.Clear)
        self.ui.checkBox.stateChanged.connect(self.CheckLine)
        self.ui.checkBox.stateChanged.connect(self.state_for_check1)
        self.ui.checkBox_2.stateChanged.connect(self.CheckLine)
        


                
    #Metods
    #this part navigates or translation,
    #will it be translated instanly or only after user pressed a button and so on
    def CheckLine(self):
        if self.ui.checkBox_2.isChecked() & self.ui.checkBox.isChecked():
            if self.ui.checkBox.isChecked():
                self.ui.textEdit.textChanged.connect(self.Translate_check12)
            else:
                self.ui.textEdit_2.setText("")
            
        elif self.ui.checkBox.isChecked():
            self.ui.textEdit.textChanged.connect(self.Translate_check1)
            
        elif self.ui.checkBox_2.isChecked():
            self.ui.pushButton.clicked.connect(self.Translate)                        
        else:
            self.ui.pushButton.clicked.connect(self.Translate)
        
            
    #this method works when we got both checkboxes checked                                     
    def Translate_check12(self):
        if self.ui.checkBox_2.isChecked():
            Result = self.ui.textEdit.toPlainText()
            words = Result.split()
            shorten_symbols = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'w', '&', ')', ':', ':', '.', '.', '-', ',', '?', '!', '!', '"', '"', '/']
            shorten = ['but', 'can', 'do' ,'every', 'from', 'go', 'have', 'just', 'knowledge', 'like', 'more', 'not', 'people', 'quiet', 'rather', 'so', 'that', 'us', 'very', 'it', 'you', 'as', 'wil', 'and', 'by', 'cc', 'con', 'dd', 'dis', 'com', 'ea', 'en', 'ff', 'to', 'gg', 'were', 'st']
            
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
        

    #without checkboxes, or only with second checkbox,
    #works when user presses the button
    def Translate(self):
        if self.ui.checkBox_2.isChecked():
            Result = self.ui.textEdit.toPlainText()
            words = Result.split()
            shorten_symbols = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'w', '&', ')', ':', ':', '.', '.', '-', ',', '?', '!', '!', '"', '"', '/']
            shorten = ['but', 'can', 'do' ,'every', 'from', 'go', 'have', 'just', 'knowledge', 'like', 'more', 'not', 'people', 'quiet', 'rather', 'so', 'that', 'us', 'very', 'it', 'you', 'as', 'wil', 'and', 'by', 'cc', 'con', 'dd', 'dis', 'com', 'ea', 'en', 'ff', 'to', 'gg', 'were', 'st']
            
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
        

    #when we got firs box checked        
    def Translate_check1(self):
        if self.ui.checkBox.isChecked():
            self.ui.textEdit_2.setText("")
            Result = self.ui.textEdit.toPlainText()
            if self.ui.checkBox.isChecked():
                self.ui.textEdit_2.setText(Result)
        else:
            self.ui.textEdit_2.setText("")
            
        

    #this method responsible for enabling and disabling translate button
    def state_for_check1(self):
        if self.ui.checkBox.isChecked():
            self.ui.pushButton.setEnabled(0)
            Result = self.ui.textEdit.toPlainText()
        else:
            self.ui.pushButton.setEnabled(1)
        
    
    #method to clear both text fields        
    def Clear(self):
        self.ui.textEdit.setText("")
        self.ui.textEdit_2.setText("")

    #Unit-tests for different types of input with different checkboxes    
    class UnitTests(unit.TestCase):

        def test_translate(self):
            #self.form.ui.checkBox.setChecked(0)
            #self.form.ui.checkBox_2.setChecked(0)
            Translate('qwe 123 can ,./ русский')
            respons = self.form.ui.textEdit_2.toPlainText()
            self.assertEqual(respons, 'qwe 123 can ,./ русский')

        def test_translate1(self):
            self.ui.checkBox.setChecked(1)
            self.ui.checkBox_2.setChecked(0)
            self.ui.textEdit.setText('qwe 123 can ,./ русский')
            Translate_check1()
            respons = self.ui.textEdit_2.toPlainText()
            self.assertEqual(respons, 'qwe 123 can ,./ русский')

        def test_translate2(self):
            self.ui.checkBox.setChecked(0)
            self.ui.checkBox_2.setChecked(1)
            self.ui.textEdit.setText('qwe 123 can ,./ русский')
            Tanslate()
            respons = self.ui.textEdit_2.toPlainText()
            self.assertEqual(respons, 'qwe 123 c ,./ русский')

        def test_translate12(self):
            self.ui.checkBox_2.setChecked(1)
            self.ui.checkBox.setChecked(1)            
            self.ui.textEdit.setText('qwe 123 can ,./ русский')
            Translate_check12()
            respons = self.ui.textEdit_2.toPlainText()
            self.assertEqual(respons, 'qwe 123 c ,./ русский')

        def test_clear(self):
            self.ui.textEdit.setText('qwe 123 can ,./ русский')
            Clear()
            respons = self.ui.textEdit_2.toPlainText()
            self.assertEqual(self.ui.textEdit_2.toPlainText(), '')

        
    
        


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

    #launching unit-tests
    unit.main()

