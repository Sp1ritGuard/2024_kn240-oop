from Bank import BankAccount

# Демонстрація роботи
account = BankAccount("Іван", 1000)
print(account.owner)  # Публічний атрибут доступний
# print(account.__balance)  # Викличе помилку, бо атрибут приватний

account.deposit(500)
account.withdraw(300)
print("Поточний баланс:", account.get_balance)  

# Примусове звернення до приватного атрибута (небажано)
print("Прямий доступ:", account._BankAccount__balance)  # Можливий, але не рекомендований підхід