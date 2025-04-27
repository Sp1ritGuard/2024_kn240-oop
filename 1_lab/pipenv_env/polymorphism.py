# Приклад ПОЛІМОРФІЗМУ
# Базовий клас
from Inheritance import BaseDog, BaseCat, Animal

# Дочірні класи, що реалізують свій варіант методу make_sound()
class Dog(BaseDog):
    # def __init__(self, name):
    #     super().__init__(name)
    
    def make_sound(self):
        return super().make_sound() + " Woof!"

class Cat(BaseCat):
    # def __init__(self, name):
    #     super().__init__(name)
    
    def make_sound(self):
        return super().make_sound() + " Meow!" 

class Cow(Animal):
    # def __init__(self, name):
    #     super().__init__(name)
    
    def make_sound(self):
        return "Moo!"

# Функція, яка демонструє поліморфізм
def animal_sound(animal: Animal):
    """Приймає будь-який об'єкт, що наслідує Animal, і викликає make_sound()"""
    print(f"{animal.__class__.__name__} каже: {animal.make_sound()}")
