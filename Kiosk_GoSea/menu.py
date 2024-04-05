from PyQt5.QtWidgets import *
from PyQt5 import uic

from pay_UI import *

from __init__ import *

form_menu = uic.loadUiType("menu.ui")[0]
class Menu_UI(QWidget, form_menu):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.move(800, 200)
        self.Btn_pay.setDisabled(True)
        self.tab1.setCurrentIndex(0)

        self.Btn_home.clicked.connect(self.btn_home)
        self.Btn_manage.clicked.connect(self.btn_manage)
        self.Btn_pay.clicked.connect(self.btn_pay)
        self.Btn_cate1_1.clicked.connect(lambda btn:self.btn_menu1(0,0))
        self.Btn_cate1_2.clicked.connect(lambda btn:self.btn_menu1(0,1))
        self.Btn_cate1_3.clicked.connect(lambda btn:self.btn_menu1(0,2))
        self.Btn_cate2_1.clicked.connect(lambda btn:self.btn_menu1(1,0))
        self.Btn_cate2_2.clicked.connect(lambda btn:self.btn_menu1(1,1))
        self.Btn_cate2_3.clicked.connect(lambda btn:self.btn_menu1(1,2))
        self.Btn_cate2_4.clicked.connect(lambda btn:self.btn_menu1(1,3))
        self.Btn_cate3_1.clicked.connect(lambda btn:self.btn_menu1(2,0))
        self.Btn_cate3_2.clicked.connect(lambda btn:self.btn_menu1(2,1))
        self.Btn_cate3_3.clicked.connect(lambda btn:self.btn_menu1(2,2))
        self.Btn_cate3_4.clicked.connect(lambda btn:self.btn_menu1(2,3))

        self.Btn_del.clicked.connect(self.btn_menuClear)

        self.tableWidget.setRowCount(1)
    def initUi(self):
        self.setupUi(self)
    def btn_home(self):
        self.tab1.setCurrentIndex(0)
        shopcart.clearAll()
        self.Btn_pay.setDisabled(True)
        self.Ttotalprice.clear()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(1)
        self.parent().setCurrentIndex(0)

    def btn_manage(self):
        self.tab1.setCurrentIndex(0)
        shopcart.clearAll()
        self.Btn_pay.setDisabled(True)
        self.Ttotalprice.clear()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(1)
        self.parent().setCurrentIndex(3)

    def btn_pay(self):
        self.tab1.setCurrentIndex(0)
        count = 0
        count1 = 0

        self.parent().setCurrentIndex(4)

        wid = self.parent().currentWidget()
        wid.T_Totalprice.setText(self.Ttotalprice.toPlainText())

        for i in range(len(shopcart.menu)):
            if shopcart.menuop[i] == [] : #옵션없을때
                wid.Tshopinglist.insertRow(count + 1)
                count += 1
            for j in range(len(shopcart.menuop[i])):
                wid.Tshopinglist.insertRow(count+1)
                count += 1

        for i in range(len(shopcart.menu)):
            wid.Tshopinglist.setItem(count1, 0, QTableWidgetItem(shopcart.menu[i]))
            if shopcart.menuop[i] == [] : #옵션없을때
                wid.Tshopinglist.setItem(count1, 1, QTableWidgetItem('옵션 없음'))
                count1 += 1
            for j in range(len(shopcart.menuop[i])):
                wid.Tshopinglist.setItem(count1, 1, QTableWidgetItem(shopcart.menuop[i][j]))
                count1 += 1

    def btn_menu1(self, cate, menu):
        shopcart.category.append(cate_list[cate])
        shopcart.menu.append(catelist[cate].menu[menu])
        shopcart.price.append(catelist[cate].price[menu])
        self.parent().setCurrentIndex(5)

    def btn_menuClear(self):
        me = [i.row() for i in self.tableWidget.selectedItems()]  # 선택된 행번호 출력
        m = int(me[0])
        self.tableWidget.removeRow(m)
        del shopcart.category[m]
        del shopcart.menu[m]
        del shopcart.menuop[m]
        del shopcart.price[m]

        tprice = shopcart.totalprice()
        self.Ttotalprice.setText(str(tprice))

        if len(shopcart.menu) == 0: self.Btn_pay.setDisabled(True)
