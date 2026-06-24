import random
import string

from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods

def generate_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

def get_login_data(data):
    login_data = {}
    login_data['login'] = data['login']
    login_data['password'] = data['password']
    return login_data

def optional_cleanup(response, data=None):
    if response.status_code == 200:
        courier_id = response.json()
        CourierMethods.delete_courier(courier_id['id'], courier_id)
        print("Данные очищены.")
    elif response.status_code == 201:
        r = CourierMethods.login_courier(get_login_data(data))
        courier_id = r.json()
        CourierMethods.delete_courier(courier_id['id'], courier_id)
        print("Данные очищены.")
    else: 
        print("Данные не были добавлены, очистки не произошло.")

def modify_data(data, key, value):
    modified_data = data.copy()
    modified_data[key] = value
    return modified_data

def optional_cancel_order(response):
    if response.status_code == 201:
        OrderMethods.cancel_order(response.json())
        print("Заказ отменен.")
    else:
        print("Заказ не был создан.")

def optional_finish_order(in_delivery, id, id_data):
    if in_delivery == True:
        OrderMethods.finish_order(id, id_data)
        print("Заказ завершен.")
    else:
        print("Заказ не может быть завершен.")

