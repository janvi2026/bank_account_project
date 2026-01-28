class Account:
     def __init__(self,name,balance=0):
          self.name = name
          self.balance = balance
     def show_balance(self):
          print(f"name :{ self.name} balance:{self.balance}" )
