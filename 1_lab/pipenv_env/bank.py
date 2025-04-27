class BankAccount:
    __hidden_global = 10

    def __init__(self, owner: str, balance: float):
        self.owner = owner        # Публічний атрибут
        self.__balance = balance  # Приватний атрибут (інкапсульований)
    
    def __Incapsulation_method(self):
        print(f"Класова прихована змінна: {self.__hidden_global}")

    def deposit(self, amount: float):
        """Додає кошти на рахунок"""
        if amount > 0:
            self.__balance += amount
            print(f"Депозит {amount} успішний. Новий баланс: {self.__balance}")
        else:
            print("Сума повинна бути більше 0!")

    def withdraw(self, amount: float):
        """Знімає кошти з рахунку, якщо баланс дозволяє"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount}. Залишок на рахунку: {self.__balance}")
        else:
            print("Недостатньо коштів або некоректна сума!")

    @property
    def get_balance(self):
        """Надає доступ до балансу (через метод, а не напряму)"""
        return self.__balance