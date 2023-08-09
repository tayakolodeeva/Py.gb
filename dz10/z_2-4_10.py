""" 
2.Доработаем задания 5-6. Создайте класс-фабрику.
3.Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
4.Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

"""

from enum import Enum

class Animal:
    def __init__(self, name: str, color: str, size: float):
        self.name = name
        self.color = color
        self.size = size

    def show_unique(self):
        pass

    def get_animal_info(self):
        return f'Name: {self.name}, color: {self.color}, size: {self.size}'


class Fish(Animal):
    def __init__(self, name: str, color: str, size: float, max_depth: float = None):
        super().__init__(name, color, size)
        self.max_depth = max_depth

    def show_unique(self):
        print(f'Max depth: {self.max_depth}')

    def get_animal_info(self):
        return f'{super().get_animal_info()}, max depth: {self.max_depth}'


class Bird(Animal):
    def __init__(self, name: str, color: str, size: float, max_height: float = None):
        super().__init__(name, color, size)
        self.max_height = max_height

    def show_unique(self):
        print(f'Max height: {self.max_height}')

    def get_animal_info(self):
        return f'{super().get_animal_info()}, max height: {self.max_height}'


class Cat(Animal):
    def __init__(self, name: str, color: str, size: float, hairy: bool = None):
        super().__init__(name, color, size)
        self.hairy = hairy

    def show_unique(self):
        print(f'Is hairy: {self.hairy}')

    def get_animal_info(self):
        return f'{super().get_animal_info()}, is hairy: {self.hairy}'


class Animals(Enum):
    cat = Cat
    fish = Fish
    bird = Bird

class Factory:
    def __init__(self):
        self.animals = []

    def create_animal(self, animal_class: Animals, name: str, color: str, size: float, *args, **kwargs) -> Animal:
        new_animal = animal_class.value(name, color, size, *args, **kwargs)
        self.animals.append({'type': animal_class.name, 'animal': new_animal})
        return new_animal

    def show_animals(self):
        for number, animal in enumerate(self.animals):
            print(f'{number + 1}. Type: {animal["type"]}. {animal["animal"].get_animal_info()}')

if __name__ == '__main__':
    factory = Factory()
    cat_1 = factory.create_animal(Animals.cat, 'Bars', 'red', 27.5, False)
    bird_1 = factory.create_animal(Animals.bird, 'Eagle', 'blue', 13.0, 85)
   
    factory.show_animals()