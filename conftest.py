import pytest

from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods
from helpers import generate_courier_data, optional_cleanup, get_login_data, optional_cancel_order, optional_finish_order
from data import Data

@pytest.fixture
def generate_data_log_in_and_cleanup():
    payload = generate_courier_data()
    yield payload

    response = CourierMethods.login_courier(get_login_data(payload))
    optional_cleanup(response)

@pytest.fixture
def create_courier_and_log_in():
    payload = generate_courier_data()
    CourierMethods.add_courier(payload)
    return CourierMethods.login_courier(get_login_data(payload))

@pytest.fixture
def get_courier_id(create_courier_and_log_in):
    r = create_courier_and_log_in
    return r.json()

@pytest.fixture
def get_courier_id_and_cleanup(create_courier_and_log_in):
    courier_id = create_courier_and_log_in.json()
    yield courier_id

    optional_cleanup(create_courier_and_log_in)

@pytest.fixture
def get_ids_and_cancel_order_after(create_courier_and_log_in):
    courier= create_courier_and_log_in.json()
    courier_id = courier['id']
    r = OrderMethods.create_order(Data.VALID_ORDER_DATA_BLACK)
    track = r.json()
    i = OrderMethods.get_order_by_track(track['track'])
    order_id = i.json()['order']['id']
    o_id = {}
    o_id['id'] = order_id
    in_delivery = i.json()['order']['inDelivery']
    yield order_id, courier_id

    optional_finish_order(order_id, o_id, in_delivery)
    optional_cleanup(create_courier_and_log_in)
    
@pytest.fixture
def create_order_and_cancel_after():    
    r = OrderMethods.create_order(Data.VALID_ORDER_DATA_BOTH)
    track = r.json()['track']
    yield track
    
    optional_cancel_order(r)



    





    









    


    

