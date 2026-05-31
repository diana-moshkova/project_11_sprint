# Дина Мошкова, 43-я когорта — Финальный проект. Инженер по тестированию плюс
# create_kit_name_kit_test.py
import pytest

import data
from sender_stand_request import post_new_order, get_order_by_track

class TestOrderAPI:
    def test_create_and_get_order(self):
        # Шаг 1: Выполняем запрос на создание заказа
        order_body = data.ORDER_BODY
        create_response = post_new_order(order_body)

        # Шаг 2: Сохраняем номер трека заказа
        track_number = create_response.json().get("track")

        # Шаг 3: Выполняем запрос на получение заказа по треку
        get_response = get_order_by_track(track_number)

        # Шаг 4: Проверяем, что код ответа равен 200
        assert get_response.status_code == 200, f"Ожидался код 200, но получен {get_response.status_code}"