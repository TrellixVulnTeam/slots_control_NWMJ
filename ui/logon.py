# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logon.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fmLogon(object):
    def setupUi(self, fmLogon):
        fmLogon.setObjectName("fmLogon")
        fmLogon.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fmLogon.sizePolicy().hasHeightForWidth())
        fmLogon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        fmLogon.setFont(font)
        fmLogon.setMouseTracking(True)
        fmLogon.setTabletTracking(True)
        fmLogon.setFocusPolicy(QtCore.Qt.TabFocus)
        fmLogon.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhSensitiveData)
        self.label = QtWidgets.QLabel(fmLogon)
        self.label.setGeometry(QtCore.QRect(60, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setToolTipDuration(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(fmLogon)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(-1)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(fmLogon)
        self.groupBox.setGeometry(QtCore.QRect(50, 189, 301, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btnYes = QtWidgets.QPushButton(self.groupBox)
        self.btnYes.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.btnYes.setObjectName("btnYes")
        self.btnChangePassword = QtWidgets.QPushButton(self.groupBox)
        self.btnChangePassword.setGeometry(QtCore.QRect(170, 10, 121, 31))
        self.btnChangePassword.setObjectName("btnChangePassword")
        self.tbUser = QtWidgets.QLineEdit(fmLogon)
        self.tbUser.setGeometry(QtCore.QRect(160, 80, 181, 20))
        self.tbUser.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tbUser.setObjectName("tbUser")
        self.tbPassword = QtWidgets.QLineEdit(fmLogon)
        self.tbPassword.setGeometry(QtCore.QRect(160, 140, 181, 20))
        self.tbPassword.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tbPassword.setObjectName("tbPassword")
        self.groupBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tbUser.raise_()
        self.tbPassword.raise_()

        self.retranslateUi(fmLogon)
        QtCore.QMetaObject.connectSlotsByName(fmLogon)

    def retranslateUi(self, fmLogon):
        _translate = QtCore.QCoreApplication.translate
        fmLogon.setWindowTitle(_translate("fmLogon", "登录"))
        self.label.setText(_translate("fmLogon", "用户名："))
        self.label_2.setText(_translate("fmLogon", "密码："))
        self.btnYes.setText(_translate("fmLogon", "确认"))
        self.btnChangePassword.setText(_translate("fmLogon", "更改密码"))
        self.tbPassword.setInputMask(_translate("fmLogon", "*"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    fmLogon = Ui_fmLogon()
    fmLogon.setupUi(MainWindow)
    MainWindow.show()
    
sys.exit(app.exec_())