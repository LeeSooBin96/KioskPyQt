import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets

from IsTO_UI import isTO_UI
from menu import Menu_UI
from manager_UI import Manager_UI
from pay_UI import Pay_UI
from menuOption_UI import MenuOption_UI
from __init__ import *

form_class = uic.loadUiType("initialwindow.ui")[0]

class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(800, 200)
        self.show()

    def mousePressEvent(self, e):
        widget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    initialwindow = WindowClass()
    IsTO_UI = isTO_UI()
    pay_UI = Pay_UI()
    menu = Menu_UI()
    manager_UI = Manager_UI()
    pay_UI = Pay_UI()
    menuOption_UI = MenuOption_UI()

    widget.addWidget(initialwindow)
    widget.addWidget(IsTO_UI)
    widget.addWidget(menu)
    widget.addWidget(manager_UI)
    widget.addWidget(pay_UI)
    widget.addWidget(menuOption_UI)

    widget.setFixedHeight(600)
    widget.setFixedWidth(400)
    widget.move(800,200)
    widget.show()

    app.exec()
