from abc import ABC, abstractmethod


class MixinRepr:
    def __repr__(self):
        print(f'{self.__class__.__name__} ({self.__dict__.items()})')


class Category(MixinRepr):
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
        Category.products_quantity += 1

    @property
    def products(self):
        return self.__products

    @property
    def list_products(self):
        output = ''
        for product in self.__products:
            output += f'{product.name}, {product.price} руб. Остаток: {product.quantity}\n'
        return output

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return quantity

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description},{self.__products})"


class Abstract(ABC):

    @classmethod
    @abstractmethod
    def creat_product(cls):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass


# class MixinRepr:
#     def __repr__(self):
#         print(f'{self.__class__.__name__} ({self.__dict__.items()})')


class Product(MixinRepr):
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

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, product):
        if isinstance(product, Product):
            self.products.append(product)

        raise TypeError


class Smartphone(Product):
    def __init__(self, efficiency, model, memory, colour, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.colour = colour


class Lawn_grass(Product):

    def __init__(self, country, period, colour, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.period = period
        self.colour = colour

print(MixinRepr.__mro__)
