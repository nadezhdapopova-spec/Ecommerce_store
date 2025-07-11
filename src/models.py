from typing import Any, Optional


class Product:
    """Класс для создания продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, kwargs: dict, product_list: Optional[list] = None) -> Any:
        """Создает товар как экземпляр класса Product на основе данных словаря, если такой товар не добавлен.
           Иначе обновляет информацию о товаре (цена, количество)"""
        if product_list:
            for product in product_list:
                if product.name.lower() == kwargs["name"].lower():
                    product.quantity += kwargs.get("quantity", 0)
                    product.__price = max(product.__price, kwargs.get("price", 0))
                    return product
        return cls(**kwargs)

    @property
    def price(self) -> Any:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                verification = int(input("Понизить цену?(1 - да, 0 - нет): "))
                if verification == 1:
                    self.__price = new_price


class Category:
    """Класс для создания категорий продуктов"""
    name: str
    description: str
    products: list
    category_count = 0  # количество категорий
    product_count = 0  # общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
