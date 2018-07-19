interest_rate = {'car': 1.07, 'motorcycle': 1.03, 'truck': 1.11}
leaseMultiplier = {'car': 1.2, 'motorcycle': 1, 'truck': 1.7}

class Contract(object):
  def __init__(self, vehicle, customer):
    self.vehicle = vehicle 
    self.customer = customer
    self.total = 0
  
  def total_value(self):
    sales_price = self.vehicle.sale_price()
    if self.contract == 'buy': 
      I = interest_rate[self.vehicle.name]
      self.total = sales_price + ((I * self.monthly_payments * sales_price) / 100)
    else: 
      lease_multiplier = (sales_price * leaseMultiplier[self.vehicle.name] / self.length_in_months)
      self.total = sales_price + lease_multiplier
    if self.customer.is_employee(): 
       self.total=  self.total * 0.9
    return self.total
  
  def monthly_value(self):
    self.total = self.total_value()
    if self.contract == 'buy':
      monthly_value = self.total / self.monthly_payments
    else: 
      months = self.length_in_months
      monthly_value = self.total/ months
    return monthly_value
      


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
      Contract.__init__(self, vehicle, customer)
      self.contract = 'buy'
      self.monthly_payments = monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
      Contract.__init__(self, vehicle, customer)
      self.contract = 'lease'
      self.length_in_months = length_in_months
