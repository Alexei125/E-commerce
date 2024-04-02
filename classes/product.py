from product import Product
class Smartphone(Product):
    def __init__(self, efficiency, model, memory, colour, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.colour = colour




class Lawn_grass(Prodact):

    def __init__(self, country, period, colour, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.period = period
        self.colour = colour


