# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisWindow(object):
    def setupUi(self, RegisWindow):
        RegisWindow.setObjectName("RegisWindow")
        RegisWindow.resize(480, 500)
        RegisWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        RegisWindow.setWindowOpacity(1.0)
        RegisWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(RegisWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 131, 41))
        self.label.setStyleSheet("font: 20pt \"黑体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 70, 391, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 340, 391, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.regConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.regConfirm.setGeometry(QtCore.QRect(140, 360, 101, 41))
        self.regConfirm.setObjectName("regConfirm")
        self.regCancel = QtWidgets.QPushButton(self.centralwidget)
        self.regCancel.setGeometry(QtCore.QRect(250, 360, 101, 41))
        self.regCancel.setObjectName("regCancel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 100, 280, 187))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 16pt \"黑体\";\n"
"font: 12pt \"Adobe Heiti Std\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 16pt \"黑体\";\n"
"font: 12pt \"Adobe Heiti Std\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 16pt \"黑体\";\n"
"font: 12pt \"Adobe Heiti Std\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.address = QtWidgets.QLineEdit(self.layoutWidget)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 5, 1, 1, 1)
        self.phone = QtWidgets.QLineEdit(self.layoutWidget)
        self.phone.setObjectName("phone")
        self.gridLayout.addWidget(self.phone, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("font: 16pt \"黑体\";\n"
"font: 12pt \"Adobe Heiti Std\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.mail = QtWidgets.QLineEdit(self.layoutWidget)
        self.mail.setObjectName("mail")
        self.gridLayout.addWidget(self.mail, 4, 1, 1, 1)
        self.password_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setObjectName("password_2")
        self.gridLayout.addWidget(self.password_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 16pt \"黑体\";\n"
"font: 12pt \"Adobe Heiti Std\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("font: 16pt \"黑体\";\n"
"font: 12pt \"Adobe Heiti Std\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.hint = QtWidgets.QLabel(self.centralwidget)
        self.hint.setGeometry(QtCore.QRect(100, 300, 281, 31))
        self.hint.setObjectName("hint")
        RegisWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        RegisWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisWindow)
        self.statusbar.setObjectName("statusbar")
        RegisWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisWindow)

    def retranslateUi(self, RegisWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisWindow.setWindowTitle(_translate("RegisWindow", "RegisWindow"))
        self.label.setToolTip(_translate("RegisWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setWhatsThis(_translate("RegisWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">注 册</span></p></body></html>"))
        self.label.setText(_translate("RegisWindow", "注 册"))
        self.regConfirm.setText(_translate("RegisWindow", "确认"))
        self.regCancel.setText(_translate("RegisWindow", "取消"))
        self.label_2.setText(_translate("RegisWindow", "用户名："))
        self.label_5.setText(_translate("RegisWindow", "手机号："))
        self.label_3.setText(_translate("RegisWindow", "密码："))
        self.label_7.setText(_translate("RegisWindow", "住址："))
        self.label_4.setText(_translate("RegisWindow", "确认密码："))
        self.label_6.setText(_translate("RegisWindow", "邮箱："))
        self.hint.setText(_translate("RegisWindow", "[提示信息]"))
