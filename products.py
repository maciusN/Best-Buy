class Product:
    """
    A class to represent a product in the store.

    Attributes:
    name (str): Name of the product.
    price (int, float): Price of the product.
    quantity (int): Quantity of the product in stock.
    active (bool): Boolean indicating if the product is active.
    """
    def __init__(self, name, price, quantity, active=True):
        """
        Initialize a new product instance.

        :param name: Name of the product.
        :param price: Price of the product.
        :param quantity: Quantity of the product in stock.
        :param active: Boolean indicating if the product is active.
        """
        
        if not isinstance(name, str) or not name:
            raise Exception("Invalid Name")
        self.name = name

        
        if not isinstance(price, (int, float)) or price <= 0:
            raise Exception("Invalid Price")
        self.price = price

        
        if not isinstance(quantity, int) or quantity < 0:
            raise Exception("Invalid Quantity")
        self.quantity = quantity

        if not isinstance(active, bool):
            raise Exception("Invalid Active Status")
        self.active = active

    def get_quantity(self) -> float:
        """
        Get the quantity of the product as a float.

        :return: Quantity of the product.
        """
        return float(self.quantity)

    def set_quantity(self, quantity):
        """
        Set the quantity of the product. Deactivates the product if quantity is zero.

        :param quantity: New quantity of the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """
        Check if the product is active.

        :return: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activate the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product.
        """
        self.active = False

    def show(self) -> str:
        """
        Display the product details.

        :return: String representation of the product details.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Buy a certain quantity of the product. Reduces the stock and returns the total price.

        :param quantity: Quantity to buy.
        :return: Total price for the quantity bought.
        :raises Exception: If the quantity is invalid or insufficient.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            print("Invalid Quantity")
        if quantity > self.quantity:
            print("Insufficient Quantity")
        else:
            total_price = quantity * self.price
            self.set_quantity(self.quantity - quantity)
            return total_price
    