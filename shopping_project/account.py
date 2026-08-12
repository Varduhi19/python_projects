class product:
    def __init__(self, name, prise, stock=10):
        self.name = name
        self.prise = prise
        self.stock = stock

    def __str__(self):
        return f"{self.name}"

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.logs = []

    def add_product(self, product, quantity=1):
        if product.stock >= quantity:
            product.stock -= quantity
            for i in range(quantity):
                self.items.append(product)
            self.logs.append(f"Ավելացվեց {quantity} հատ {product.name}:")
        else:
            self.logs.append(f"Պահեստում չկա բավարար {product.name}: Առկա է՝ {product.stock} հատ:")
        
        
    def remove_product(self, product, count=1):
        removed_count = 0
        for i in range(count):
            if product in self.items:
                removed_count += 1
                self.items.remove(product)
                product.stock += 1
            else:
                break
        self.logs.append(f"Ջնջվեց {removed_count} հատ {product.name}:")

    def get_total(self):
        cost = 0
        for item in self.items:
            cost += item.prise
        return cost  # print-ի փոխարեն return ենք անում, որ FastAPI-ն ստանա գումարը

class ShoppingAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.cart-ը դարձնում ենք ձեր ShoppingCart() կլասի օբյեկտ
        self.cart = ShoppingCart()
        self.balance = 100.0

    def check_password(self, password_input):
        return self.password == password_input


# Օգտատերերի բազան
users_database = {
    "arman": ShoppingAccount("arman", "password123"),
    "admin": ShoppingAccount("admin", "admin2026")
}

# Օրինակելի ապրանքներ
laptop = product("Laptop", 1200, 5)
phone = product("iPhone", 800, 3)




    