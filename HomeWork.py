class product:
    def __init__(self,name,prise,stock=10):
        self.name = name
        self.prise = prise
        self.stock = stock

    def __str__(self):
        return f"{self.name}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self,product, quantity = 1):
        if product.stock >= quantity:
            product.stock -= quantity
            for i in range(quantity):
                self.items.append(product)
            print(*self.items)
        else:
            print(f"We not have enough {product}, the {product}s count: ", product.stock)
        
    def remove_product(self,product,count = 1):
        removed_count = 0
        for i in range(count):
            if product in self.items:
                removed_count += 1
                self.items.remove(product)
                product.stock += 1
            else:
                print(f"all {product} is deleted")
                break
        print(f"{removed_count} {product} has been deleted", "\n",*self.items )

        
    def get_total(self):
        cost = 0
        for product in self.items:
            cost += product.prise
        print(cost)


laptop = product("Laptop", 1200, 5)
phone = product("iPhone", 800, 3)


cart = ShoppingCart()


cart.add_product(laptop, 2)  
cart.add_product(phone, 5)   
cart.add_product(phone, 2)

cart.get_total() 

cart.remove_product(phone,3)
