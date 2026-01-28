def deposite(account,amt):
     account.balance+=amt
     print(f"deposited {amt}")

def withdraw(account,amt):
     if amt <=account.balance:
          account.balance -= amt
          print(f" withdrwan {amt}")
     else:
          print("Insufficient balance")
     
