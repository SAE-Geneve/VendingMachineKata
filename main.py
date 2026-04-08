import os
from vending_machine import VendinMachine
from coin import Coin, type_coin
from products_list import Products

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n===== VENDING MACHINE =====")
    print("1. Insert coin")
    print("2. Select product")
    print("3. Show balance")
    print("4. Look inside the machine")
    print("5. Cancel (return coins)")
    print("6. Quit")
    print("===========================")

def display_products(vm):
    print("\n--- Products ---")
    for i, (name, price) in enumerate(Products.items(), 1):
        stock = vm.products_number.get(name, 0)
        print(f"  {i}. {name} - ${price:.2f} (stock: {stock})")

def display_coins():
    print("\n--- Coins ---")
    for i, name in enumerate(type_coin, 1):
        print(f"  {i}. {name}")

def main():
    vm = VendinMachine()
    product_names = list(Products.keys())

    clear()
    print("Welcome to the Vending Machine!")

    while True:        
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            clear()
            display_coins()
            coin_choice = input("Choose a coin (1-4): ").strip()
            if coin_choice in ("1", "2", "3", "4"):
                clear()
                coin = Coin(type_coin[int(coin_choice) - 1])
                vm.InsertCoin(coin)
                vm.CalculeValue()
            else:
                clear()
                print("Invalid choice.")

        elif choice == "2":
            clear()
            display_products(vm)
            product_choice = input("Choose a product (number): ").strip()
            if product_choice.isdigit() and 1 <= int(product_choice) <= len(product_names):
                name = product_names[int(product_choice) - 1]
                price = Products[name]
                if vm.products_number.get(name, 0) <= 0:
                    clear()
                    print(f"{name} is out of stock!")
                elif vm.valueTotal < price:
                    clear()
                    print(f"Not enough money. {name} costs ${price:.2f}, you have ${vm.valueTotal:.2f}")
                else:
                    clear()
                    vm.valueTotal -= price
                    vm.products_number[name] -= 1
                    print(f"Dispensed: {name}! Remaining balance: ${vm.valueTotal:.2f}")
            else:
                clear()
                print("Invalid choice.")

        elif choice == "3":
            clear()
            print(f"Current balance: ${vm.valueTotal:.2f}")

        elif choice == "4":
            clear()
            print("\n===== INSIDE THE MACHINE =====")
            print("\n--- Products in stock ---")
            for name, price in Products.items():
                stock = vm.products_number.get(name, 0)
                status = f"{stock} left" if stock > 0 else "EMPTY"
                print(f"  {name} - ${price:.2f} : {status}")
            print(f"\n--- Inserted coins ---")
            if vm.money:
                for coin in vm.money:
                    print(f"  {coin.name}")
            else:
                print("  No coins inserted.")
            print(f"\n--- Total balance: ${vm.valueTotal:.2f} ---")
            print("==============================")

        elif choice == "5":
            clear()
            print(f"Returning ${vm.valueTotal:.2f}")
            vm.Cancel()
            print("Coins returned.")

        elif choice == "6":
            clear()
            if vm.valueTotal > 0:
                print(f"Returning ${vm.valueTotal:.2f}")
                vm.Cancel()
            print("Goodbye!")
            break

        else:
            clear()
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
