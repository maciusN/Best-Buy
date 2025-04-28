class Store:
    def __init__(self, products):
        """
        Initialize the store with a list of products.

        Args:
            products (list): A list of Product objects.
        """
        self.products = products

    def add_product(self, product):
        """
        Add a product to the store's product list.

        Args:
            product (Product): The product to be added.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store's product list.

        Args:
            product (Product): The product to be removed.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Get the total number of products in the store.

        Returns:
            int: The total number of products.
        """
        total_amount = 0
        for product in self.products:
            total_amount += product.quantity
        print(f"Total of {total_amount} items in store")

    def get_all_products(self):
        """
        Get a list of all active products in the store.

        Returns:
            list: A list of active products.
        """
        self.list = []
        for product in self.products:
            if product.active == True and product.quantity > 0:
                self.list.append(product)
        return self.list

    def order(self, shopping_list):
        """
        Process an order from the shopping list and calculate the total price.

        Args:
            shopping_list (list of tuples): 
            A list of tuples where each tuple contains a product and its quantity.

        Returns:
            float: The total price of the order.
        """
        sum_price = 0

        for product, quantity in shopping_list:
            if product not in self.products or not product.is_active():
                print(
                    f"The product '{product.name}' is not available in the store.")
            sum_price += product.buy(quantity)
        return sum_price
