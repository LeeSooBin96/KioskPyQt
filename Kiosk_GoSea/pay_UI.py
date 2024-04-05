from PyQt5.QtWidgets import *
from PyQt5 import uic

from __init__ import *

import sys

form_pay_UI = uic.loadUiType("pay_UI.ui")[0]

class Pay_UI(QWidget, form_pay_UI): #결제창
    def __init__(self):
        super().__init__()
        self.initUi()
        self.move(800, 200)
        self.show()
        self.order_num = 0 #주문 번호

        self.Btn_payCard.clicked.connect(self.payAll) #결제하기 버튼
        self.Btn_member.clicked.connect(self.Member) #회원 적립 버튼
        self.Btn_cancel.clicked.connect(self.cancel) #결제 취소 버튼
        self.Tshopinglist.setRowCount(1)

    def initUi(self):
        self.setupUi(self)

    def Member(self): #회원 적립 또는 생성
        while True:
            name = self.TName.text()
            if name == '신규 생성 시 입력' or name == '':
                self.TName.setText('이름을 입력해주세요')
                break
            num = self.TPhone.text()
            if len(num) == 10 and num[:3] == '011':
                num = num[3:]
            elif len(num) == 11 and num[:3] == '010':
                num = num[3:]
            else:
                self.TPhone.setText('잘못된 번호입니다.')
                break

            total = shopcart.totalprice()
            if name in memlist and num in phonelist: #기존 회원 적립
                memlist[name] += int(total*0.05)
                self.mempoint.setText(str(memlist[name]))
            else: #신규 생성
                memlist[name]=int(total*0.05)
                phonelist.append(num)
                self.mempoint.setText(str(memlist[name]))

            self.Btn_member.setDisabled(True)
            self.Btn_cancel.setDisabled(True)
            break

    def payAll(self): #결제 진행 및 장바구니 정보 초기화
        t_income.append(shopcart.totalprice()) #총 매출 저장
        for j in range(len(cate_list)):        #카테고리별 매출 저장
            for i in shopcart.category:
                if i == cate_list[j]: c_income[j] += shopcart.price[shopcart.category.index(i)]
        self.order_num += 1
        shopcart.print_reciept(self.order_num)

        self.TName.setText('신규 생성 시 입력')
        self.TPhone.setText("'-' 제외 하고 입력하세요")
        self.mempoint.clear()
        self.Btn_member.setEnabled(True)
        self.Btn_cancel.setEnabled(True)
        shopcart.clearAll()
        self.Tshopinglist.clear()
        self.T_Totalprice.clear()
        self.Tshopinglist.setRowCount(1)
        self.parent().setCurrentIndex(2)
        self.parent().currentWidget().Btn_pay.setDisabled(True)
        self.parent().currentWidget().Ttotalprice.clear()
        self.parent().currentWidget().tableWidget.clearContents()
        self.parent().currentWidget().tableWidget.setRowCount(1)
        self.parent().setCurrentIndex(0)

    def cancel(self):
        self.TName.setText('신규 생성 시 입력')
        self.TPhone.setText("'-' 제외 하고 입력하세요")
        self.Tshopinglist.setRowCount(1)
        self.parent().setCurrentIndex(2)
        self.Tshopinglist.clear()
