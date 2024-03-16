class Category:
    name: str
    description: str
    product: str
    category_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.product = product
        self.prodacts = self.all_prodacts(self.prodacts)
        Category.category_quantity += 1


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
