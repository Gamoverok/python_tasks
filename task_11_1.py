class Volvo:
    def __init__(self, weight, age, engine_capacity):
        self.__weight = weight
        self.__age = age
        self.__engine_capacity = engine_capacity

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity


volvo_1 = Volvo
volvo_1.weight = 1500
volvo_1.age = 1993
volvo_1.engine_capacity = 3.0
print(f'Масса Volvo:= {volvo_1.weight} кг')
print(f'Год производства Volvo:= {volvo_1.age} год')
print(f'Объем двигателя Volvo:= {volvo_1.engine_capacity} л')


class Bmw:
    def __init__(self, weight, age, engine_capacity):
        self.__weight = weight
        self.__age = age
        self.__engine_capacity = engine_capacity

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity


bmw_1 = Bmw
bmw_1.weight = 1450
bmw_1.age = 1998
bmw_1.engine_capacity = 2.5
print(f'Масса Bmw:= {bmw_1.weight} кг')
print(f'Год производства Bmw:= {bmw_1.age} год')
print(f'Объем двигателя Bmw:= {bmw_1.engine_capacity} л')


class Audi:
    def __init__(self, weight, age, engine_capacity):
        self.__weight = weight
        self.__age = age
        self.__engine_capacity = engine_capacity

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity


audi_1 = Audi
audi_1.weight = 1600
audi_1.age = 2001
audi_1.engine_capacity = 4.5
print(f'Масса Audi:= {audi_1.weight} кг')
print(f'Год производства Audi:= {audi_1.age} год')
print(f'Объем двигателя Audi:= {audi_1.engine_capacity} л')


class Opel:
    def __init__(self, weight, age, engine_capacity):
        self.__weight = weight
        self.__age = age
        self.__engine_capacity = engine_capacity

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity


opel_1 = Opel
opel_1.weight = 1450
opel_1.age = 2005
opel_1.engine_capacity = 1.9
print(f'Масса Opel:= {opel_1.weight} кг')
print(f'Год производства Opel:= {opel_1.age} год')
print(f'Объем двигателя Opel:= {opel_1.engine_capacity} л')


class Geely:
    def __init__(self, weight, age, engine_capacity):
        self.__weight = weight
        self.__age = age
        self.__engine_capacity = engine_capacity

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity


gely_1 = Geely
gely_1.weight = 1600
gely_1.age = 2013
gely_1.engine_capacity = 1.8
print(f'Масса Geely:= {gely_1.weight} кг')
print(f'Год производства Geely:= {gely_1.age} год')
print(f'Объем двигателя Geely:= {gely_1.engine_capacity} л')
