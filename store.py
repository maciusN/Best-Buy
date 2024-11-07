import products


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return len(self.products)

    def get_all_products(self):
        self.list = []
        for product in self.products:
            if product.active == True:
                self.list.append(product)
        return self.list

    def order(self, shopping_list):
        sum_price = 0
        for product, quantity in shopping_list:
            if product not in self.products or not product.is_active():
                raise ValueError(
                    f"The product '{product.name}' is not available in the store.")
            sum_price += product.buy(quantity)
        return sum_price


bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

store = Store([bose, mac])
price = store.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")
