from account import Account
from transaction import deposite,withdraw
acc = Account("neha",10000)
acc.show_balance()
deposite(acc,500)
withdraw(acc,300)
acc.show_balance()