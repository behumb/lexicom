class Technic:
    __slots__ = ('name', 'price', 'in_stock')

    def __init__(self, name: str, price: float, in_stock: bool):
        self.name = name
        # self.price = price
        # self.in_stock = in_stock

    # @property
    # def category(self) -> str:
    #     return 'Expensive' if self.price > 10000 else 'Budgetary'

    def __eq__(self, other):
        return len(self.name) == len(other.name)

    def __gt__(self, other):
        return len(self.name) > len(other.name)


def compare_by_name_length(func):
    def wrapper(technic_1, technic_2):
        if isinstance(technic_1, Technic) and isinstance(technic_2, Technic):
            return func(len(technic_1.name), len(technic_2.name))
        else:
            raise ValueError('Params must be instance of Technic')

    return wrapper


@compare_by_name_length
def compare_technics(technic_1: Technic, technic_2: Technic) -> str:
    if technic_1 == technic_2:
        return 'Names are equal'
    elif technic_1 > technic_2:
        return 'First technic name is longer'
    else:
        return 'Second technic name is longer'
