import allure

from api_methods.order_methods import OrderMethods

class TestOrdersList:
    @allure.title('Успешное получение списка заказов')
    @allure.description('Проверяет, что при выполнении запроса возвращается список заказов с нужным кодом ответа')
    def test_get_orders_list_success(self):
        response = OrderMethods.get_orders_list()
        assert response.status_code == 200
        assert 'orders' in response.json()