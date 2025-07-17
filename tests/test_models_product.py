from typing import Any
from unittest.mock import patch

import pytest

from src.models import Product, Category


def test_product_init(product_1: Product, product_2: Product) -> None:
    assert product_1.name == "Xiaomi Redmi Note 11"
    assert product_1.price == 31000.0

    assert product_2.name == "Samsung Galaxy C23 Ultra"
    assert product_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_2.quantity == 5


def test_product_init_null_price() -> None:
    with pytest.raises(ValueError):
        Product("Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                0,
                5)


def test_product_init_negative_price() -> None:
    with pytest.raises(ValueError):
        Product("Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                -180000,
                5)


def test_product_init_negative_quantity() -> None:
    with pytest.raises(ValueError):
        Product("Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000,
                -5)


def test_product_str(product_2: Product) -> None:
    assert str(product_2) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_1: Product, product_2: Product) -> None:
    assert product_1.price * product_1.quantity + product_2.price * product_2.quantity == 1334000.0


def test_product_add_invalid(product_1: Product, category_1: Category) -> None:
    with pytest.raises(TypeError):
        result = product_1 + category_1


def test_new_product_in_product_list(new_product_data: dict, prods_list: list) -> None:
    updated_product = Product.new_product(new_product_data, product_list=prods_list)

    assert updated_product in prods_list
    assert updated_product.quantity == 10
    assert updated_product.price == 181000.0


def test_new_product_not_product_list(new_product_data: dict) -> None:
    updated_product = Product.new_product(new_product_data)

    assert updated_product.name == "Samsung Galaxy S23"
    assert updated_product.description == "256GB, Серый цвет, 200MP камера"
    assert updated_product.quantity == 5
    assert updated_product.price == 181000.0


def test_new_product_invalid_data(new_product_invalid_data) -> None:
    with pytest.raises(KeyError):
        Product.new_product(new_product_invalid_data)


def test_price_accept(new_product_data: dict) -> None:
    test_product = Product(**new_product_data)

    with patch("builtins.input", return_value="1"):
        test_product.price = 170000.0

    assert test_product.price == 170000.0


def test_price_reject(new_product_data: dict) -> None:
    test_product = Product(**new_product_data)

    with patch("builtins.input", return_value="0"):
        test_product.price = 170000.0

    assert test_product.price == 181000.0


def test_price_zero(new_product_data: dict, capsys: Any) -> None:
    test_product = Product(**new_product_data)
    test_product.price = 0
    assert test_product.price == 181000.0

    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_negative_number(new_product_data: dict, capsys: Any) -> None:
    test_product = Product(**new_product_data)
    test_product.price = -100000.0
    assert test_product.price == 181000.0

    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_not_number(product_1) -> None:
    with pytest.raises(TypeError):
        product_1.price = "180000.0"
