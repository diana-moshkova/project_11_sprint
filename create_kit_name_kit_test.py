# create_kit_name_kit_test.py
import pytest
from data import get_order_body
from sender_stand_request import post_new_order, get_order_by_track

class TestOrderAPI:
    def test_create_and_get_order(self):
        # Шаг 1: Выполняем запрос на создание заказа
        order_body = get_order_body()
        create_response = post_new_order(order_body)

        # Проверяем, что заказ создан успешно (код 201)
        assert create_response.status_code == 201, f"Ошибка создания заказа: получен код {create_response.status_code}, ожидался 201"

        # Сохраняем номер трека заказа
        track_number = create_response.json().get("track")
        assert track_number is not None, "Трек‑номер не был возвращён при создании заказа"

        # Шаг 2: Выполняем запрос на получение заказа по треку
        get_response = get_order_by_track(track_number)

        # Шаг 3: Проверяем, что код ответа равен 200
        assert get_response.status_code == 200, f"Ожидался код 200, но получен {get_response.status_code}"

        # Дополнительная проверка: убедимся, что в ответе есть данные о заказе
        order_data = get_response.json()
        assert "order" in order_data, "В ответе отсутствует поле 'order'"
        assert order_data["order"]["track"] == track_number, "Трек‑номер в ответе не соответствует ожидаемому"