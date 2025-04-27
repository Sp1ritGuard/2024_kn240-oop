# Приклад АБСТРАКЦІЇ
from abc import ABC, abstractmethod

# Абстрактний клас
class Vehicle(ABC):
    def __init__(self, brand: str):
        self.brand = brand

    @abstractmethod
    def move(self):
        """Абстрактний метод, який має бути реалізований у підкласах"""
        pass
    
    @abstractmethod
    def stop (self):
        pass

# Дочірній клас Car реалізує абстрактний метод move
class Car(Vehicle):
    def move(self):
        return f"{self.brand} рухається по дорозі."
    
    def stop(self):
        return f"{self.brand} зупинився"

# Дочірній клас Boat реалізує абстрактний метод move
class Boat(Vehicle):
    def move(self):
        return f"{self.brand} пливе по воді."
    
    def stop(self):
        return f"{self.brand} пришвартувався"

# Дочірній клас Airplane реалізує абстрактний метод move
class Airplane(Vehicle):
    def move(self):
        return f"{self.brand} летить у повітрі."
    
    def stop(self):
        return f"{self.brand} приземлився"

