from typing import Any
from unittest.mock import patch

import pytest

from src.exceptions import ProductPriceError
from src.models import Category, Product


def test_product_init(product_1: Product, product_2: Product) -> None:
    """Проверяет инициализацию объектов класса Product"""
    assert product_1.name == "Xiaomi Redmi Note 11"
    assert product_1.price == 31000.0

    assert product_2.name == "Samsung Galaxy C23 Ultra"
    assert product_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_2.quantity == 5


def test_product_validate_price_null() -> None:
    """Проверяет вызов исключения при добавлении товара с ценой 0"""
    with pytest.raises(ProductPriceError, match="Цена должна быть положительной"):
        Product("Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                0,
                5)


def test_product_validate_price_negative() -> None:
    """Проверяет вызов исключения при добавлении товара с отрицательной ценой"""
    with pytest.raises(ProductPriceError, match="Цена должна быть положительной"):
        Product("Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                -180000,
                5)


def test_product_validate_quantity_negative() -> None:
    """Проверяет вызов исключения при добавлении товара с отрицательным количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым или отрицательным количеством не может быть добавлен"):
        Product("Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000,
                -5)


def test_product_validate_quantity_null() -> None:
    """Проверяет вызов исключения при добавлении товара с отрицательным количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым или отрицательным количеством не может быть добавлен"):
        Product("Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000,
                0)


def test_product_str(product_2: Product) -> None:
    """Проверяет создание строкового представления товара для пользователя"""
    assert str(product_2) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_1: Product, product_2: Product) -> None:
    """Проверяет результат сложения полной стоимости указанных товаров на складе"""
    assert product_1.price * product_1.quantity + product_2.price * product_2.quantity == 1334000.0


def test_product_add_invalid(product_1: Product, category_1: Category) -> None:
    """Проверяет сложение стоимости товаров, один из которых не является объектом класса Product"""
    with pytest.raises(TypeError,
                       match="Товар Смартфоны, количество продуктов: 19 шт. " +
                             "не является объектом <class 'src.models.Product'>"):
        _ = product_1 + category_1


def test_new_product_in_product_list(new_product_data: dict, prods_list: list) -> None:
    """Проверяет обновление информации о существующем товаре (цена, количество)"""
    updated_product = Product.new_product(new_product_data, product_list=prods_list)

    assert updated_product in prods_list
    assert updated_product.quantity == 10
    assert updated_product.price == 181000.0


def test_new_product_not_product_list(new_product_data: dict) -> None:
    """Проверяет добавление нового товара"""
    updated_product = Product.new_product(new_product_data)

    assert updated_product.name == "Samsung Galaxy S23"
    assert updated_product.description == "256GB, Серый цвет, 200MP камера"
    assert updated_product.quantity == 5
    assert updated_product.price == 181000.0


def test_new_product_invalid_data(new_product_invalid_data: dict) -> None:
    """Проверяет вызов исключения при добавлении товара, если часть данных отсутствует"""
    with pytest.raises(KeyError, match="Отсутствуют необходимые параметры товара"):
        Product.new_product(new_product_invalid_data)


def test_price_accept(new_product_data: dict) -> None:
    """Проверяет обновление цены товара при положительной верификации"""
    test_product = Product(**new_product_data)

    with patch("builtins.input", return_value="1"):
        test_product.price = 170000.0

    assert test_product.price == 170000.0


def test_price_reject(new_product_data: dict) -> None:
    """Проверяет обновление цены товара при отрицательной верификации"""
    test_product = Product(**new_product_data)

    with patch("builtins.input", return_value="0"):
        test_product.price = 170000.0

    assert test_product.price == 181000.0


def test_price_zero(new_product_data: dict, capsys: Any) -> None:
    """Проверяет попытку изменить цену товара на 0"""
    test_product = Product(**new_product_data)
    test_product.price = 0
    assert test_product.price == 181000.0

    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_price_negative_number(new_product_data: dict, capsys: Any) -> None:
    """Проверяет попытку установить отрицательную цену товара"""
    test_product = Product(**new_product_data)
    test_product.price = -100000.0
    assert test_product.price == 181000.0

    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_price_not_number(product_1: Any) -> None:
    """Проверяет попытку изменить цену товара на нечисловое значение"""
    with pytest.raises(TypeError, match="Цена не является числом"):
        product_1.price = "180000.0"
