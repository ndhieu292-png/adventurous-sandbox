users = []
def user_system():
    menu = ["1. Register", "2. Login", "3. Exit"]
    for task in menu:
        print(task)
    while True:
        choice = input("Enter option: ")
        if choice == "1":
            username = input("Your username: ")
            password = input("your password: ")
            user = {"username": username, "password": password, "cart":  [], "history": []}
            users.append(user)
            print("Success")
        elif choice == "2":
            login_username = input("Your username: ")
            login_found = False
            for user in users:
                if login_username == user["username"]:
                    login_found = True
                    login_password = input("Your password, q for quit: ")
                    while True:
                        if login_password == "q":
                            break
                        elif login_password == user["password"]:
                            print("Success")
                            user_menu()
                        else:
                            print("Fail")
                            break
            if login_found == False:
                print("Not available")
                break
        elif choice == "3":
            break
        else:
            print("Invalid")
products = []
def create_product():
    product_id = input("Your product id: ")
    name = input("Your product:")
    price = int(input("Enter prise: "))
    stock = int(input("Enter stock: "))
    new_product = {"id": product_id,"name": name,"price": price,"stock": stock}
    products.append(new_product)
def stock_management(item):
    print(f"Current stock: {item['stock']}")
    new_stock = int(input("Enter new stock: "))
    item["stock"] = new_stock
    print("Stock updated!")
def search_product(keyword):
    matches = []
    for product in products:
        if keyword == product["id"] or keyword in product["name"]:
            matches.append(product)
    return matches
def product_menu():
    menu = ["1. Add product", "2. Show lists", "3. Search", "4. Stock management", "5. Exit"]
    for task in menu:
        print(task)
    while True:
        option = input("Choose your option: ")
        if option == "1":
            create_product()
        elif option == "2":
            for product in products:
                print(product)
        elif option == "3":
            while True:
                keyword = input("Enter id or name of product, q for quit: ")
                if keyword == "q":
                    break
                matches = search_product(keyword)
                if len(matches) == 0:
                    print("Not available")
                for item in matches:
                    print(item)
        elif option == "4":
            while True: 
                name_product = input("Enter your product id or name, q for quit: ")
                found = False
                for item in products:
                    if name_product == item["id"] or name_product == item["name"]:
                        found = True
                        stock_management(item)
                if found == False:
                    print("Invalid")
                elif name_product == "q":
                    break
        elif option == "5":
            break
        else:
            print("Invalid")
def add_cart(user):
    product_id = input("Choose id product: ")
    quantity = int(input("Enter quantity: "))
    cart = {"product_id": product_id, "quantity": quantity}
    user["cart"].append(cart)
def remove_cart(id_cart, user):
    while True:
        found = False
        for cart in user["cart"]:
            if id_cart == cart["product_id"]:
                found = True
                user["cart"].remove(cart)
        if found == False:
            break
def quantity_cart(itemcart):
    print(f"Current cart quantity is {itemcart['quantity']}")
    new_quantity = int(input("Enter new quantity: "))
    itemcart["quantity"] = new_quantity
    print("Quantity cart updated!")
def cart_system(user):
    menu_cart = ["1. Add to cart", "2. Remove from cart", "3. Change quantity"]
    while True:
        for item in menu_cart:
            print(item)
        cart_choice = input("Choose your option, q for quit: ")
        if cart_choice == "1":
            while True:
                for product in products:
                    print(product)
                option = input("1. Add cart\n2. Done\n")
                if option == "1":
                    add_cart()
                elif option == "2":
                    break
        elif cart_choice == "2":
            while True:
                for item in user["cart"]:
                    print(item)
                option = input("1. Remove", "2. Done")
                if option == "1":
                    id_cart = input("Choose id cart: ")
                    remove_cart(id_cart)
                elif option == "2":
                    break
        elif cart_choice == "3":
            while True:
                if len(user["cart"]) == 0:
                    print("Empty cart")
                    break
                for itemcart in user["cart"]:
                    print(itemcart)
                option = input("Choose your id cart, q for quit: ")
                if option == "q":
                    break
                found = False
                for itemcart in user["cart"]:
                    if option == itemcart["product_id"]:
                        found = True
                        quantity_cart(itemcart)
                        break
                if found == False:
                    print("Invalid")
        elif cart_choice == "q":
            break
def checkout(user):
    order_items = []
    for itemcart in user["cart"]:
        for item in products:
            if itemcart["product_id"] == item["id"]:
                if itemcart["quantity"] > item["stock"]:
                    print("Insufficient stock")
                    return False
    total = 0
    for itemcart in user["cart"]:
        for item in products:
            if itemcart["product_id"] == item["id"]:
                if itemcart["quantity"] <= item ["stock"]:
                    item["stock"] -= itemcart["quantity"]
                    order_items.append({"id": item['id'], "qty": itemcart['quantity'], "price": item['price']})
                    qty = itemcart['quantity']
                    total += qty * item['price']
    order = {"items": order_items, "total": total}
    user["history"].append(order)
    user["cart"].clear()
    return True
def user_menu(user):
    user_menu = ["1. Search", "2. Cart system", "3. View cart", "4. Checkout", "5. Log out"]
    while True:
        for item in user_menu:
            print(item)
        choice = input("Choose option: ")
        if choice == "1":
            keyword = input("Enter your product id or name: ")
            matches = search_product(keyword)
            if len(matches) == 0:
                print("Not available")
            for item in matches:
                print(item)
        elif choice == "2":
            cart_system()
        elif choice == "3":
            for itemcart in user["cart"]:
                print(itemcart)
        elif choice == "4":
            checkout()
        elif choice == "5":
            break
        else:
            print("Invalid")
                
while True:
    choice = input("Choose your role 1. admin 2. user: ")
    if choice == "1":
        menu = ["1. Add product", "2. Search product", "3. Stock management", "4. Exit"]
        while True:
            for item in menu:
                print(item)
            choice = input("Choose your option: ")
            if choice == "1":
                create_product()
            elif choice == "2":
                keyword = input("Enter name or id product: ")
                search_product(keyword)
            elif choice == "3":
                productname = input("Enter name or id product: ")
                found = False
                for item in products:
                    if productname == item["id"] or productname == item["name"]:
                        found = True
                        stock_management(item)
                if found == False:
                    break
            elif choice == "4":
                break
    if choice == "2":
        user_system()

                    

                    










