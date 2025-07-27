from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление товара для пользователя"""
        pass

    @abstractmethod
    def __add__(self, *args: Any, **kwargs: Any) -> Any:
        """Возвращает сумму указанных товаров"""
        pass

    @property
    @abstractmethod
    def price(self) -> Any:
        """Возвращает цену товара"""
        pass

    @price.setter
    @abstractmethod
    def price(self, *args: Any, **kwargs: Any) -> None:
        """Изменяет цену товара"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Создает новый товар"""
        pass

    @staticmethod
    def validate_price(price: int | float) -> int | float:
        """Проверяет, что цена товара больше 0"""
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        return price

    @staticmethod
    def validate_quantity(quantity: int) -> int:
        """Проверяет, что количество товара не менее 0"""
        if quantity <= 0:
            raise ValueError("Товар с нулевым или отрицательным количеством не может быть добавлен")
        return quantity


class BaseCatalogObject(ABC):

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление объекта каталога (категория/заказ) для пользователя"""
        pass
