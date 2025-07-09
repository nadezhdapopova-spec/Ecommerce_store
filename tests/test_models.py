from src.models import Category


def test_product_init(product_1, product_2) -> None:
    assert product_1.name == "Xiaomi Redmi Note 11"
    assert product_1.price == 31000.0

    assert product_2.name == "Samsung Galaxy C23 Ultra"
    assert product_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_2.quantity == 5


def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны для удобства жизни"
    assert len(category_1.products) == 2

    assert category_2.name == "Телевизоры"
    assert category_2.description == "Ваш друг и помощник"
    assert len(category_2.products) == 1

    assert Category.category_count == 2
    assert category_1.product_count == 3
    assert category_2.product_count == 3
