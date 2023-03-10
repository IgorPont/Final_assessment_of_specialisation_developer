from Programme.DomesticAnimals.DomesticAnimalsAbstract import DomesticAnimalsAbstract


class Dogs(DomesticAnimalsAbstract):
    '''Класс собаки'''

    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

    def eat(self):
        """Собака умеет есть"""
        pass

    def speak(self):
        """Собака умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Собака: кличка - {self.__name}, дата рождения - {self.__birth_date}')
