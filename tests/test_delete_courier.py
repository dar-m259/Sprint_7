import allure

from api_methods.courier_methods import CourierMethods
from data import WRONG_ID

class TestDeleteCourier:
    @allure.title('Успешное удаление курьера')
    @allure.description('Проверяет, что курьер успешно удаляется из базы, возвращается нужный код и ответ')
    def test_delete_courier_sucess(self, get_courier_id):
        response = CourierMethods.delete_courier(get_courier_id['id'], get_courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Ошибка при удалении курьера без указания его id')
    @allure.description('Проверяет, что при попытке удаления курьера без указания id курьера возвращается ошибка')
    def test_delete_courier_no_id_in_body_error(self, get_courier_id_and_cleanup):
        response = CourierMethods.delete_courier(get_courier_id_and_cleanup['id'], '')
        assert response.status_code == 400
        assert response.json() == {"message":  "Недостаточно данных для удаления курьера"}            

    @allure.title('Ошибка несуществующего id курьера при удалении курьера')
    @allure.description('Проверяет, что при попытке удаления курьера с указанием несуществующего id курьера возвращается ошибка')
    def test_delete_courier_wrong_id_error(self):
        with allure.step('Подготовить данные несуществующего id курьера'):
            courier_id = WRONG_ID
        response = CourierMethods.delete_courier(courier_id['id'], courier_id)
        assert response.status_code == 404
        assert {"message": "Курьера с таким id нет"}
    

    
