class Category:
    name: str
    description: str
    products: list
    category_quantity = 0
    products_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = __products
        Category.category_quantity += 1
        Category.products_quantity += len(self.__products)

    def add_products(self, value):
        return self.__products.append(value)

    @property
    def list_products(self):
        for product in self.__products:
            output += f'{product.name}, {product.price} руб. Остаток: {product.available}'

        return output


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def creat_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return f'Цена = {self.price}'

    @price.setter
    def price(self):
        if self.price <= 0:
            print('Цена введена не корректная')
