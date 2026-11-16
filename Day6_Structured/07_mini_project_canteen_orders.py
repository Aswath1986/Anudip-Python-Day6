"""
==========================================================================
 Day 6 | Lesson 07 : Mini Project, Canteen Orders
==========================================================================
 First principle
   Yesterday's canteen bill was built from functions. Today the same
   canteen is built from objects: each thing in the real canteen (an item,
   an order, a payment) becomes a class that keeps its own data and rules.

 Find each idea in this file and in canteen_models.py
   1. Class and object          MenuItem, Order
   2. Class attribute           MenuItem.gst_rate
   3. Encapsulation             Order._items, Order.total
   4. Inheritance               Combo(MenuItem)
   5. Polymorphism              order.checkout(Upi()) / checkout(Cash())
   6. Abstraction               Payment(ABC)
   7. From Day 5                import, lambda, map, filter, sorted

 Run this file :  python 07_mini_project_canteen_orders.py
==========================================================================
"""
from canteen_models import MenuItem, Combo, Order, Upi, Cash, Payment

# --------------------------------------------------------------------------
# 1. The menu: objects in a dict
# --------------------------------------------------------------------------
menu = {
    "tea": MenuItem("Tea", 10),
    "samosa": MenuItem("Samosa", 15),
    "dosa": MenuItem("Dosa", 40),
    "meal": Combo("Meal combo", 100, discount_percent=10),
}

print("MENU")
for item in sorted(menu.values(), key=lambda i: i.price):
    print(" ", item)

# --------------------------------------------------------------------------
# 2. Two orders, two objects, separate data
# --------------------------------------------------------------------------
asha_order = Order("Asha")
asha_order.add(menu["tea"], 2)
asha_order.add(menu["dosa"])

ravi_order = Order("Ravi")
ravi_order.add(menu["meal"])
ravi_order.add(menu["samosa"], 3)
ravi_order.add(menu["tea"], 0)          # Quantity must be at least 1

print(len(asha_order), "items, total", asha_order.total)    # 3 items, total 63.0
print(len(ravi_order), "items, total", ravi_order.total)    # 4 items, total 141.75

# --------------------------------------------------------------------------
# 3. One checkout line, any kind of payment
# --------------------------------------------------------------------------
print(asha_order.checkout(Upi()))       # Asha: Rs 63.0 paid by UPI
print(ravi_order.checkout(Cash()))      # Ravi: Rs 142 paid in cash

# --------------------------------------------------------------------------
# 4. Day 5 tools work on objects too
# --------------------------------------------------------------------------
orders = [asha_order, ravi_order]

totals = list(map(lambda order: order.total, orders))
print(totals)                           # [63.0, 141.75]

big = list(filter(lambda order: order.total > 100, orders))
print([order.customer for order in big])        # ['Ravi']

# --------------------------------------------------------------------------
# 5. A new requirement, with no change to canteen_models.py
# --------------------------------------------------------------------------
class MealCoupon(Payment):              # the contract tells us what to write
    def pay(self, amount):
        return f"Rs {amount} paid by meal coupon"

print(asha_order.checkout(MealCoupon()))        # Asha: Rs 63.0 paid by meal coupon


# ==========================================================================
# TRY IT YOURSELF
#   1. Add "coffee" at Rs 20 to the menu and order two for a third customer.
#   2. Add a Card payment that adds a 2 percent fee.
#   3. Add a method remove_last() to Order in canteen_models.py.
#   4. Change MenuItem.gst_rate to 12 at the top of this file and run it
#      again. How many lines did you change, and how many totals changed?
#   5. Print the customer with the highest total using max(..., key=...).
# ==========================================================================
