from typing import Any
from unittest.mock import mock_open, patch

from src.models import Category
from src.utils import create_objects_from_json, read_json


@patch("json.load")
@patch("builtins.open", new_callable=mock_open)
def test_read_json(mock_file: Any, mock_json_load: Any) -> None:
    mock_json_load.return_value = [{"key": "value"}]

    result = read_json("test_path.json")
    assert result == [{"key": "value"}]
    mock_file.assert_called_once_with("test_path.json", "r", encoding="utf8")


def test_create_objects_from_json(data_from_json: list[dict]) -> None:
    result = create_objects_from_json(data_from_json)

    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
    assert Category.product_count == 4
    assert Category.category_count == 2
    assert result[0].products_list[0].name == "Samsung Galaxy C23 Ultra"
    assert result[0].products_list[1].name == "Iphone 15"
    assert result[1].products_list[0].name == "55\" QLED 4K"
    assert result[0].products_list[0].price == 180000.0
    assert result[1].products_list[0].quantity == 7
