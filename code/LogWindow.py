# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(420, 256)
        self.label_6 = QtWidgets.QLabel(Login)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 411, 51))
        self.label_6.setStyleSheet("font: 14pt \"楷体\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(50, 70, 301, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(21, 21, 260, 131))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 12pt \"黑体\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.logName = QtWidgets.QLineEdit(self.widget)
        self.logName.setObjectName("logName")
        self.gridLayout_2.addWidget(self.logName, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("font: 12pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.logPassword = QtWidgets.QLineEdit(self.widget)
        self.logPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.logPassword.setObjectName("logPassword")
        self.gridLayout_2.addWidget(self.logPassword, 1, 1, 1, 1)
        self.hint = QtWidgets.QLabel(self.widget)
        self.hint.setObjectName("hint")
        self.gridLayout_2.addWidget(self.hint, 2, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.regis = QtWidgets.QPushButton(self.widget)
        self.regis.setObjectName("regis")
        self.gridLayout.addWidget(self.regis, 0, 1, 1, 1)
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 2)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_6.setText(_translate("Login", "欢迎使用“你帮我助”物资交换软件"))
        self.label.setText(_translate("Login", "用户名："))
        self.label_2.setText(_translate("Login", "密码："))
        self.hint.setText(_translate("Login", "[提示信息]"))
        self.regis.setText(_translate("Login", "注册"))
        self.login.setText(_translate("Login", "登录"))
