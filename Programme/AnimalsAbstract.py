from abc import ABC, abstractmethod


class Animals(ABC):
    """Абстрактный класс Животные (Друзья человека)"""

    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date

    def get_name(self) -> str:
        return self.__name

    def get_birth_date(self) -> str:
        return self.__birth_date

    @abstractmethod
    def print_animal(self):
        """Распечатать свойства животного"""
        pass
