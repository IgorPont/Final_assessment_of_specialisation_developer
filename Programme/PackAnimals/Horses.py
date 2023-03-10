from Programme.PackAnimals.PackAnimalsAbstract import PackAnimalsAbstract


class Horses(PackAnimalsAbstract):
    '''Класс лошади'''

    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

    def eat(self):
        """Лошадь умеет есть"""
        pass

    def speak(self):
        """Лошадь умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Лошадь: кличка - {self.__name}, дата рождения - {self.__birth_date}')
