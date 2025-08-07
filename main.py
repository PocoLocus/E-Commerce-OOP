class Item:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"

class Product(Item):
    def __init__(self, id, name, price):
        super().__init__(id, name, price)

class Service(Item):
    def __init__(self, id, name, price, duration):
        super().__init__(id, name, price)
        self.duration = duration

    def __str__(self):
        return f"{self.name} - {self.duration} hrs (${self.price})"

class ShoppingCart:
    def __init__(self):
        self.cart_list = []

    def add_item(self, new_item):
        self.cart_list.append(new_item)

    def list_items(self):
        for item in self.cart_list:
            print(f"{item}")

    def get_total(self):
        return sum(item.price for item in self.cart_list)

class Order:
    def __init__(self, my_cart):
        self.cart = my_cart

    def send_order(self):
        print("Order details")
        self.cart.list_items()
        print(f"Total: {self.cart.get_total()}$")
        print("The order has been sent!")


item_1 = Product(1, "t-shirt", 10)
item_2 = Product(2, "pants", 20)
item_3 = Service(3, "support", 5, 10)

my_cart = ShoppingCart()
my_cart.add_item(item_1)
my_cart.add_item(item_2)
my_cart.add_item(item_3)

final_order = Order(my_cart)
final_order.send_order()
