class Product:
    def __init__(self, name, price, stock=10):
        self.name=name
        self.price=price
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
                total+=i["product"].price * i["quantity"]
            return total
       def remove_product(self, product, count):
        
        for i in self.items:
            
            if i["product"] == product:
                
                product.stock += i["quantity"]
                
               
                self.items.remove(i)
                
                print(f"{product.name}-ը հեռացվեց զամբյուղից:")
                return  
        
        
        print(f"{product.name}-ը չկա ձեր զամբյուղում:")
        
pr1 = Product("Phone", 500, stock=5)
pr2 = Product("Headphones", 50, stock=10)

cart = ShoppingCard()
cart.add_product(pr1, 2) 
cart.add_product(pr2, 3)  
cart.remove_product(pr1, 3)

print("Total:", cart.get_total())  