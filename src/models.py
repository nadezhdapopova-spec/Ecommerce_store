from typing import Any, Optional

from src.base_product import BaseProduct
from src.info_class_mixin import InfoClassMixin


class Product(BaseProduct, InfoClassMixin):
    """Класс для создания товаров"""
    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name: str, description: str, price: int | float, quantity: int) -> None:
        """Конструктор для товара"""
        self.name = name
        self.description = description
        self.__price = Product.validate_price(price)
        self.quantity = Product.validate_quantity(quantity)
        super().__init__()

    def __str__(self) -> str:
        """Возвращает строковое представление товара для пользователя"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Возвращает сумму полной стоимости указанных товаров на складе"""
        if not isinstance(other, self.__class__):
            raise TypeError(f"Товар {other} не является объектом {self.__class__}")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> Any:
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Обновляет цену товара по условию"""
        if not isinstance(new_price, (int, float)):
            raise TypeError("Цена не является числом.")
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                verification = int(input("Понизить цену?(1 - да, 0 - нет): "))
                if verification == 1:
                    self.__price = new_price

    @classmethod
    def new_product(cls, kwargs: dict, product_list: Optional[list] = None) -> Any:
        """Создает товар как объект класса Product, если товар ранее не добавлен.
           Иначе обновляет информацию о товаре (цена, количество)"""
        required_keys = {"name", "description", "price", "quantity"}
        if not required_keys.issubset(kwargs):
            raise KeyError("Отсутствуют необходимые данные товара")

        if product_list:
            for product in product_list:
                if product.name.lower() == kwargs["name"].lower():
                    product.quantity += kwargs.get("quantity")
                    product.__price = max(product.__price, kwargs.get("price"))
                    return product
        return cls(**kwargs)

    @staticmethod
    def validate_price(price: int | float) -> int | float:
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        return price

    @staticmethod
    def validate_quantity(quantity: int) -> int:
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        return quantity


class Category(InfoClassMixin):
    """Класс для создания категорий товаров"""
    name: str
    description: str
    products: list
    category_count = 0  # количество категорий
    product_count = 0  # общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: Optional[list] = None) -> None:
        """Конструктор для категории"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
        super().__init__()

    def __str__(self) -> str:
        """Возвращает строковое представление категории для пользователя"""
        return f"{self.name}, количество продуктов: {self.category_products_count} шт."

    @property
    def products(self) -> str:
        """Переобразует список товаров в категории в строку и возвращает ее"""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self) -> list:
        """Возвращает список товаров в категории"""
        return self.__products

    @property
    def category_products_count(self) -> int:
        """Возвращает количество товаров в текущей категории"""
        category_products_count = 0
        for product in self.__products:
            category_products_count += product.quantity
        return category_products_count

    def add_product(self, product: Product) -> None:
        """Добавляет новый товар в категорию"""
        if not isinstance(product, Product):
            raise TypeError(f"Товар {product} не является объектом Product")
        self.__products.append(product)
        Category.product_count += 1


class ProductsIterator:
    category_obj: Category

    def __init__(self, category_obj: Category):
        """Конструктор для итератора списка товаров в категории"""
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> Any:
        """Возвращает итератор"""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Возвращает следующий товар из списка товаров в категории"""
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
