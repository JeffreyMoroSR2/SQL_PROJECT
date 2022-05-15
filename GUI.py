# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import TableCreate

class Ui_MainWindow(object):
    def load_category(self):
        base = TableCreate('pythonsqlite.db')
        base.create_tables()
        result = base.print_category()
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def insert_category(self):
        base = TableCreate('pythonsqlite.db')
        base.create_tables()

        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()
        for row in range(rowCount):
            rowData = ''
            for column in range (columnCount):
                widgetItem = self.tableWidget.item(row, column)
                if(widgetItem and widgetItem.text):
                    rowData = rowData +  ' ' + widgetItem.text()

            id = rowData.split()[0]
            category = rowData.split()[1]
            base.insert_category((id, category))
            break



    def load_goods(self):
        base = TableCreate('pythonsqlite.db')
        base.create_tables()
        result = base.print_goods()
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def insert_goods(self):
        base = TableCreate('pythonsqlite.db')
        base.create_tables()

        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()
        for row in range(rowCount):
            rowData = ''
            for column in range (columnCount):
                widgetItem = self.tableWidget.item(row, column)
                if(widgetItem and widgetItem.text):
                    rowData = rowData + ' ' + widgetItem.text()

            id = rowData.split()[0]
            name = rowData.split()[1]
            price = rowData.split()[2]
            ref = rowData.split()[3]

            base.insert_category((id, name, price, ref))
            break

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 781, 341))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(30, 430, 171, 71))
        self.btn_load.setObjectName("btn_load")
        self.btn_load_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_2.setGeometry(QtCore.QRect(220, 430, 171, 71))
        self.btn_load_2.setObjectName("btn_load_2")
        self.btn_load_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_3.setGeometry(QtCore.QRect(410, 430, 171, 71))
        self.btn_load_3.setObjectName("btn_load_3")
        self.btn_load_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_4.setGeometry(QtCore.QRect(600, 430, 171, 71))
        self.btn_load_4.setObjectName("btn_load_4")

        self.btn_load.clicked.connect(self.load_category)
        self.btn_load_2.clicked.connect(self.load_goods)
        self.btn_load_3.clicked.connect(self.insert_category)
        self.btn_load_4.clicked.connect(self.insert_goods)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_load.setText(_translate("MainWindow", " Load Category"))
        self.btn_load_2.setText(_translate("MainWindow", "Load Goods"))
        self.btn_load_3.setText(_translate("MainWindow", "Insert Category"))
        self.btn_load_4.setText(_translate("MainWindow", "Insert Goods"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
