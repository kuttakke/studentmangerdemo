import sqlite3
import os


class StudentDB:
    def __init__(self):
        # self.db: sqlite3
        self.db_name = "StudentDb.db"
        self.student_table = "student_info"
        self.user_table = "user"
        self.head = ["s_id", "s_name", "s_sex", "s_telephone", "s_birthday", "s_address", "s_email"]
        self._check()

    def _check(self):
        sql = sqlite3.connect(os.path.join(".", "src", self.db_name))
        create_tabel_student_table = f"""
                                    CREATE TABLE IF NOT EXISTS `{self.student_table}`  (
                                    `s_id` int NOT NULL,
                                    `s_name` varchar(255) NOT NULL,
                                    `s_sex` varchar(255) NOT NULL,
                                    `s_telephone` varchar(255) NOT NULL,
                                    `s_birthday` varchar(255) NULL,
                                    `s_address` varchar(255) NULL,
                                    `s_email` varchar(255) NULL,
                                    PRIMARY KEY (`s_id`))
                                    """
        create_tabel_user = f"""
                            CREATE TABLE IF NOT EXISTS `{self.user_table}`  (
                            `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            `user` varchar(255) NOT NULL,
                            `password` varchar(255) NOT NULL
                            );
                            """
        insert_user_root = """
                            insert into `user`(`user`, `password`) select 'root', 'root' 
                            where not exists (select * from `user` where `user`='root')
                            """
        self.db = sql
        with sql:
            sql.execute(create_tabel_student_table)
            sql.execute(create_tabel_user)
            sql.execute(insert_user_root)

    def login(self, user: str, password: str) -> bool:
        sql = f"""
                SELECT `user`, `password` FROM `user` WHERE `user`="{user}" AND `password`="{password}"
                """
        with self.db:
            flag = list(self.db.execute(sql))
        if flag:
            return True
        else:
            return False

    def get_all_info(self):
        sql = """SELECT * FROM `student_info`"""
        with self.db:
            info = list(self.db.execute(sql))
        return info

    def get_info(self, key: str):
        sql = f"""SELECT * FROM `student_info` WHERE {key}"""
        with self.db:
            info = list(self.db.execute(sql))
        return info

    def inser_info(self, info: list):
        sql = """insert into student_info (s_id, s_name, s_sex, s_telephone, s_birthday, s_address, s_email)
                values (%s,'%s','%s',%s,%s,'%s','%s')""" % (info[0], info[1], info[2], info[3], info[4], info[5], info[6])
        try:
            with self.db:
                self.db.execute(sql)
        except BaseException as e:
            return False, str(e)
        else:
            return True, "插入成功"

    def update_info(self, r_info, n_info):
        update_str = ""
        for i in range(len(r_info)):
            if r_info[i] != n_info[i]:
                update_str += f"`{self.head[i]}`"
                update_str += f"='{n_info[i]}',"
        if update_str:
            sql = f"""UPDATE student_info SET {update_str.strip(",")} WHERE s_id={r_info[0]} """
            try:
                with self.db:
                    self.db.execute(sql)
            except BaseException as e:
                return False, e
            else:
                return True, "修改成功"
        else:
            return False, "信息没有变动"

    def delete(self, sid: str):
        sql = f"""DELETE FROM student_info WHERE s_id={sid}"""
        try:
            with self.db:
                self.db.execute(sql)
        except BaseException as e:
            return False, e
        else:
            return True, "删除成功"

    def add_user(self, info: list):
        sql = """INSERT into user(user, password) VALUES ('%s', '%s')""" % (info[0], info[1])
        try:
            with self.db:
                self.db.execute(sql)
        except BaseException as e:
            return False, e
        else:
            return True, "添加成功"

    def update_passwd(self, info: list):
        sql = f"""UPDATE user SET password='{info[1]}' WHERE user='{info[0]}' """
        try:
            with self.db:
                self.db.execute(sql)
        except BaseException as e:
            return False, e
        else:
            return True, "修改成功"


db = StudentDB()
