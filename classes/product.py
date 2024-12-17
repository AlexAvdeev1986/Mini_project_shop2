class Product:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("Цена товара должна быть положительным числом")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} руб."

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


# Новый тип продукта: Бытовая химия
class HouseholdChemical(Product):
    def __init__(self, name, price, chemical_type):
        super().__init__(name, price)
        self.chemical_type = chemical_type  # Тип бытовой химии (например, "моющее средство")

    def __str__(self):
        return f"{self.name} ({self.chemical_type}): {self.price} руб."

    def __repr__(self):
        return (f"HouseholdChemical(name='{self.name}', price={self.price}, "
                f"chemical_type='{self.chemical_type}')")
