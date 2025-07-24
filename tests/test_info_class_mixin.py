def test_info_class_mixin_product(capsys, product_1):
    message = capsys.readouterr()
    assert (message.out.strip() ==
            "Product(name: Xiaomi Redmi Note 11, description: 1024GB, Синий, _Product__price: 31000.0, quantity: 14)")


def test_info_class_mixin_smartphone_product(capsys, smartphone_product_1):
    message = capsys.readouterr()
    assert (message.out.strip() ==
            "Smartphone(name: Xiaomi Redmi Note 11, description: 1024GB, Синий, " +
            "_Product__price: 31000.0, quantity: 14)")


def test_info_class_mixin_lawn_qrass_product(capsys, lawn_qrass_product_1):
    message = capsys.readouterr()
    assert (message.out.strip() ==
            "LawnGrass(name: Газонная трава, description: Элитная трава для газона, " +
            "_Product__price: 500.0, quantity: 20)")


def test_info_class_mixin_category(capsys, category_2):
    message = capsys.readouterr()
    assert (message.out.strip().split("\n")[-1] ==
            "Category(name: Телевизоры, description: Ваш друг и помощник, _Category__products: " +
            "[Product(name: QLED 4K, description: Фоновая подсветка, _Product__price: 123000.0, quantity: 7)])")
