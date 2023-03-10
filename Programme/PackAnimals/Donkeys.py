from Programme.PackAnimals.PackAnimalsAbstract import PackAnimalsAbstract


class Donkeys(PackAnimalsAbstract):
    '''Класс ослы'''

    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

    def eat(self):
        """Осел умеет есть"""
        pass

    def speak(self):
        """Осел умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Осел: кличка - {self.__name}, дата рождения - {self.__birth_date}')