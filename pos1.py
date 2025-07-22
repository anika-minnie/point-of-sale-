# n Pos stelsel in python
# Lys vir die gekoopde produkte
cart = []

#produkte lys
products = [
("kaas", 50.00),
("melk", 30.00),
("brood", 15.00)    
]

def display_products():

    # Vertoon beskikbare produkte
    print("\nBeskikbare Produkte:")
    for idx, (name, price) in enumerate(products, 1):
        print(f"{idx}. {name} - R{price:.2f}")

#vertoon beskikbare produkte
    def add_product():  
            display_products()
            choice= input("Add produkte by(1-3): ") 
            if choice in ['1', '2', '3']:
                idx = int(choice) - 1
                cart.append(products[idx])
                print(f"{products[idx][0]} bygevoeg.")  

            else:
                print("Ongeldige keuse.")
                display_cart()      
    def display_cart(): 
         
    # Vertoon alle produkte in die cart en die totale prys
        if not cart:
         print("\ncart is leeg.")
         return
    print("\nItems in cart:")
    total = 0
    print("Exiting POS system.")
    
    for name, price in cart:
        print(f"- {name}: R{price:.2f}")
        total += price
        print(f"total: R{total:.2f}")   

# Cart te delete 
    def delete_cart():  
        cart.clear()
        print("Cart is delete.") 
    def main():    
              sentinel = False
              while not sentinel:   
                    print("\nPOS Menu:")
                    print("1. Add Product")
                    print("2. Display Cart")
                    print("3. Delete Cart")
                    print("4. Exit")
                    option = input("Select an option (1-4): ")
                    if option == '1':
                        add_product()
                    elif option == '2':
                        display_cart()
                    elif option == '3':
                        delete_cart()
                    elif option == '4':
                        sentinel = True
                        print("Exiting POS system. Goodbye!")
                    else:
                        print("Invalid option. Please try again.")

                        if __name__ == "__main__":  
                             
                             
                            main()


         
    