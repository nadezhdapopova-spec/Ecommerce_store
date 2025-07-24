from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Метод должен быть реализован в дочерних классах"""
        pass
