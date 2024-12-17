# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.product import Product, HouseholdChemical
from classes.order import Order
from classes.discount import Discount
from classes.customer import Customer
from classes.shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def total_spent(self):
        return sum(order.total_price() for order in self.orders)

    def __str__(self):
        return f"Клиент {self.name}, общая сумма заказов: {self.total_spent()} руб."

    def __repr__(self):
        return f"Customer(name='{self.name}', orders={self.orders})"


if __name__ == "__main__":
    # Создание продуктов
    product1 = Product("Ноутбук", 50000)
    product2 = Product("Смартфон", 20000)
    product3 = HouseholdChemical("Моющее средство", 300, "моющее средство")
    product4 = HouseholdChemical("Стиральный порошок", 500, "стиральное средство")

    # Создание клиентов
    customer1 = Customer("Иван")
    customer2 = Customer("Мария")

    # Создание заказов
    order1 = Order([product1, product3])
    order2 = Order([product2, product4])
    order3 = Order([product3, product4])

    # Добавление заказов клиентам
    customer1.add_order(order1)
    customer2.add_order(order2)
    customer2.add_order(order3)

    # Создание корзины покупок
    cart1 = ShoppingCart(customer1)
    cart1.add_order(order1)

    cart2 = ShoppingCart(customer2)
    cart2.add_order(order2)
    cart2.add_order(order3)

    # Применение скидок
    print("Цена заказа с сезонной скидкой (10%):", Discount.seasonal_discount(order1))
    print("Цена заказа с промокодом (15%):", Discount.promo_code_discount(order2, 15))

    # Информация о покупателях
    print("\n--- Информация о клиентах ---")
    print(customer1)
    print(customer2)

    # Детали корзины покупок
    print("\n--- Детали корзины покупок ---")
    print(cart1.get_details())
    print(cart2.get_details())

    # Общая статистика
    print("\n--- Статистика заказов ---")
    print(f"Общее количество заказов: {Order.total_orders()}")
    print(f"Общая сумма всех заказов: {Order.total_value()} руб.")
    