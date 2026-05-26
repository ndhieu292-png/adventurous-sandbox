def user_menu():
    user_menu = ["1. Search", "2. Cart system", "3. View cart", "4. Checkout", "5. Log out"]
    while True:
        for item in user_menu:
            print(item)
        choice = input("Choose option: ")
        if choice == "1":
            keyword = input("Enter your product id or name: ")
            search_product(keyword)
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
def checkout():
    for itemcart in user["cart"]:
        for item in products:
            if itemcart["product_id"] == item["id"]:
                quantity = itemcart["quantity"]
                if quantity <= item["stock"]:
                    item["stock"] -= quantity
                    break
                else:
                    print("Insufficient stock, please change your cart quantity!")
                    break
        user["cart"].clear()
            

