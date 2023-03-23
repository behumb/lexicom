class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price}'


class Customer:

    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone
        self.products = []

    def products_to_str_list(self):
        return "; ".join(map(str, self.products))

    def __str__(self):
        return f'{self.name} {self.phone}: {self.products_to_str_list()}'


def optimize_data_structure(data: list) -> list:
    customers_data = list(set([(record[2], record[3]) for record in data]))
    customers_list = [Customer(name=data[0], phone=data[1]) for data in customers_data]
    for customer in customers_list:
        for record in data:
            if (customer.name, customer.phone) == (record[2], record[3]):
                customer.products.append(Product(name=record[0], price=record[1]))
    return customers_list
