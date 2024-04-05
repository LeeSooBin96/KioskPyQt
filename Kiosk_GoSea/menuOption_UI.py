from PyQt5.QtWidgets import *
from PyQt5 import uic
from __init__ import *

form_menuOption_UI = uic.loadUiType("menuOption.ui")[0]

class MenuOption_UI(QDialog, form_menuOption_UI):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.insertMenu.clicked.connect(self.insertmenu)
        self.Btn_RTM.clicked.connect(self.btn_rtm)

    def initUi(self):
        self.setupUi(self)

    def btn_rtm(self):
        shopcart.category.pop()
        shopcart.menu.pop()
        shopcart.price.pop()
        self.checkClear()
        self.parent().setCurrentIndex(2)

    def insertmenu(self):
        tmpop = []
        # 담기 선택시 옵션값, 선택 메뉴 리스트 등록
        if self.R_rice.isChecked():
            shopcart.op.append(op_list[0])
            shopcart.sel_op(0)
        if self.R_drink1.isChecked():
            shopcart.op.append(op_list[1])
            shopcart.sel_op(1)
        if self.R_drink2.isChecked():
            shopcart.op.append(op_list[2])
            shopcart.sel_op(2)
        if self.R_drink3.isChecked():
            shopcart.op.append(op_list[3])
            shopcart.sel_op(3)

        # 이번에만 옵션 적용
        for i in range(len(shopcart.op)):
            tmpop.append(shopcart.op[i])

        shopcart.menuop.append(tmpop)

        self.checkClear()
        # 새 옵션 받기 위해 클리어
        shopcart.op.clear()
        self.parent().setCurrentIndex(2)
        wid = self.parent().currentWidget()

#-----------------------------------------------------------------------------------------
        tablemenu=shopcart.menu[-1]
        tablenum=len(shopcart.menu)-1 #들어갈 행 번호
        wid.tableWidget.setItem(tablenum,0,QTableWidgetItem(tablemenu)) #메뉴 이름 삽입
        if shopcart.menuop[-1] !=[]: #옵션 있을때
            tableop=",".join(shopcart.menuop[-1])
            wid.tableWidget.setItem(tablenum, 1, QTableWidgetItem(tableop))
            wid.tableWidget.insertRow(tablenum + 1)
        else: #옵션 없을 때
            wid.tableWidget.setItem(tablenum,1,QTableWidgetItem('옵션 없음'))
            wid.tableWidget.insertRow(tablenum + 1)

        tprice=shopcart.totalprice()
        wid.Ttotalprice.setText(str(tprice))

        self.parent().currentWidget().Btn_pay.setEnabled(True)

    def checkClear(self):
        # 체크박스 초기화
        self.R_rice.setChecked(False)
        self.R_drink1.setChecked(False)
        self.R_drink2.setChecked(False)
        self.R_drink3.setChecked(False)
