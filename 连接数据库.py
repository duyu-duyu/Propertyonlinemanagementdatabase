from PySide2.QtWidgets import QApplication, QMessageBox, QLineEdit, QPushButton, QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
import pymysql
import sys
import time
import re


class UI:

    def __init__(self):

        self.ui = QUiLoader().load('kuangjia.ui')

        self.ui.pushButton_2.clicked.connect(self.addpeople)
        self.ui.pushButton.clicked.connect(self.addhetong)
        self.ui.pushButton_3.clicked.connect(self.addshoukuan)
        self.ui.pushButton_4.clicked.connect(self.searchbaobiao)
        self.ui.pushButton_5.clicked.connect(self.searchshoukuan)
        self.ui.pushButton_6.clicked.connect(self.searchhetong)
        self.ui.pushButton_7.clicked.connect(self.searchpeople)
    def searchpeople(self):
        try:
            conn = pymysql.connect(host="192.168.61.159", user="root", password="123", database="shoulou",
                                   charset="UTF8")
        except:
            print("error")
            conn.close()
            sys.exit()
        cur = conn.cursor()
        selectSQL='select * from loupan'
        print(selectSQL)
        cur.execute(selectSQL)
        method = self.ui.tableWidget_3.rowCount()
        print(method)
        method = int(method)
        for i in range(method):
            self.ui.tableWidget_3.removeRow(0)
        for row in cur.fetchall():
            i = 0
            print(row)
            self.ui.tableWidget_3.insertRow(0)
            item = QTableWidgetItem()
            item.setText(str(row[0]))
            self.ui.tableWidget_3.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setText(str(row[1]))
            self.ui.tableWidget_3.setItem(i, 1, item)
            item = QTableWidgetItem()
            item.setText(str(row[2]))
            self.ui.tableWidget_3.setItem(i, 2, item)
            item = QTableWidgetItem()
            item.setText(str(row[3]))
            self.ui.tableWidget_3.setItem(i, 3, item)
            item = QTableWidgetItem()
            item.setText(str(row[4]))
            self.ui.tableWidget_3.setItem(i, 4, item)
            item = QTableWidgetItem()
            item.setText(str(row[5]))
            self.ui.tableWidget_3.setItem(i, 5, item)
            item = QTableWidgetItem()
            item.setText(str(row[6]))
            self.ui.tableWidget_3.setItem(i, 6, item)
            item = QTableWidgetItem()
            item.setText(str(row[7]))
            self.ui.tableWidget_3.setItem(i, 7, item)

            i = i + 1
    def searchhetong(self):
        try:
            conn = pymysql.connect(host="192.168.61.159", user="root", password="123", database="shoulou",
                                   charset="UTF8")
        except:
            print("error")
            conn.close()
            sys.exit()
        cur = conn.cursor()
        selectSQL='select * from hetong'
        print(selectSQL)
        cur.execute(selectSQL)
        method = self.ui.tableWidget_4.rowCount()
        print(method)
        method = int(method)
        for i in range(method):
            self.ui.tableWidget_4.removeRow(0)
        for row in cur.fetchall():
            i = 0
            print(row)
            self.ui.tableWidget_4.insertRow(0)
            item = QTableWidgetItem()
            item.setText(str(row[0]))
            self.ui.tableWidget_4.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setText(str(row[1]))
            self.ui.tableWidget_4.setItem(i, 1, item)
            item = QTableWidgetItem()
            item.setText(str(row[2]))
            self.ui.tableWidget_4.setItem(i, 2, item)
            item = QTableWidgetItem()
            item.setText(str(row[3]))
            self.ui.tableWidget_4.setItem(i, 3, item)
            item = QTableWidgetItem()
            item.setText(str(row[4]))
            self.ui.tableWidget_4.setItem(i, 4, item)
            item = QTableWidgetItem()
            item.setText(str(row[5]))
            self.ui.tableWidget_4.setItem(i, 5, item)
            item = QTableWidgetItem()
            item.setText(str(row[6]))
            self.ui.tableWidget_4.setItem(i, 6, item)
            item = QTableWidgetItem()
            item.setText(str(row[7]))
            self.ui.tableWidget_4.setItem(i, 7, item)

            i = i + 1
    def searchshoukuan(self):
        try:
            conn = pymysql.connect(host="192.168.61.159", user="root", password="123", database="shoulou",
                                   charset="UTF8")
        except:
            print("error")
            conn.close()
            sys.exit()
        cur = conn.cursor()
        selectSQL='select * from shoukuan'
        print(selectSQL)
        cur.execute(selectSQL)
        method = self.ui.tableWidget_5.rowCount()
        print(method)
        method = int(method)
        for i in range(method):
            self.ui.tableWidget_5.removeRow(0)
        for row in cur.fetchall():
            i = 0
            print(row)
            self.ui.tableWidget_5.insertRow(0)
            item = QTableWidgetItem()
            item.setText(str(row[0]))
            self.ui.tableWidget_5.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setText(str(row[1]))
            self.ui.tableWidget_5.setItem(i, 1, item)
            item = QTableWidgetItem()
            item.setText(str(row[2]))
            self.ui.tableWidget_5.setItem(i, 2, item)
            item = QTableWidgetItem()
            item.setText(str(row[3]))
            self.ui.tableWidget_5.setItem(i, 3, item)
            item = QTableWidgetItem()
            item.setText(str(row[4]))
            self.ui.tableWidget_5.setItem(i, 4, item)

            i = i + 1
    def searchbaobiao(self):
        try:
            conn = pymysql.connect(host="192.168.61.159", user="root", password="123", database="shoulou",
                                   charset="UTF8")
        except:
            print("error")
            conn.close()
            sys.exit()
        cur2 = conn.cursor()
        cur1 = conn.cursor()
        cur = conn.cursor()
        selectSQL='select yonghu from loupan'
        print(selectSQL)
        cur.execute(selectSQL)
        selectSQL1 = 'select loupanid from loupan'
        print(selectSQL1)
        cur1.execute(selectSQL1)
        selectSQL2 = 'select hetongid from hetong'
        print(selectSQL2)
        cur2.execute(selectSQL2)
        cur3 = conn.cursor()
        selectSQL3 = 'select shoukuanid from shoukuan'
        print(selectSQL3)
        cur3.execute(selectSQL2)
        method = self.ui.tableWidget_5.rowCount()
        print(method)
        method = int(method)
        for i in range(method):
            self.ui.tableWidget_5.removeRow(0)
        for row in cur.fetchall():
            i = 0
            print(row)
            self.ui.tableWidget_6.insertRow(0)
            item = QTableWidgetItem()
            item.setText(str(row[0]))
            self.ui.tableWidget_6.setItem(i, 0, item)
        for row in cur1.fetchall():
            i = 0
            print(row)
            self.ui.tableWidget_6.insertRow(0)
            item = QTableWidgetItem()
            item.setText(str(row[0]))
            self.ui.tableWidget_6.setItem(i, 1, item)
        for row in cur2.fetchall():
            i = 0
            print(row)
            self.ui.tableWidget_6.insertRow(0)
            item = QTableWidgetItem()
            item.setText(str(row[0]))
            self.ui.tableWidget_6.setItem(i, 2, item)
        for row in cur3.fetchall():
            i = 0
            print(row)
            self.ui.tableWidget_6.insertRow(0)
            item = QTableWidgetItem()
            item.setText(str(row[0]))
            self.ui.tableWidget_6.setItem(i, 3, item)


    def addpeople(self):
        text1 = self.ui.lineEdit_15.text()
        text2 = self.ui.lineEdit.text()
        text3 = self.ui.lineEdit_2.text()
        text4 = self.ui.lineEdit_3.text()
        text5 = self.ui.lineEdit_4.text()
        text6 = self.ui.lineEdit_5.text()
        text7 = self.ui.lineEdit_6.text()
        text8 = self.ui.lineEdit_7.text()
        print(text1, text2, text3, text4, text5, text6, text7, text8)
        try:
            conn = pymysql.connect(host="192.168.61.159", user="root", password="123", database="shoulou",
                                   charset="UTF8")
        except:
            print("error")
            conn.close()
            sys.exit()
        cur = conn.cursor()
        insertSql = 'INSERT INTO loupan values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")'%(text1,text2,text3,text4,text5,text6,text7,text8)
        print(insertSql)
        cur.execute(insertSql)
        conn.commit()

    def addhetong(self):
        text1 = self.ui.lineEdit_16.text()
        text2 = self.ui.lineEdit_17.text()
        text3 = self.ui.lineEdit_18.text()
        text4 = self.ui.lineEdit_19.text()
        text5 = self.ui.lineEdit_20.text()
        text6 = self.ui.lineEdit_21.text()
        text7 = self.ui.lineEdit_22.text()
        text8 = self.ui.lineEdit_23.text()
        print(text1, text2, text3, text4, text5, text6, text7, text8)
        try:
            conn = pymysql.connect(host="192.168.61.159", user="root", password="123", database="shoulou",
                                   charset="UTF8")
        except:
            print("error")
            conn.close()
            sys.exit()
        cur = conn.cursor()
        insertSql = 'INSERT INTO hetong values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")' % (
        text1, text2, text3, text4, text5, text6, text7, text8)
        print(insertSql)
        cur.execute(insertSql)
        conn.commit()

    def addshoukuan(self):
        text1 = self.ui.lineEdit_40.text()
        text2 = self.ui.lineEdit_41.text()
        text3 = self.ui.lineEdit_42.text()
        text4 = self.ui.lineEdit_43.text()
        text5 = self.ui.lineEdit_44.text()
        print(text1, text2, text3, text4, text5)
        try:
            conn = pymysql.connect(host="192.168.61.159", user="root", password="123", database="shoulou",
                                   charset="UTF8")
        except:
            print("error")
            conn.close()
            sys.exit()
        cur = conn.cursor()
        insertSql = 'INSERT INTO shoukuan values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")' % (
        text1, text2, text3, text4, text5)
        print(insertSql)
        cur.execute(insertSql)
        conn.commit()


app = QApplication([])
ui = UI()
ui.ui.show()
app.exec_()
