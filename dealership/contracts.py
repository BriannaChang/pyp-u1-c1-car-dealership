
class Contract(object):
  def __init__(self, vehicle, customer):
    self.vehicle = vehicle 
    self.customer = customer
    self.total = 0
  
  def total_value(self):
    if self.customer.is_employee(): 
       self.total=  self.total * 0.9
    return self.total
  
  def monthly_value(self):
    self.total = self.total_value()
    monthly_value = self.total / self.MONTH
    return monthly_value
      


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
      super(BuyContract, self).__init__(vehicle, customer)
      self.monthly_payments = monthly_payments
      self.MONTH = monthly_payments
      
    def total_value(self): 
      sales_price = self.vehicle.sale_price()
      I = self.vehicle.INTEREST_RATE
      self.total = sales_price + ((I * self.monthly_payments * sales_price) / 100)
      super(BuyContract, self).total_value()
      return self.total


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
      super(LeaseContract, self).__init__(vehicle, customer)
      self.contract = 'lease'
      self.length_in_months = length_in_months
      self.MONTH = length_in_months
   
    def total_value(self): 
      sales_price = self.vehicle.sale_price()
      lease_multiplier = (sales_price * self.vehicle.LEASE_MULTIPLIER / self.length_in_months)
      self.total = sales_price + lease_multiplier
      super(LeaseContract, self).total_value()
      return self.total
