class Product:
    def __init__(self, name="Maciej", price=1, quantity=15, active=True):
        self.name = name
        if not isinstance(self.name, str) or not self.name:
            raise Exception("Invalid Name")

        self.price = price
        if not isinstance(self.price, (int, float)) or self.price <= 0:
            raise Exception("Invalid Price")

        self.quantity = quantity
        if not isinstance(self.quantity, int) or self.quantity < 0:
            raise Exception("Invalid Quantity")

        if not isinstance(active, bool):
            raise Exception("Invalid Active Status")
        self.active = active

    def get_quantity(self) -> float:
        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        if self.active == True:
            return True
        else:
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        self.quantity = self.quantity - quantity
        return float(self.price)

