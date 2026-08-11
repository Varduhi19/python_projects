class Product:
    def __init__(self, name, prise, stock=10):
        self.name=name
        self.prise=prise
        self.stock=stock
class ShoppingCard:
       def __init__(self):
            self.items=[]
       def add_product(self,product, quantity = 1):
           if product.stock>=quantity:
               self.items.append({"product": product, "quantity": quantity})
               product.stock-=quantity
               print("apranqy hajoxutyamb avelacvel e")
           else:
               print("verjacel e")
       def get_total(self):
            total=0
            for i in self.items:
                total+=i["product"].prise * i["quantity"]
            return total
        
pr1 = Product("Phone", 500, stock=5)
pr2 = Product("Headphones", 50, stock=10)

cart = ShoppingCard()
cart.add_product(pr1, 2)  # 2 * 500 = 1000
cart.add_product(pr2, 3)  # 3 * 50 = 150

print("Total:", cart.get_total())  # Կտպի 1150