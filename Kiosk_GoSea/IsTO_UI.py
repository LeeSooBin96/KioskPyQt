from PyQt5.QtWidgets import *
from PyQt5 import uic
from __init__ import *

form_isTO = uic.loadUiType("IsTO_UI.ui")[0]

class isTO_UI(QWidget, form_isTO):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.move(800, 200)
        self.show()
        self.Btn_RTH.clicked.connect(self.btn_rth)
        self.Btn_TChoice1.clicked.connect(self.btn_choiceto1)
        self.Btn_TChoice2.clicked.connect(self.btn_choiceto2)

    def initUi(self):
        self.setupUi(self)

    def btn_rth(self):
        self.parent().setCurrentIndex(0)

    def btn_choiceto1(self):
        shopcart.take = '매장 이용'
        self.parent().setCurrentIndex(2)

    def btn_choiceto2(self):
        shopcart.take = '포장'
        self.parent().setCurrentIndex(2)
