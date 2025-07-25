from typing import Any

import pytest

from src.models import Category, Order, Product
from src.products import Smartphone


def test_order_init(product_1: Product, smartphone_product_2: Smartphone) -> None:
    """Проверяет инициализацию объектов класса Order"""
    order_1 = Order(product_1, 2)

    assert order_1.product == "Xiaomi Redmi Note 11, количество: 2 шт., стоимость: 62000.0 руб."
    assert order_1.count == 2
    assert order_1.total_price == 62000.0

    order_2 = Order(smartphone_product_2, 2)

    assert order_2.product == "Iphone 15, количество: 2 шт., стоимость: 420000.0 руб."
    assert order_2.count == 2
    assert order_2.total_price == 420000.0


def test_validate_product(category_2: Any) -> None:
    """Проверяет вызов исключения при добавлении товара, не являющегося объектом класса Product"""
    with pytest.raises(TypeError):
        _ = Order(category_2, 3)


def test_validate_count_null(product_1: Product) -> None:
    """Проверяет вызов исключения при добавлении товара с количеством 0"""
    with pytest.raises(ValueError):
        _ = Order(product_1, 0)


def test_validate_count_negative(product_1: Product) -> None:
    """Проверяет вызов исключения при добавлении товара с отрицательным количеством"""
    with pytest.raises(ValueError):
        _ = Order(product_1, -5)


def test_validate_count_too_much(product_1: Product) -> None:
    """Проверяет вызов исключения при добавлении количества товара больше, чем есть в наличии"""
    with pytest.raises(ValueError):
        _ = Order(product_1, 15)


def test_order_product_str(product_2: Product) -> None:
    """Проверяет создание строкового представления товара для пользователя"""
    order_3 = Order(product_2, 2)

    assert order_3.product == "Samsung Galaxy C23 Ultra, количество: 2 шт., стоимость: 360000.0 руб."


def test_get_total_price(product_2: Product) -> None:
    order_4 = Order(product_2, 2)
    order_5 = Order(product_2, 3)
    order_6 = Order(product_2, 4)

    assert order_4.total_price == 360000.0
    assert order_5.total_price == 540000.0
    assert order_6.total_price == 720000.0
