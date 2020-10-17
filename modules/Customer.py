from .Account import Account

class Customer(Account):
    customerID = ""
    def __init__(self, id):
        self.customerID = id
    
