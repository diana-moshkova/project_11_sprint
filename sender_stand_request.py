# sender_stand_request.py
import requests
from configuration import BASE_URL, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH

def post_new_order(order_body):
    """Отправляет POST‑запрос на создание заказа"""
    url = BASE_URL + CREATE_ORDER_PATH
    response = requests.post(url, json=order_body)
    return response

def get_order_by_track(track_number):
    """Отправляет GET‑запрос для получения заказа по номеру трека"""
    url = BASE_URL + GET_ORDER_BY_TRACK_PATH
    params = {"t": track_number}
    response = requests.get(url, params=params)
    return response