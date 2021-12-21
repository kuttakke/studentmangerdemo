from faker import Faker
import random
from datetime import datetime
from src.sql import db

"""
生成假数据
"""

fake = Faker(locale="zh_CN")

for _ in range(20):
    id_ = fake.credit_card_number()
    name = fake.name()
    sex = random.choice(["男", "女"])
    phone = fake.phone_number()
    birthday = datetime.strftime(fake.date_between(start_date=datetime(1996, 1, 1), end_date=datetime(2001, 1, 1)),
                                 "%Y-%m-%d")
    address = fake.address().replace(" ", "")
    mail = fake.email()
    info = [id_, name, sex, phone, birthday, address, mail]
    flag = db.inser_info(info)
    print(flag[1])
    print(info)
