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
