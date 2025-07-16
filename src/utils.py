import json
from typing import Any

from src.models import Category, Product


def read_json(file_path: str) -> Any:
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    return data


def create_objects_from_json(data: list[dict]) -> list:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
