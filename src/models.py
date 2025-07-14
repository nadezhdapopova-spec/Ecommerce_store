class Product:
    """Класс для создания продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
