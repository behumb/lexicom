class Technic:
    __slots__ = ('name', 'price', 'in_stock')

    def __init__(self, name: str, price: float, in_stock: bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

    @property
    def category(self) -> str:
        return 'Expensive' if self.price > 10000 else 'Budgetary'
