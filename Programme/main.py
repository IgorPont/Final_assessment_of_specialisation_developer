from Programme.DomesticAnimals.Cats import Cats
from Programme.DomesticAnimals.Dogs import Dogs
from Programme.DomesticAnimals.Hamsters import Hamsters
from Programme.PackAnimals.Camels import Camels
from Programme.PackAnimals.Donkeys import Donkeys
from Programme.PackAnimals.Horses import Horses

if __name__ == '__main__':
    dog_1 = Dogs('Шарик', '2022-09-12')
    cat_1 = Cats('Мурка', '2015-08-23')
    hamster_1 = Hamsters('Прошка', '2022-01-14')
    horse_1 = Horses('Бегун', '2020-02-17')
    donkey_1 = Donkeys('Упрямый', '2021-06-19')
    camel_1 = Camels('Горбун', '2028-09-11')

    camel_1.print_animal()
    print(camel_1.get_name())
