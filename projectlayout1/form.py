# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_layout1(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(800, 600)
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(350, 220, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.l1pid = QtWidgets.QLineEdit(main)
        self.l1pid.setGeometry(QtCore.QRect(480, 220, 113, 20))
        self.l1pid.setObjectName("l1pid")
        self.l1ppassword = QtWidgets.QLineEdit(main)
        self.l1ppassword.setGeometry(QtCore.QRect(480, 270, 113, 20))
        self.l1ppassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.l1ppassword.setObjectName("l1ppassword")
        self.l1signb1 = QtWidgets.QPushButton(main)
        self.l1signb1.setGeometry(QtCore.QRect(410, 330, 75, 23))
        self.l1signb1.setObjectName("l1signb1")
        self.l1createb2 = QtWidgets.QPushButton(main)
        self.l1createb2.setGeometry(QtCore.QRect(390, 370, 131, 23))
        self.l1createb2.setObjectName("l1createb2")
        self.label_3 = QtWidgets.QLabel(main)
        self.label_3.setGeometry(QtCore.QRect(140, 150, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(main)
        self.label_2.setGeometry(QtCore.QRect(350, 270, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "main"))
        self.label.setText(_translate("main", "POLICE ID"))
        self.l1signb1.setText(_translate("main", "SIGNIN"))
        self.l1createb2.setText(_translate("main", "CREATE NEW ACCOUNT"))
        self.label_3.setText(_translate("main", " CRIMINAL CASE DATA BASE"))
        self.label_2.setText(_translate("main", "PASSWORD"))
