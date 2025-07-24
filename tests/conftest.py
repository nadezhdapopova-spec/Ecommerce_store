import pytest

from src.models import Category, Product, ProductsIterator
from src.products import LawnGrass, Smartphone


@pytest.fixture
def product_1() -> Product:
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )


@pytest.fixture
def product_2() -> Product:
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def category_1() -> Category:
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
def category_2() -> Category:
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


@pytest.fixture
def category_3() -> Category:
    return Category(
        name="Ноутбуки",
        description="Ваш помощник в работе",
        products=None
    )


@pytest.fixture(autouse=True)
def reset_class_variables():
    Category.clear_context()


@pytest.fixture
def new_product_data() -> dict:
    return {"name": "Samsung Galaxy S23",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 181000.0,
            "quantity": 5}


@pytest.fixture
def new_product_invalid_data() -> dict:
    return {"name": "Samsung Galaxy S23",
            "price": 181000.0,
            "quantity": 5}


@pytest.fixture
def prods_list() -> list:
    return [
        Product("Samsung Galaxy S23", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


@pytest.fixture
def data_from_json() -> list[dict]:
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром",
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]


@pytest.fixture
def products_iterator(category_1: Category) -> ProductsIterator:
    return ProductsIterator(category_1)


@pytest.fixture
def smartphone_product_1() -> Smartphone:
    return Smartphone("Xiaomi Redmi Note 11",
                      "1024GB, Синий",
                      31000.0,
                      14,
                      90.3,
                      "Note 11",
                      1024,
                      "Синий")


@pytest.fixture
def smartphone_product_2() -> Smartphone:
    return Smartphone("Iphone 15",
                      "512GB, Gray space",
                      210000.0,
                      8,
                      98.2,
                      "15",
                      512,
                      "Gray space")


@pytest.fixture
def lawn_qrass_product_1() -> LawnGrass:
    return LawnGrass("Газонная трава",
                     "Элитная трава для газона",
                     500.0,
                     20,
                     "Россия",
                     "7 дней",
                     "Зеленый")


@pytest.fixture
def lawn_qrass_product_2() -> LawnGrass:
    return LawnGrass("Газонная трава 2",
                     "Выносливая трава",
                     450.0,
                     15,
                     "США",
                     "5 дней",
                     "Темно-зеленый")
