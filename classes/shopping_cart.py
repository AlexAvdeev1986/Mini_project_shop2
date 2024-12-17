from classes.product import Product, HouseholdChemical
from classes.order import Order


class ShoppingCart:
    admin = "admin"  # Администратор по умолчанию

    def __init__(self, customer):
        self.customer = customer
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_details(self):
        total_spent = sum(order.total_price() for order in self.orders)
        product_list = []
        for order in self.orders:
            product_list.extend(order.products)

        product_details = ", ".join(str(product) for product in product_list)
        return (f"Покупатель {self.customer.name} приобрел: {product_details}. "
                f"Общая сумма: {total_spent} руб. "
                f"Покупки зарегистрировал пользователь {ShoppingCart.admin}.")
