class Product():
    def __init__ (self, name, price):
        self.name = name
        self.price = price
class Buyer ():
    def __init__ (self, name, balance):
        self.name = name 
        self.balance = balance 
class Basket():
    def __init__(self, buyer, name_product: Product):
       self.buyer = buyer 
       self.name_product = name_product
    def get_total_price(self):
       tp = 0
       for i in self.name_product:
          tp += i.price
       return tp
class Order():
    def __init__(self, product_card: Basket):
        self.product_card = product_card
        self.is_closed = False

    def close_order(self):
        if self.product_card.buyer.balance > self.product_card.get_total_price():
            self.is_closed = True
        return {"success": True}
     