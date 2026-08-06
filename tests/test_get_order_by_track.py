import allure

from api_methods.order_methods import OrderMethods
from data import WRONG_TRACK

class TestGetOrderByTrack:
    @allure.title('Успешное получение данных заказа по номеру')
    @allure.description('Проверяет, что при запросе данных заказа с указанием его номера данные возвращаются вместе с нужным кодом ответа')
    def test_get_order_by_track_success(self, create_order_and_cancel_after):
        response = OrderMethods.get_order_by_track(create_order_and_cancel_after)
        assert response.status_code == 200
        assert 'order' in response.json()

    @allure.title('Ошибка при получении данных заказа без указания его номера')
    @allure.description('Проверяет, что при попытке получения данных заказа без указания его номера возвращается ошибка')
    def test_get_order_by_track_without_track_error(self):
        response = OrderMethods.get_order_by_track('')
        assert response.status_code == 400
        assert response.json() == {"message":  "Недостаточно данных для поиска"}

    @allure.title('Ошибка несуществующего заказа при получении данных заказа')
    @allure.description('Проверяет, что при попытке получения данных заказа с указанием несуществующего номера заказа возвращается ошибка')
    def test_get_order_by_track_wrong_track_error(self):
        response = OrderMethods.get_order_by_track(WRONG_TRACK)
        assert response.status_code == 404
        assert response.json() == {"message": "Заказ не найден"}
