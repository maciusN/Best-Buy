import products
import store


def start():
    menu = """
        Store Menu
        ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit"""
    print(menu)


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

    while True:
        
        start()

        user_input = int(input("Please choose a number: "))

        if user_input == 1:
            index = 1
            for product in best_buy.get_all_products():
                print(str(index) + ". " + product.show())
                index += 1
        elif user_input == 2:
            best_buy.get_total_quantity()
        elif user_input == 3:
            shopping_cart_sum = 0
            while True:
                index = 1
                for product in best_buy.get_all_products():
                    print(str(index) + ". " + product.show())
                    index += 1
                
                user_input_product = input("Which product # do you want? ")
                user_input_amount = input("What amount do you want? ")
                
                if user_input_product == "" and user_input_amount == "":
                    break
                try:
                    shopping_cart_sum += best_buy.order([(best_buy.get_all_products()[int(user_input_product) - 1], int(user_input_amount))])
                except (ValueError, IndexError):
                    print("Error adding product!")
                
            print(f"Order made! Total payment: {shopping_cart_sum}$")
            

        elif user_input == 4:
            break


if __name__ == "__main__":
    main()
