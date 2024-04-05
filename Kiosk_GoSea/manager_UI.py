from PyQt5.QtWidgets import *
from PyQt5 import uic

from __init__ import *

form_manager = uic.loadUiType("managerUI.ui")[0]

class Manager_UI(QWidget, form_manager): #관리자 모드
    def __init__(self):
        super().__init__()
        self.initUi()
        self.move(800, 200)
        self.show()

        self.Btn_ShowSales.clicked.connect(self.btn_show) #매출 확인 버튼
        self.Btn_close.clicked.connect(self.btn_close) #닫기 버튼
        self.Btn_initSales.clicked.connect(self.btn_init) #매출 초기화 버튼

    def initUi(self):
        self.setupUi(self)

    def btn_show(self): #총/ 카테고리 별매출 출력 함수
        tincome=0
        for i in range(len(cate_list)):
            self.cate_income.append(f'{cate_list[i]}:{c_income[i]}원')
        for i in range(len(t_income)):
            tincome += t_income[i]
        self.total_income.setPlainText(f'총 {tincome}원')

    def btn_init(self):  #매출 초기화 함수
        t_income.clear()
        for i in range(len(c_income)):
            c_income[i] = 0
        self.cate_income.clear()
        self.total_income.clear()
        self.parent().setCurrentIndex(0)

    def btn_close(self): #닫기 버튼
        self.cate_income.clear()
        self.total_income.clear()
        self.parent().setCurrentIndex(2)