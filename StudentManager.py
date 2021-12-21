import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from src import Manager, AddStudent, UpdateStudent, AddUser, ChangePass
from src.login import LoginWindow
from src.sql import db
from PyQt5.Qt import QPixmap, QPalette, QBrush


class MyWindow(QMainWindow, Manager.Ui_Manager):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


class AddWindow(QDialog, AddStudent.Ui_AddInfo):
    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
        self.setupUi(self)


class UpdateWindow(QDialog, UpdateStudent.Ui_UpdateInfo):
    def __init__(self, parent=None):
        super(UpdateWindow, self).__init__(parent)
        self.setupUi(self)


class AddUserWindow(QDialog, AddUser.Ui_AddUser):
    def __init__(self, parent=None):
        super(AddUserWindow, self).__init__(parent)
        self.setupUi(self)


class ChangeUserWindow(QDialog, ChangePass.Ui_ChangePass):
    def __init__(self, parent=None):
        super(ChangeUserWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    login = LoginWindow()
    login.mainloop()
    if not login.LoginFlag:
        exit()
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.setFixedSize(myWin.width(), myWin.height())
    addwin = AddWindow()
    upwin = UpdateWindow()
    add_user_win = AddUserWindow()
    change_user_win = ChangeUserWindow()
    change_user_win.user.setPlainText(login.user_name)

    # 背景
    back_ground = QPalette()
    pix = QPixmap("./src/banner01.png")
    pix = pix.scaled(myWin.width(), myWin.height())
    back_ground.setBrush(QPalette.Background, QBrush(pix))
    myWin.setPalette(back_ground)
    myWin.setWindowOpacity(0.90)

    def add():
        info = addwin.get_inset()
        flag = db.inser_info(info)
        if flag[0]:
            QMessageBox.information(addwin, "sucess", flag[1])
            addwin.hide()
            myWin.add_tree(info)
            addwin.clear_text()
        else:
            QMessageBox.critical(addwin, "错误", flag[1])


    def update():
        r_info = get_selected_info()
        info = upwin.get_insert_info()
        flag = db.update_info(r_info, info)
        if flag[0]:
            QMessageBox.information(upwin, "sucess", flag[1])
            upwin.hide()
            row = myWin.Sinfo.selectedItems()[0].row()
            myWin.chang_tree(row, info)
        else:
            QMessageBox.critical(upwin, "错误", flag[1])


    def get_selected_info():
        row = myWin.Sinfo.selectedItems()[0].row()
        info = [myWin.Sinfo.item(row, col).text() for col in range(0, myWin.Sinfo.columnCount())]
        return info


    def show_upwin():
        upwin.change(get_selected_info())
        upwin.show()


    def delete():
        row = myWin.Sinfo.selectedItems()[0].row()
        sid = myWin.Sinfo.item(row, 0).text()
        reply = QMessageBox.information(myWin, '警告', f'是否删除学号为{sid}的学生信息', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
        if str(reply) == "16384":
            flag = db.delete(sid)
            if flag[0]:
                QMessageBox.information(myWin, "sucess", flag[1])
                myWin.Sinfo.removeRow(row)
            else:
                QMessageBox.critical(myWin, "错误", flag[1])
        else:
            pass


    def add_user():
        user = add_user_win.ID.toPlainText()
        passwd = add_user_win.passwd.toPlainText()
        if not user or not passwd:
            QMessageBox.critical(add_user_win, "错误", "没有输入")
            return
        flag = db.add_user([user, passwd])
        if flag[0]:
            QMessageBox.information(add_user_win, "sucess", flag[1])
            add_user_win.hide()
            add_user_win.clear()
        else:
            QMessageBox.critical(add_user_win, "错误", flag[1])


    def change_user():
        user = change_user_win.user.toPlainText()
        passwd = change_user_win.passwd.toPlainText()
        if not passwd:
            QMessageBox.critical(change_user_win, "错误", "没有输入")
            return
        flag = db.update_passwd([user, passwd])
        if flag[0]:
            QMessageBox.information(change_user_win, "sucess", flag[1])
            change_user_win.hide()
            change_user_win.passwd.setPlainText("")
        else:
            QMessageBox.critical(change_user_win, "错误", flag[1])


    def find():
        id_ = myWin.Edit_id.toPlainText()
        name = myWin.Edit_name.toPlainText()
        phone = myWin.Edit_phone.toPlainText()
        mail = myWin.Edit_email.toPlainText()
        raw = " AND "
        find_list = []
        if id_:
            find_list.append(f"s_id='{id_}'")
        if name:
            find_list.append(f"s_name='{name}'")
        if phone:
            find_list.append(f"s_telephone='{phone}'")
        if mail:
            find_list.append(f"s_email='{mail}'")
        if not any([id_, name, phone, mail]):
            QMessageBox.information(myWin, "错误", "没有输入")
        info = db.get_info(raw.join(find_list))
        if info:
            myWin.clear_table()
            myWin.set_tree(info)
        else:
            QMessageBox.information(myWin, "错误", "没有找到改信息")


    myWin.Button_add_student.clicked.connect(addwin.show)
    myWin.Button_update.clicked.connect(show_upwin)
    addwin.pushButton.clicked.connect(add)
    upwin.pushButton.clicked.connect(update)
    myWin.Button_delete.clicked.connect(delete)
    myWin.Button_add_user.clicked.connect(add_user_win.show)
    add_user_win.pushButton.clicked.connect(add_user)
    myWin.Button_change_passwd.clicked.connect(change_user_win.show)
    change_user_win.pushButton.clicked.connect(change_user)
    myWin.Button_find.clicked.connect(find)
    myWin.Button_clear.clicked.connect(myWin.recover)

    myWin.show()
    sys.exit(app.exec_())
