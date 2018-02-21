import unittest as unit

import sys
import unittest
#from PyQt5.QtGui import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import braille
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

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

    #launching unit-tests
if __name__ == '__main__':
    unit.main()
