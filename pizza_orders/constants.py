from enum import Enum

class OrderStatus(Enum):
    Pending = ('Pending', 'Pending')
    Delivered = ('Delivered', 'Delivered')

    @classmethod
    def choices(cls):
        return [x.value for x in cls]

class PizzaSizes(Enum):
    Small = ('Small', 'Small')
    Large = ('Large', 'Large')
    Medium = ('Medium', 'Large')

    @classmethod
    def choices(cls):
        return [x.value for x in cls]


class PizzaFlavours(Enum):
    Marjhareeta = ('Margarita', 'Margarita')
    Marinara = ('Marinara', 'Marinara')
    Salami = ('Salami', 'Salami')

    @classmethod
    def choices(cls):
        return [x.value for x in cls]