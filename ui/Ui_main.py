# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Projects\workflow\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChange_Password = QtWidgets.QAction(MainWindow)
        self.actionChange_Password.setObjectName("actionChange_Password")
        self.actionQuery = QtWidgets.QAction(MainWindow)
        self.actionQuery.setObjectName("actionQuery")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionInput_Slot_Allocation = QtWidgets.QAction(MainWindow)
        self.actionInput_Slot_Allocation.setObjectName("actionInput_Slot_Allocation")
        self.actionInput_Booking = QtWidgets.QAction(MainWindow)
        self.actionInput_Booking.setObjectName("actionInput_Booking")
        self.menu.addSeparator()
        self.menu.addAction(self.actionChange_Password)
        self.menu_2.addAction(self.actionQuery)
        self.menu_2.addAction(self.actionEdit)
        self.menu_3.addAction(self.actionInput_Slot_Allocation)
        self.menu_3.addAction(self.actionInput_Booking)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "管理"))
        self.menu_2.setTitle(_translate("MainWindow", "运管"))
        self.menu_3.setTitle(_translate("MainWindow", "舱控"))
        self.actionChange_Password.setText(_translate("MainWindow", "Change Password"))
        self.actionQuery.setText(_translate("MainWindow", "Query"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionInput_Slot_Allocation.setText(_translate("MainWindow", "Input Slot Allocation"))
        self.actionInput_Booking.setText(_translate("MainWindow", "Input Booking"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

