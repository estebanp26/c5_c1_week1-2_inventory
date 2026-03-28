inventory = []



def add_product():
    name       = input("Product name: ")
    unit_price = float(input("Unit price: "))
    quantity   = int(input("Quantity: "))

    # Validate that price and quantity are not negative
    if unit_price <= 0:
        print("Invalid value. Price cannot be zero or negative.")
        return
    if quantity <= 0:
        print("Invalid value. Quantity cannot be zero or negative.")
        return

    # Store the product as a dictionary inside the inventory list
    product = {"name": name, "price": unit_price, "quantity": quantity}
    inventory.append(product)
    print(f"Product '{name}' added successfully.")


def show_inventory():
    # Check if inventory is empty
    if not inventory:
        print("Inventory is empty.")
        return

    # Loop through each product and print it
    for product in inventory:
        print(f"Product: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")


def calculate_statistics():
    # Check if inventory is empty
    if not inventory:
        print("Inventory is empty. No statistics available.")
        return

    total_value    = 0
    total_products = 0

    # Loop through inventory to calculate totals
    for product in inventory:
        total_value    += product["price"] * product["quantity"]
        total_products += product["quantity"]

    print(f"Total products registered : {total_products}")
    print(f"Total inventory value     : {total_value}")


# This variable controls the loop
# When the user chooses Exit, it becomes False and the program stops
active = True

while active:
    print("\n--- INVENTORY SYSTEM MENU ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("Select an option (1-4): ")

    if option == "1":
        add_product()
    elif option == "2":
        show_inventory()
    elif option == "3":
        calculate_statistics()
    elif option == "4":
        print("Goodbye!")
        active = False
    else:
        print("Invalid option. Please enter a number from 1 to 4.")
