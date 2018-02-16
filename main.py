import sys
import os, msvcrt

from translator import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        if self.ui.checkBox.isChecked():
            self.ui.textEdit.setText('первый чек')
        else:
            self.ui.pushButton.clicked.connect(self.Translate)
            pass        
        self.ui.pushButton_2.clicked.connect(self.Clear)

    while 1:
        a = msvcrt.getch()
        os.system("cls")
        print(a)

    
    #UI fuctions
    def Clear(self):
        self.ui.textEdit.setText("")
        self.ui.textEdit_2.setText("")
                                        
    def Translate(self):
        if self.ui.checkBox_2.isChecked():
            self.ui.textEdit.setText('второй чек')
            pass
        else:
            self.ui.textEdit_2.setText("")
            Result = self.ui.textEdit.toPlainText()
            self.ui.textEdit_2.setText(Result)

       

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
