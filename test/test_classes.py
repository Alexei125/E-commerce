import pytest
from classes import Category
from classes import Product


@pytest.fixture()
def category_device():
    return Category('Смартфон', 'Смартфон', 'Samsung')


def test_init(category_device):
    assert category_device.name == 'Смартфон'
    assert category_device.description == 'Смартфон'
    assert category_device.product == 'Samsung'


@pytest.fixture()
def product_device():
    return Product('Смартфон', 'Samsung', 20_000, 60)


def test_init(product_device):
    assert product_device.name == 'Смартфон'
    assert product_device.description == 'Смартфон'
    assert product_device.price == 20_000
    assert product_device.quantity == 60
