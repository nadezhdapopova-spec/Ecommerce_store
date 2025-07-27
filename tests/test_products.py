import pytest

from src.products import LawnGrass, Smartphone


def test_smartphone_product_init(smartphone_product_1: Smartphone) -> None:
    """Проверяет инициализацию объектов класса Smartphone"""
    assert smartphone_product_1.name == "Xiaomi Redmi Note 11"
    assert smartphone_product_1.description == "1024GB, Синий"
    assert smartphone_product_1.price == 31000.0
    assert smartphone_product_1.quantity == 14
    assert smartphone_product_1.efficiency == 90.3
    assert smartphone_product_1.model == "Note 11"
    assert smartphone_product_1.memory == 1024
    assert smartphone_product_1.color == "Синий"


def test_smartphone_product_add(smartphone_product_1: Smartphone, smartphone_product_2: Smartphone) -> None:
    """Проверяет результат сложения полной стоимости указанных товаров на складе"""
    assert (smartphone_product_1.price * smartphone_product_1.quantity +
            smartphone_product_2.price * smartphone_product_2.quantity == 2114000.0)


def test_smartphone_product_add_invalid(smartphone_product_1: Smartphone, lawn_qrass_product_1: LawnGrass) -> None:
    """Проверяет сложение стоимости товаров, являющихся объектами разных классов"""
    with pytest.raises(TypeError, match="Товар 'Газонная трава' " +
                                        "не является объектом <class 'src.products.Smartphone'>"):
        _ = smartphone_product_1 + lawn_qrass_product_1


def test_lawn_qrass_product_init(lawn_qrass_product_1: LawnGrass) -> None:
    """Проверяет инициализацию объектов класса LawnGrass"""
    assert lawn_qrass_product_1.name == "Газонная трава"
    assert lawn_qrass_product_1.description == "Элитная трава для газона"
    assert lawn_qrass_product_1.price == 500.0
    assert lawn_qrass_product_1.quantity == 20
    assert lawn_qrass_product_1.country == "Россия"
    assert lawn_qrass_product_1.germination_period == "7 дней"
    assert lawn_qrass_product_1.color == "Зеленый"


def test_lawn_qrass_product_add(lawn_qrass_product_1: LawnGrass, lawn_qrass_product_2: LawnGrass) -> None:
    """Проверяет результат сложения полной стоимости указанных товаров на складе"""
    assert (lawn_qrass_product_1.price * lawn_qrass_product_1.quantity +
            lawn_qrass_product_2.price * lawn_qrass_product_2.quantity == 16750.0)


def test_lawn_qrass_product_add_invalid(lawn_qrass_product_1: LawnGrass, smartphone_product_1: Smartphone) -> None:
    """Проверяет сложение стоимости товаров, являющихся объектами разных классов"""
    with pytest.raises(TypeError, match="Товар 'Xiaomi Redmi Note 11' " +
                                        "не является объектом <class 'src.products.LawnGrass'>"):
        _ = lawn_qrass_product_1 + smartphone_product_1
