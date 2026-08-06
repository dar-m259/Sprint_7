import pytest
import allure

from api_methods.courier_methods import CourierMethods
from helpers import optional_cleanup, modify_data, generate_courier_data

class TestAddCourrier:
    @allure.title('Успешное создание курьера')
    @allure.description('Проверяет, что курьер успешно создается, возвращается нужный код и ответ')
    def test_add_courier_added(self, generate_data_log_in_and_cleanup):
        response = CourierMethods.add_courier(generate_data_log_in_and_cleanup)
        assert response.status_code == 201
        assert response.json() == {"ok":True}

    @allure.title('Ошибка при создании двух одинаковых курьеров')
    @allure.description('Проверяет, что при попытке создания двух курьеров с одинаковыми данными возвращается ошибка')
    def test_add_same_courier_twice_error(self, generate_data_log_in_and_cleanup):
        response = CourierMethods.add_courier(generate_data_log_in_and_cleanup)
        assert response.status_code == 201

        response = CourierMethods.add_courier(generate_data_log_in_and_cleanup)
        optional_cleanup(response)
        assert response.status_code == 409
        assert response.json() == {"message": "Этот логин уже используется"}    

    @allure.title('Ошибка незаполненного поля логина или пароля при создании курьера')
    @allure.description('Проверяет, что при попытке создания курьера без заполнения полей логина или пароля возвращается ошибка')
    @pytest.mark.parametrize('field', ['login', 'password', 'firstName'])
    def test_add_less_courier_data_error(self, field):
        courier_data = modify_data(generate_courier_data(), field, '')

        response = CourierMethods.add_courier(courier_data)
        optional_cleanup(response, courier_data)
        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для создания учетной записи"}

    @allure.title('Ошибка уже существующего логина при создании курьера')
    @allure.description('Проверяет, что при попытке создания курьера с уже имеющимся в базе логином возвращается ошибка')
    def test_add_courier_with_existing_login_error(self, generate_data_log_in_and_cleanup):
        response = CourierMethods.add_courier(generate_data_log_in_and_cleanup)
        assert response.status_code == 201

        with allure.step('Подготовить данные курьера с уже существующим логином'):
            new_data = modify_data(generate_courier_data(), 'login', generate_data_log_in_and_cleanup['login'])
        response = CourierMethods.add_courier(new_data)
        optional_cleanup(response)
        assert response.status_code == 409
        assert response.json() == {"message": "Этот логин уже используется"}
        
    