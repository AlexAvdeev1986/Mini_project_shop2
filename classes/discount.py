class Discount:
    @staticmethod
    def apply_discount(price, discount_percent):
        if not (0 <= discount_percent <= 100):
            raise ValueError("Процент скидки должен быть от 0 до 100")
        return price * (1 - discount_percent / 100)

    @staticmethod
    def seasonal_discount(order):
        return sum(Discount.apply_discount(product.price, 10) for product in order.products)

    @staticmethod
    def promo_code_discount(order, promo_percent):
        return sum(Discount.apply_discount(product.price, promo_percent) for product in order.products)
