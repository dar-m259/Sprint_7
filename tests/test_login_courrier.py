import pytest
import allure

from helpers import optional_cleanup, generate_courier_data, modify_data, get_login_data
from api_methods.courier_methods import CourierMethods

class TestLoginCourrier:
    @allure.title('Курьер успешно залогинился')
    @allure.description('Проверяет, что курьер успешно залогинился и ответ возвращает нужный код и id курьера')
    def test_login_courier_return_id(self, create_courier_and_log_in):
        with allure.step('Курьер создан и залогинился'):
            response = create_courier_and_log_in
        optional_cleanup(response)

        courier_id = response.json()
        assert response.status_code == 200
        assert 'id' in courier_id
    
    @allure.title('Ошибка при попытке залогинить курьера с неправильным логином или паролем')
    @allure.description('Проверяет, что при попытке залогинить курьера с неправильным логином или паролем возвращается ошибка')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_courier_wrong_login_or_password_error(self, generate_data_log_in_and_cleanup, field):        
        response = CourierMethods.add_courier(generate_data_log_in_and_cleanup)
        assert response.status_code == 201
        
        with allure.step('Подготовить данные курьера с неправильным логином или паролем'):
            wrong_data = modify_data(generate_data_log_in_and_cleanup, field, generate_courier_data()['login'])
        response = CourierMethods.login_courier(get_login_data(wrong_data))
        assert response.status_code == 404
        assert response.json() == {"message": "Учетная запись не найдена"}
    
    @allure.title('Ошибка при попытке залогинить курьера без указания логина или пароля')
    @allure.description('Проверяет, что при попытке залогинить курьера без указания логина или пароля возвращается ошибка')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_courier_empty_field_error(self, generate_data_log_in_and_cleanup, field):
        response = CourierMethods.add_courier(generate_data_log_in_and_cleanup)
        assert response.status_code == 201

        empty_field = modify_data(generate_data_log_in_and_cleanup, field, '')
        response =  CourierMethods.login_courier(get_login_data(empty_field))
        assert response.status_code == 400
        assert response.json() == {"message":  "Недостаточно данных для входа"}

    @allure.title('Ошибка при попытке залогиниться несуществующим курьером')
    @allure.description('Проверяет, что при попытке залогинить курьером с несуществующими логином и паролем возникает ошибка')
    def test_login_courier_wrong_user_error(self):
        response = CourierMethods.login_courier(get_login_data(generate_courier_data()))
        assert response.status_code == 404
        assert response.json() == {"message": "Учетная запись не найдена"}        
