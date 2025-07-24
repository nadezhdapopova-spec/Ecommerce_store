import json
from typing import Any

from src.models import Category, Product


def read_json(file_path: str) -> Any:
    """Читает json-файл и преобразует содержимое в python-объект"""
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    return data


def create_objects_from_json(data: list[dict]) -> list:
    """Преобразует содержимое из json-файла в объекты классов Category и Product"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
