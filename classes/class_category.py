class Category:
    name: str
    description: str
    products: list
    category_quantity = 0
    products_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_quantity += 1
        Category.products_quantity += len(self.__products)

    def add_products(self, value):
        self.__products.append(value)

    @property
    def list_products(self):
        output = ''
        for product in self.__products:
            output += f'{product.name}, {product.price} руб. Остаток: {product.quantity}\n'
        return output


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def creat_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price




