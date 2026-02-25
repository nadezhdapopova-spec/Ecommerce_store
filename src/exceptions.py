from typing import Any


class ProductAttributeError(Exception):
    """Общий класс исключения для атрибутов класса Product"""

    def __init__(self, message: Any=None) -> None:
        super().__init__(message)


class ProductQuantityError(ProductAttributeError):
    """Класс исключения для атрибута quantity класса Product"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.message = args[0] if args else "Задано невалидное количество товара"


class ProductPriceError(ProductAttributeError):
    """Класс исключения для атрибута price класса Product"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.message = args[0] if args else "Задана невалидная цена товара"
