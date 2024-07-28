
from Bank_accounts import Bank_Account

teste = Bank_Account(1000, "teste")
teste2 = Bank_Account(1200, "teste2")

teste.deposit(100)

teste.transfer(1100, teste2)