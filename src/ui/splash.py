from PyQt5 import QtCore, QtWidgets

from src.ui.splash_ui import Ui_Dialog as Splash_UI

"""
from PyQt5.QtWidgets import QMainWindow
class Splash_Dialog(QMainWindow, Splash_UI):
    def __init__(self):
        QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.center_screen()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def center_screen(self):
        size = self.size()
        desktopSize = QtWidgets.QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2) - (size.height() / 2)
        left = (desktopSize.width() / 2) - (size.width() / 2)
        self.move(left, top)

    def btn_close_clicked(self):
        self.close()
"""
# -------------------------------------------------------
# [20220502] modified by zx to make Splash_Dialog inherits QDialog instead of QMainWindow
# Otherwise, info dialog window can not show, just its label and button elements show
# Besides, run time error of "Splash_Dialog object has no attribute 'setSizeGripEnabled'" occurs
# -------------------------------------------------------
from PyQt5.QtWidgets import QDialog
class Splash_Dialog(QDialog, Splash_UI):
    def __init__(self):
        QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.center_screen()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def center_screen(self):
        size = self.size()
        desktopSize = QtWidgets.QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2) - (size.height() / 2)
        left = (desktopSize.width() / 2) - (size.width() / 2)
        self.move(left, top)

    def btn_close_clicked(self):
        self.close()