class Customer:
    def __init__(self, customer_id, name, email, password):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password

    def welcoming(self):
        print(f"Welcome back, {self.name}!")

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, customer, cart):
        
        self.order_id = order_id
        self.customer = customer
        self.cart = cart
    
    def place_order(self):
        print(f"Order placed by {self.customer.name} with order ID {self.order_id}.")
        print("Ordered items:")
        for item in self.cart.items:
            print(f"{item['quantity']} x {item['product'].name}")