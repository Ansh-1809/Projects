def display_menu():
    print("\n===== Welcome to the Billing System =====")
    print("1. Add item")
    print("2. Show bill")
    print("3. Exit")

cart = []

while True:
    display_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        qty = int(input("Enter quantity: "))
        total = price * qty
        cart.append({'name': name, 'price': price, 'qty': qty, 'total': total})
        print(f"{name} added to cart.")
        
    elif choice == '2':
        print("\n===== Final Bill =====")
        grand_total = 0
        for item in cart:
            print(f"{item['name']} - {item['qty']} x {item['price']} = {item['total']}")
            grand_total += item['total']
        print(f"\nGrand Total: ₹{grand_total:.2f}")
        
    elif choice == '3':
        print("Thank you for using the billing system.")
        break
        
    else:
        print("Invalid choice. Please try again.")
