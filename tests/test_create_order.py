import pytest
import allure
import json

from data import Data
from api_methods.order_methods import OrderMethods
from helpers import optional_cancel_order

class TestCreateOrder:
    @allure.title('Успешное создание заказа с разными вариантами выбранного цвета самоката')
    @allure.description('Проверяет успешное создание заказа с разными вариантами выбранного цвета самоката (черный, серый, черный и серый, никакой), возвращение нужного кода и ответа')
    @pytest.mark.parametrize('data', [Data.VALID_ORDER_DATA_BLACK, Data.VALID_ORDER_DATA_GREY, Data.VALID_ORDER_DATA_NONE, Data.VALID_ORDER_DATA_BOTH])
    def test_create_order_with_different_scooter_variants_success(self, data):
        response = OrderMethods.create_order(json.dumps(data))
        optional_cancel_order(response)
        assert response.status_code == 201
        assert 'track' in response.json()
        