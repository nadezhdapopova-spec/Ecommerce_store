from typing import Any
from unittest.mock import patch

from src.models import Category, Product


def test_product_init(product_1: Product, product_2: Product) -> None:
    assert product_1.name == "Xiaomi Redmi Note 11"
    assert product_1.price == 31000.0

    assert product_2.name == "Samsung Galaxy C23 Ultra"
    assert product_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_2.quantity == 5


def test_new_product_in_product_list(new_product_data: dict, products_list: list) -> None:
    updated_product = Product.new_product(new_product_data, product_list=products_list)

    assert updated_product in products_list
    assert updated_product.quantity == 10
    assert updated_product.price == 181000.0


def test_new_product_not_product_list(new_product_data: dict) -> None:
    updated_product = Product.new_product(new_product_data)

    assert updated_product.name == "Samsung Galaxy S23"
    assert updated_product.description == "256GB, Серый цвет, 200MP камера"
    assert updated_product.quantity == 5
    assert updated_product.price == 181000.0


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


def test_category_init(category_1: Category, category_2: Category) -> None:
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны для удобства жизни"
    assert len(category_1.products_list()) == 2

    assert category_2.name == "Телевизоры"
    assert category_2.description == "Ваш друг и помощник"
    assert len(category_2.products_list()) == 1

    assert Category.category_count == 2
    assert category_1.product_count == 3
    assert category_2.product_count == 3


def test_add_product(product_1: Product) -> None:
    Category.product_count = 0
    category = Category("Смартфоны", "Категория смартфонов", [])
    product_str = "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"

    category.add_product(product_1)
    assert product_str in category.products


def test_products(category_2: Category) -> None:
    test_prods = category_2.products

    assert test_prods == "QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
