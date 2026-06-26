import requests
import allure

from url import URL

class OrderMethods:
    @staticmethod
    @allure.step('Создать заказ')
    def create_order(body):
        return requests.post(URL.URL_CREATE_ORDER, data = body)
    
    @staticmethod
    @allure.step('Отменить заказ')
    def cancel_order(body):
        return requests.put(URL.URL_CANCEL_ORDER, params = body)

    @staticmethod
    @allure.step('Получить список заказов')
    def get_orders_list():
        return requests.get(URL.URL_GET_ORDERS_LIST)

    @staticmethod
    @allure.step('Получить заказ по номеру')
    def get_order_by_track(t):
        return requests.get(f'{URL.URL_GET_ORDER_BY_TRACK}?t={t}')

    @staticmethod
    @allure.step('Принять заказ')
    def accept_order(id, courier_id):
        return requests.put(f'{URL.URL_ACCEPT_ORDER}{id}?courierId={courier_id}')
    
    @staticmethod
    @allure.step('Завершить заказ')
    def finish_order(id, body):
        return requests.put(f'{URL.URL_FINISH_ORDER}{id}', data = body)
    
    
   

    
    
    