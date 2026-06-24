import json

from faker import Faker

fake = Faker('ru_Ru')

WRONG_ID = {"id": fake.random_int(1, 99)}
WRONG_DATA = fake.random_int(1, 99)
WRONG_TRACK = fake.random_int(1000000, 9999999)

data_1 = {
    "firstName": 'Анна',
    "lastName": 'Иванова',
    "address": 'г. Москва, улица Пушкина, д. 5, кв. 17',
    "metroStation": 12,
    "phone": '+7 198 757 46 13',
    "rentTime": 3,
    "deliveryDate": '2026-06-30',
    "comment": 'Подъезд 2',
    "color": ["BLACK"]}

data_2 = {
    "firstName": 'Анна',
    "lastName": 'Иванова',
    "address": 'г. Москва, улица Пушкина, д. 5, кв. 17',
    "metroStation": "Сокольники",
    "phone": '+7 198 757 46 13',
    "rentTime": 3,
    "deliveryDate": '2026-06-30',
    "comment": 'Подъезд 2',
    "color": ["GREY"]}

data_3 = {
    "firstName": 'Анна',
    "lastName": 'Иванова',
    "address": 'г. Москва, улица Пушкина, д. 5, кв. 17',
    "metroStation": 12,
    "phone": '+7 198 757 46 13',
    "rentTime": 3,
    "deliveryDate": '2026-06-30',
    "comment": 'Подъезд 2'}

data_4 = {
    "firstName": 'Анна',
    "lastName": 'Иванова',
    "address": 'г. Москва, улица Пушкина, д. 5, кв. 17',
    "metroStation": 12,
    "phone": '+7 198 757 46 13',
    "rentTime": 3,
    "deliveryDate": '2026-06-30',
    "comment": 'Подъезд 2',
    "color": ["BLACK", "GREY"]}  

class Data:
    VALID_ORDER_DATA_BLACK = json.dumps(data_1)
    VALID_ORDER_DATA_GREY = json.dumps(data_2)
    VALID_ORDER_DATA_NONE = json.dumps(data_3)
    VALID_ORDER_DATA_BOTH = json.dumps(data_4)
