# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#검색 UI
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 800)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 481, 61))
        self.label_3.setStyleSheet("font: 57 28pt \"Adobe 명조 Std M\";")
        self.label_3.setObjectName("label_3")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(0, 60, 901, 721))
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 10, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 20, 411, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "미래 에셋 생명"))
        self.label_3.setText(_translate("MainWindow", "추천 펀드"))
        self.pushButton.setText(_translate("MainWindow", "확인"))
        self.comboBox.setItemText(0, _translate("MainWindow", "펀드 평균 수익률"))
        self.comboBox.setItemText(1, _translate("MainWindow", "펀드 수익률 최소값"))
        self.comboBox.setItemText(2, _translate("MainWindow", "펀드 수익률 1분위 값"))
        self.comboBox.setItemText(3, _translate("MainWindow", "펀드 수익률 중간값"))
        self.comboBox.setItemText(4, _translate("MainWindow", "펀드 수익률 3분위 값"))
        self.comboBox.setItemText(5, _translate("MainWindow", "펀드 수익률 최댓 값"))
        self.menu.setTitle(_translate("MainWindow", "미래 에셋 생명"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
