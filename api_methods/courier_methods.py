import requests
import allure

from url import URL

class CourierMethods:
    @staticmethod
    @allure.step('Создать курьера')
    def add_courier(body):
        return requests.post(URL.URL_ADD_COUR, data = body)
    
    @staticmethod
    @allure.step('Залогинить курьера')
    def login_courier(body):
        return requests.post(URL.URL_LOG_COUR, data = body)

    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(id, body):
        return requests.delete(f'{URL.URL_DELETE_COUR}{id}', data = body)