# StudentManager

## 环境

python = "^3.6"

poetry-core >= 1.0.0

pillow = "^8.3.2"

pyqt5 = "^5.15.4"

faker = "^9.8.2"

数据库使用sqlite,文件位于`src/StudentDB.db`

## 介绍

Python作业

学生管理系统，包含登录、修改、添加用户和增加、修改、删除、查找学生信息

默认用户名密码：`root`

`StudentManger.py`：整合多窗口，实现窗口间按钮功能

`fake_info.py`：生成虚假数据

`src/sql.py`：数据库类

`src/login.py`： 登录页面

`src/Manager.py`: 主页面, 实现信息查找

`src/AddStudent.py`：添加学生页面

`src/AddUser.oy`： 添加用户页面

`src/ChangePass.py`： 修改当前用户密码页面

`src/UpdateStudent.py`： 修改学生信息页面