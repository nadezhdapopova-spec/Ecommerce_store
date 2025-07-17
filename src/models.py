from typing import Any, Optional


class Product:
    """Класс для создания товаров"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Возвращает сумму полной стоимости указанных товаров на складе"""
        if not isinstance(other, Product):
            raise TypeError(f"Товар {other} не является объектом Product")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, kwargs: dict, product_list: Optional[list] = None) -> Any:
        """Создает товар как экземпляр класса Product на основе данных словаря, если такой товар не добавлен.
           Иначе обновляет информацию о товаре (цена, количество)"""
        required_keys = {"name", "description", "price", "quantity"}
        if not required_keys.issubset(kwargs):
            raise KeyError("Отсутствуют необходимые ключи")

        if product_list:
            for product in product_list:
                if product.name.lower() == kwargs["name"].lower():
                    product.quantity += kwargs.get("quantity", 0)
                    product.__price = max(product.__price, kwargs.get("price", 0))
                    return product
        return cls(**kwargs)

    @property
    def price(self) -> Any:
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
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


class Category:
    """Класс для создания категорий товаров"""
    name: str
    description: str
    products: list
    category_count = 0  # количество категорий
    product_count = 0  # общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: Optional[list] = None) -> None:
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории для пользователя"""
        return f"{self.name}, количество продуктов: {self.category_products_count} шт."

    @property
    def products(self) -> str:
        """Переобразует список товаров в категории в строку заданного формата и возвращает ее"""
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
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> Any:
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
