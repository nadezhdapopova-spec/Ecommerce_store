from src.models import Product


class Smartphone(Product):
    efficiency: int | float  # производительность
    model: str
    memory: int
    color: str

    def __init__(self,
                 name: str,
                 description: str,
                 price: int| float,
                 quantity: int,
                 efficiency: int | float,
                 model: str,
                 memory: int,
                 color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
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
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
