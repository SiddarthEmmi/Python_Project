import sys

print("DMART BILLING")
ls = []  # List of selected items
qr = []  # List of quantities
am = []  # List of amounts
ma = ['sugar', 'rice', 'salt', 'wheet', 'spoon', 'Tcup', 'plates', 'fork', 'shirt', 'pants', 'Tshirt', 'formals']

def mart():
    while True:
        print("\nDMART MENU")
        print("1. Shopping")
        print("2. Verification")
        print("3. Billing")
        print("4. Exit")
        try:
            ch = int(input("Enter your choice: "))
            if ch == 1:
                shop()
            elif ch == 2:
                verification()
            elif ch == 3:
                billing()
            elif ch == 4:
                print("Exiting... Thank you for shopping!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def shop():
    while True:
        print("\nShopping Categories:")
        print("1. Grocery")
        print("2. Kitchen")
        print("3. Clothes")
        print("4. Go to Main Menu")
        try:
            chh = int(input("Enter your choice: "))
            if chh == 1:
                grocery()
            elif chh == 2:
                kitchen()
            elif chh == 3:
                clothes()
            elif chh == 4:
                return  # Go back to the main menu
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def grocery():
    print("\nWelcome to Grocery Shopping")
    print("  Items       Price")
    print("1. Sugar       40/kg")
    print("2. Rice        50/kg")
    print("3. Salt        20/kg")
    print("4. Wheet       30/kg")
    print("5. Go to Shopping Menu")
    while True:
        try:
            c = int(input("Enter your choice: "))
            if c == 1:
                m = int(input("Enter the sugar quantity (kg): "))
                add_item("sugar", m, 40)
            elif c == 2:
                n = int(input("Enter the rice quantity (kg): "))
                add_item("rice", n, 50)
            elif c == 3:
                p = int(input("Enter the salt quantity (kg): "))
                add_item("salt", p, 20)
            elif c == 4:
                q = int(input("Enter the wheet quantity (kg): "))
                add_item("wheet", q, 30)
            elif c == 5:
                return  # Go back to shopping menu
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def kitchen():
    print("\nWelcome to Kitchen Shopping")
    print("  Items        Price")
    print("1. Spoon        30")
    print("2. Tcup         40")
    print("3. Plates       50")
    print("4. Fork         20")
    print("5. Go to Shopping Menu")
    while True:
        try:
            c = int(input("Enter your choice: "))
            if c == 1:
                r = int(input("Enter the spoon quantity: "))
                add_item("spoon", r, 30)
            elif c == 2:
                s = int(input("Enter the Tcup quantity: "))
                add_item("Tcup", s, 40)
            elif c == 3:
                t = int(input("Enter the plates quantity: "))
                add_item("plates", t, 50)
            elif c == 4:
                u = int(input("Enter the fork quantity: "))
                add_item("fork", u, 20)
            elif c == 5:
                return  # Go back to shopping menu
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def clothes():
    print("\nWelcome to Clothes Shopping")
    print("  Items        Price")
    print("1. Shirt        600")
    print("2. Pants        400")
    print("3. Tshirt       300")
    print("4. Formals      500")
    print("5. Go to Shopping Menu")
    while True:
        try:
            c = int(input("Enter your choice: "))
            if c == 1:
                v = int(input("Enter the shirt quantity: "))
                add_item("shirt", v, 600)
            elif c == 2:
                w = int(input("Enter the pants quantity: "))
                add_item("pants", w, 400)
            elif c == 3:
                x = int(input("Enter the Tshirt quantity: "))
                add_item("Tshirt", x, 300)
            elif c == 4:
                y = int(input("Enter the formals quantity: "))
                add_item("formals", y, 500)
            elif c == 5:
                return  # Go back to shopping menu
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_item(item, quantity, price_per_unit):
    total_price = quantity * price_per_unit
    ls.append(item)
    qr.append(quantity)
    am.append(total_price)
    print(f"Added {quantity} x {item} for {total_price}.")

def verification():
    print("\nVerification of Selected Items:")
    for item in ls:
        if item in ma:
            print(f"{item} is available in the shop.")
        else:
            print(f"{item} is not available in the shop.")

def billing():
    print("\nBilling Details")
    print("  Items      Quantity      Price")
    for x, y, z in zip(ls, qr, am):
        print(f"   {x}         {y}           {z}")
    total_amount = sum(am)
    print("Total Amount:             ", total_amount)

# Run the mart function
mart()
