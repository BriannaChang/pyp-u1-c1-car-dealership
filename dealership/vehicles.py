multiplier = {'sale': {'car': 1.2 , 'motorcycle' : 1.1, 'truck': 1.6}, 'purchase': {'car': 0.004 , 'motorcycle': 0.009, 'truck': 0.02}}

class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model 
        self.year = year 
        self.base_price = base_price
        self.miles = miles 
        
    def sale_price(self):
      S = multiplier['sale'][self.name]
      self.sales_price = self.base_price * S
      return self.sales_price
    
    def purchase_price(self):
      P = multiplier['purchase'][self.name]
      self.purchase_price = self.sale_price() - (P * self.miles)
      return self.purchase_price
      
class Car(Vehicle):
  def __init__(self, maker, model, year, base_price, miles):
    Vehicle.__init__(self, maker, model, year, base_price, miles)
    self.name = 'car'


class Motorcycle(Vehicle):
  def __init__(self, maker, model, year, base_price, miles):
    Vehicle.__init__(self, maker, model, year, base_price, miles)
    self.name = 'motorcycle'


class Truck(Vehicle):
  def __init__(self, maker, model, year, base_price, miles):
    Vehicle.__init__(self, maker, model, year, base_price, miles)
    self.name = 'truck'
