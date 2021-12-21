# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateInfo(object):
    def setupUi(self, UpdateInfo):
        UpdateInfo.setObjectName("UpdateInfo")
        UpdateInfo.resize(633, 184)
        self.phone = QtWidgets.QPlainTextEdit(UpdateInfo)
        self.phone.setGeometry(QtCore.QRect(260, 70, 111, 31))
        self.phone.setObjectName("phone")
        self.address = QtWidgets.QPlainTextEdit(UpdateInfo)
        self.address.setGeometry(QtCore.QRect(60, 120, 311, 31))
        self.address.setObjectName("address")
        self.birthday = QtWidgets.QPlainTextEdit(UpdateInfo)
        self.birthday.setGeometry(QtCore.QRect(60, 70, 111, 31))
        self.birthday.setObjectName("birthday")
        self.label = QtWidgets.QLabel(UpdateInfo)
        self.label.setGeometry(QtCore.QRect(30, 20, 31, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(UpdateInfo)
        self.pushButton.setGeometry(QtCore.QRect(500, 120, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.name = QtWidgets.QPlainTextEdit(UpdateInfo)
        self.name.setGeometry(QtCore.QRect(260, 20, 111, 31))
        self.name.setObjectName("name")
        self.label_4 = QtWidgets.QLabel(UpdateInfo)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 31, 31))
        self.label_4.setObjectName("label_4")
        self.ID = QtWidgets.QPlainTextEdit(UpdateInfo)
        self.ID.setGeometry(QtCore.QRect(60, 20, 111, 31))
        self.ID.setObjectName("ID")
        self.mail = QtWidgets.QPlainTextEdit(UpdateInfo)
        self.mail.setGeometry(QtCore.QRect(470, 70, 131, 31))
        self.mail.setObjectName("mail")
        self.sex = QtWidgets.QPlainTextEdit(UpdateInfo)
        self.sex.setGeometry(QtCore.QRect(490, 20, 111, 31))
        self.sex.setObjectName("name_2")
        self.label_2 = QtWidgets.QLabel(UpdateInfo)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 31, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UpdateInfo)
        self.label_3.setGeometry(QtCore.QRect(230, 70, 31, 31))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(UpdateInfo)
        self.label_6.setGeometry(QtCore.QRect(420, 70, 51, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(UpdateInfo)
        self.label_7.setGeometry(QtCore.QRect(460, 20, 31, 31))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(UpdateInfo)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 31, 31))
        self.label_5.setObjectName("label_5")

        self.ID.setEnabled(False)
        self.retranslateUi(UpdateInfo)
        QtCore.QMetaObject.connectSlotsByName(UpdateInfo)

    def retranslateUi(self, UpdateInfo):
        _translate = QtCore.QCoreApplication.translate
        UpdateInfo.setWindowTitle(_translate("UpdateInfo", "修改学生信息"))
        self.label.setText(_translate("UpdateInfo", "学号"))
        self.pushButton.setText(_translate("UpdateInfo", "修改"))
        self.label_4.setText(_translate("UpdateInfo", "生日"))
        self.label_2.setText(_translate("UpdateInfo", "姓名"))
        self.label_3.setText(_translate("UpdateInfo", "电话"))
        self.label_6.setText(_translate("UpdateInfo", "电子邮箱"))
        self.label_7.setText(_translate("UpdateInfo", "性别"))
        self.label_5.setText(_translate("UpdateInfo", "地址"))

    def change(self, info: list):
        _translate = QtCore.QCoreApplication.translate
        self.ID.setPlainText(_translate("UpdateInfo", info[0]))
        self.name.setPlainText(_translate("UpdateInfo", info[1]))
        self.sex.setPlainText(_translate("UpdateInfo", info[2]))
        self.phone.setPlainText(_translate("UpdateInfo", info[3]))
        self.birthday.setPlainText(_translate("UpdateInfo", info[4]))
        self.address.setPlainText(_translate("UpdateInfo", info[5]))
        self.mail.setPlainText(_translate("UpdateInfo", info[6]))

    def get_insert_info(self) -> list:
        id = self.ID.toPlainText()
        name = self.name.toPlainText()
        sex = self.sex.toPlainText()
        phone = self.phone.toPlainText()
        birthday = self.birthday.toPlainText()
        address = self.address.toPlainText()
        email = self.mail.toPlainText()
        info = [id, name, sex, phone, birthday, address, email]
        return info