import pytest
from classes.class_category import Category
from classes.class_category import Product


@pytest.fixture()
def category_device():
    return Category('Смартфон', 'Смартфоны', [])


def test_init(category_device):
    assert category_device.name == 'Смартфон'
    assert category_device.description == 'Смартфоны'
    assert category_device.products_quantity == 0
    assert category_device.category_quantity == 1



@pytest.fixture()
def product_device():
    return Product('', 'Samsung', 20_000, 60)


def test_product(product_device):
    assert product_device.name == ''
    assert product_device.description == 'Samsung'
    assert product_device.price == 20_000
    assert product_device.quantity == 60

