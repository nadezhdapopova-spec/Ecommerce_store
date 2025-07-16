from src.models import Category, Product


def test_category_init(category_1: Category, category_2: Category) -> None:
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны для удобства жизни"
    assert len(category_1.products_list) == 2

    assert category_2.name == "Телевизоры"
    assert category_2.description == "Ваш друг и помощник"
    assert len(category_2.products_list) == 1

    assert Category.category_count == 2
    assert category_1.product_count == 3
    assert category_2.product_count == 3


def test_category_str(category_1: Category) -> None:
    assert str(category_1) == "Смартфоны, количество продуктов: 19 шт."


def test_products(category_2: Category) -> None:
    test_prods = category_2.products

    assert test_prods == "QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"


def test_category_products_count(category_1: Category, category_2: Category) -> None:
    assert category_1.category_products_count == 19

    assert category_2.category_products_count == 7


def test_add_product(product_1: Product) -> None:
    Category.product_count = 0
    category = Category("Смартфоны", "Категория смартфонов", [])
    product_str = "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"

    category.add_product(product_1)
    assert product_str in category.products
