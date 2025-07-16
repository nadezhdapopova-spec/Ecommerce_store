import json
import os
from typing import Any

from config import ROOT_DIR
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


if __name__ == "__main__":
    file_name = os.path.join(ROOT_DIR, "data", "products.json")
    json_data = read_json(file_name)
    obj_categories = create_objects_from_json(json_data)
    print(obj_categories[0].name)
    print(obj_categories[0].products)
    print(obj_categories[0].products[0].name)
    print(obj_categories[0].products[1].name)
    print(obj_categories[0].products[2].name)
    print(obj_categories[1].category_count)
    print(obj_categories[1].product_count)
