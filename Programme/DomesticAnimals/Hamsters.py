from Programme.DomesticAnimals.DomesticAnimalsAbstract import DomesticAnimalsAbstract


class Hamsters(DomesticAnimalsAbstract):
    '''Класс хомяки'''

    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

    def eat(self):
        """Хомяк умеет есть"""
        pass

    def speak(self):
        """Хомяк умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Хомяк: кличка - {self.__name}, дата рождения - {self.__birth_date}')
