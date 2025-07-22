from typing import Any

from src.models import Product


class Smartphone(Product):
    """Класс для создания товаров - смартфонов"""
    efficiency: int | float  # производительность
    model: str
    memory: int
    color: str

    def __init__(self,
                 name: str,
                 description: str,
                 price: int | float,
                 quantity: int,
                 efficiency: int | float,
                 model: str,
                 memory: int,
                 color: str) -> None:
        """Конструктор для товара - смартфона"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> int | float:
        """Возвращает сумму полной стоимости указанных товаров на складе"""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity

        raise TypeError


class LawnGrass(Product):
    """Класс для создания товаров - трава газонная"""
    country: str
    germination_period: str  # срок прорастания
    color: str

    def __init__(self,
                 name: str,
                 description: str,
                 price: int | float,
                 quantity: int,
                 country: str,
                 germination_period: str,
                 color: str) -> None:
        """Конструктор для товара - трава газонная"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> int | float:
        """Возвращает сумму полной стоимости указанных товаров на складе"""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity

        raise TypeError
