import allure

from api_methods.order_methods import OrderMethods
from data import WRONG_DATA

class TestAcceptOrder:
    @allure.title('Успешное принятие заказа')
    @allure.description('Проверяет, что заказ успешно принимается, возвращается нужный код и ответ')
    def test_accept_order_success(self, get_ids_and_cancel_order_after):
        with allure.step('Создание курьера, создание заказа, получение id курьера и заказа'):
            ord_id, cour_id = get_ids_and_cancel_order_after
        response = OrderMethods.accept_order(ord_id, cour_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Ошибка отсутствия id курьера при принятии заказа')
    @allure.description('Проверяет, что при попытке принять заказ без указания id курьера возвращается ошибка')
    def test_accept_order_no_courier_id_error(self, get_ids_and_cancel_order_after):
        with allure.step('Создание курьера, создание заказа, получение id курьера и заказа'):
            ord_id, cour_id = get_ids_and_cancel_order_after
        cour_id = ''
        response = OrderMethods.accept_order(ord_id, cour_id)
        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для поиска"}

    @allure.title('Ошибка несуществующего id курьера при принятии заказа')
    @allure.description('Проверяет, что при попытке принять заказ с указанием несуществующего id курьера возвращается ошибка')
    def test_accept_order_wrong_courier_id_error(self, get_ids_and_cancel_order_after):
        with allure.step('Создание курьера, создание заказа, получение id курьера и заказа'):
            ord_id, cour_id = get_ids_and_cancel_order_after
        with allure.step('Ввести несуществующий id курьера'):
            cour_id = WRONG_DATA
        response = OrderMethods.accept_order(ord_id, cour_id)
        assert response.status_code == 404
        assert response.json() == {"message": "Курьера с таким id не существует"}

    @allure.title('Ошибка отсутствия id заказа при принятии заказа')
    @allure.description('Проверяет, что при попытке принять заказ без указания id заказа возвращается ошибка')
    def test_accept_order_no_order_id_error(self, get_ids_and_cancel_order_after):
        with allure.step('Создание курьера, создание заказа, получение id курьера и заказа'):
            ord_id, cour_id = get_ids_and_cancel_order_after
        ord_id = ''
        response = OrderMethods.accept_order(ord_id, cour_id)
        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для поиска"}

    @allure.title('Ошибка несуществующего id заказа при принятии заказа')
    @allure.description('Проверяет, что при попытке принять заказ с указанием несуществующего id заказа возвращается ошибка')
    def test_accept_order_wrong_order_id_error(self, get_ids_and_cancel_order_after):
        with allure.step('Создание курьера, создание заказа, получение id курьера и заказа'):
            ord_id, cour_id = get_ids_and_cancel_order_after
        with allure.step('Ввести несуществующий id курьера'):
            ord_id = WRONG_DATA
        response = OrderMethods.accept_order(ord_id, cour_id)
        assert response.status_code == 404
        assert response.json() == {"message": "Заказа с таким id не существует"}        
