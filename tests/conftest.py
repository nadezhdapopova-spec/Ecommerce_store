from typing import Any

import pytest

from src.models import Product, Category


@pytest.fixture
def product_1() -> Any:
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )


@pytest.fixture
def product_2() -> Any:
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def category_1() -> Any:
    return Category(
        name="Смартфоны",
        description="Смартфоны для удобства жизни",
        products=[
            Product(
                "Samsung Galaxy C23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5),
            Product(
                "Xiaomi Redmi Note 11",
                "1024GB, Синий",
                31000.0,
                14)
        ]
    )


@pytest.fixture
def category_2() -> Any:
    return Category(
        name="Телевизоры",
        description="Ваш друг и помощник",
        products=[
            Product(
                "QLED 4K",
                "Фоновая подсветка",
                123000.0,
                7)
        ]
    )
