class InfoClassMixin:
    """Класс-миксин, который выводит в консоль информацию, от какого класса и с какими параметрами создан объект"""

    def __init__(self) -> None:
        """Конструктор класса InfoClassMixin"""
        print(repr(self))

    def __repr__(self) -> str:
        """Выводит в консоль информацию, от какого класса и с какими параметрами создан объект"""
        class_name = self.__class__.__name__
        attrs = ', '.join(f"{key}: {value}" for key, value in self.__dict__.items())
        return f"{class_name}({attrs})"
