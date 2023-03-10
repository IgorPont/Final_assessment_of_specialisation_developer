from Programme.DomesticAnimals.DomesticAnimalsAbstract import DomesticAnimalsAbstract


class Cats(DomesticAnimalsAbstract):
    '''Класс кошки'''

    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

    def eat(self):
        """Кошка умеет есть"""
        pass

    def speak(self):
        """Кошка умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Кошка: кличка - {self.__name}, дата рождения - {self.__birth_date}')
