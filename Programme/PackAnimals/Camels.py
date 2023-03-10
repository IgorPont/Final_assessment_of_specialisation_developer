from Programme.PackAnimals.PackAnimalsAbstract import PackAnimalsAbstract


class Camels(PackAnimalsAbstract):
    '''Класс верблюды'''

    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

    def eat(self):
        """Верблюд умеет есть"""
        pass

    def speak(self):
        """Верблюд умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Верблюд: кличка - {self.__name}, дата рождения - {self.__birth_date}')