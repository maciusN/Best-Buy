import products
import store


def main():
    """
    Main function to initialize the store with products and display the store menu.
    """
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds",
                                     price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    best_buy = store.Store(product_list)

    def start():
        menu = """
        Store Menu
        ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit"""
        print(menu)

    while True:
        start()

        user_input = int(input("Please choose a number: "))

        if user_input == 1:
            print("------")
            for product in product_list:
                print(f"{product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")
            print()
        elif user_input == 2:
            total_amount = 0
            for product in product_list:
                total_amount += product.quantity
            print(f"Total of {total_amount} items in store")
        elif user_input == 3:
            total_payment = 0
            print("------")
            for product in product_list:
                print(f"{product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")
            print("When you want to finish order, enter empty text.")
            while True:
                print()
                user_input_product = input("Which product do you want? ")
                user_input_amount = input("What amount do you want? ")
                if user_input_product in ("1","MacBook Air M2"):
                    total_payment += product_list[0].price * \
                        int(user_input_amount)
                    print("Product added to list!")
                elif user_input_product in ("2", "Bose QuietComfort Earbuds"):
                    total_payment += product_list[1].price * \
                        int(user_input_amount)
                    print("Product added to list!")
                elif user_input_product in ("3", "Google Pixel 7"):
                    total_payment += product_list[2].price * \
                        int(user_input_amount)
                    print("Product added to list!")
                elif user_input_product == "" and user_input_amount == "":
                    break
            print("********")
            print(f"Order made! Total payment = ${total_payment}")
        elif user_input == 4:
            break


if __name__ == "__main__":
    main()
