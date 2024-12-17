class Order:
    _total_orders = 0
    total_order_value = 0

    def __init__(self, products):
        self.products = products
        Order._total_orders += 1
        Order.total_order_value += self.total_price()

    def total_price(self):
        return sum(product.price for product in self.products)

    @classmethod
    def total_orders(cls):
        return cls._total_orders

    @classmethod
    def total_value(cls):
        return cls.total_order_value

    def __str__(self):
        return f"Заказ (Общая цена = {self.total_price()} руб.)"

    def __repr__(self):
        return f"Order(products={self.products})"
