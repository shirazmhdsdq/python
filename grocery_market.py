# Grocery Market CLI App

# Sample product list
products = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40,
    "rice": 60,
    "eggs": 5
}

# Cart to store user purchases
cart = {}

def show_products():
    print("\n🛒 Available Products:")
    for item, price in products.items():
        print(f"- {item.capitalize()} : ₹{price}")
    print()

def add_to_cart():
    item = input("Enter item name to add: ").lower()
    if item in products:
        qty = int(input(f"How many {item}s? "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"✅ Added {qty} {item}(s) to your cart.\n")
    else:
        print("❌ Item not found in store.\n")

def view_cart():
    if not cart:
        print("🛒 Your cart is empty.\n")
        return

    print("\n🧾 Your Cart:")
    total = 0
    for item, qty in cart.items():
        price = products[item]
        item_total = price * qty
        total += item_total
        print(f"- {item.capitalize()} x {qty} = ₹{item_total}")
    print(f"Total: ₹{total}\n")

def checkout():
    if not cart:
        print("🛒 Your cart is empty. Nothing to checkout.\n")
        return

    print("\n🧾 Final Bill:")
    total = 0
    for item, qty in cart.items():
        price = products[item]
        item_total = price * qty
        total += item_total
        print(f"- {item.capitalize()} x {qty} = ₹{item_total}")
    print(f"\n🟩 Total Amount Due: ₹{total}")
    print("✅ Thank you for shopping with us!\n")
    cart.clear()  # Empty the cart after checkout

def main():
    while True:
        print("📍 Grocery Market Menu")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            print("👋 Exiting Grocery Market. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
