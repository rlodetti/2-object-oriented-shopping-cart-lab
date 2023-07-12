import numpy as np
class ShoppingCart:
    # write your code here
    def __init__(self,employee_discount = None):
        self.total = 0
        self.employee_discount = employee_discount
        self.items = []
      
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total
    
    def mean_item_price(self):
        prices = []
        for i in self.items:
            prices.append(i['price'])
        return np.mean(prices)

    def median_item_price(self):
        prices = []
        for i in self.items:
            prices.append(i['price'])
        return np.median(prices)

    def apply_discount(self):
        if self.employee_discount == None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            disc_total = self.total * (1-self.employee_discount/100)
            return disc_total
            

    def void_last_item(self):
        if self.items == []:
            return "There are no items in your cart!"
        else:
            self.total -= self.items.pop()['price']