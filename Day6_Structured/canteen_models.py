"""
A small module used by Lesson 07.

It holds the classes of the canteen. The program that takes orders is in
07_mini_project_canteen_orders.py and imports these classes from here.
"""
from abc import ABC, abstractmethod


class MenuItem:
    """One thing the canteen sells."""
    gst_rate = 5                        # class attribute: shared by all items

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_gst(self):
        return round(self.price * (100 + MenuItem.gst_rate) / 100, 2)

    def __str__(self):
        return f"{self.name:<10} Rs {self.price}"


class Combo(MenuItem):
    """A MenuItem sold at a discount. Inheritance: a Combo IS A MenuItem."""

    def __init__(self, name, price, discount_percent):
        super().__init__(name, price)
        self.discount_percent = discount_percent

    def price_with_gst(self):           # override, reusing the parent's work
        full = super().price_with_gst()
        return round(full * (100 - self.discount_percent) / 100, 2)


class Payment(ABC):
    """Abstraction: every payment must be able to pay."""

    @abstractmethod
    def pay(self, amount):
        pass


class Upi(Payment):
    def pay(self, amount):
        return f"Rs {amount} paid by UPI"


class Cash(Payment):
    def pay(self, amount):
        rounded = round(amount)         # the counter has no small coins
        return f"Rs {rounded} paid in cash"


class Order:
    """Encapsulation: items are added only through add()."""

    def __init__(self, customer):
        self.customer = customer
        self._items = []

    def add(self, item, quantity=1):
        if quantity <= 0:
            print("Quantity must be at least 1")
            return
        for _ in range(quantity):
            self._items.append(item)

    @property
    def total(self):
        return round(sum(item.price_with_gst() for item in self._items), 2)

    def __len__(self):
        return len(self._items)

    def checkout(self, payment):        # polymorphism: any Payment works
        return f"{self.customer}: {payment.pay(self.total)}"


# Runs only with:  python canteen_models.py   (Day 5, Lesson 08)
if __name__ == "__main__":
    tea = MenuItem("Tea", 10)
    print(tea, "->", tea.price_with_gst())      # Tea        Rs 10 -> 10.5
