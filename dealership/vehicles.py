

class Vehicle(object):
 
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model 
        self.year = year 
        self.base_price = base_price
        self.miles = miles 
        
    def sale_price(self):
      S = self.SALE_MULTIPLIER
      self.sales_price = self.base_price * S
      return self.sales_price
    
    def purchase_price(self):
      P = self.PURCHASE_MULTIPLIER
      self.purchase_price = self.sale_price() - (P * self.miles)
      return self.purchase_price
      
class Car(Vehicle):
  SALE_MULTIPLIER = 1.2 
  PURCHASE_MULTIPLIER = 0.004
  INTEREST_RATE = 1.07
  LEASE_MULTIPLIER = 1.2

class Motorcycle(Vehicle):
  SALE_MULTIPLIER = 1.1
  PURCHASE_MULTIPLIER = 0.009
  INTEREST_RATE = 1.03
  LEASE_MULTIPLIER = 1


class Truck(Vehicle):
  SALE_MULTIPLIER = 1.6
  PURCHASE_MULTIPLIER = 0.02
  INTEREST_RATE = 1.11
  LEASE_MULTIPLIER = 1.7
