# Занятие 1 Наследование, Композиция, Полиморфизм

# ЗАДАНИЕ 1
# пример НАСЛЕДОВАНИЯ:
class Car:
    # класс автомобиль.
    def __init__(self, brand, model, length, width, weight, max_speed, color):
        # Конструктор класса. Задает основные парметры автомобиля.
        self.brand = brand
        self.model = model
        self.length = length
        self.weight = weight
        self.width = width
        self.max_speed = max_speed
        self.color = color

    def accelerate(self):
        # Метод, позволяющий автомобилю ускоряться.
        pass

    def brake(self):
        # Метод, позволяющий автомобилю тормозить.
        pass

    def right(self):
        # Метод, позволяющий автомобилю поворачивать направо.
        pass

    def left(self):
        # Метод, позволяющий автомобилю поворачивать налево.
        pass

    def open_door(self):
        # Метод, позволяющий открыть дверь.
        pass

class Truck(Car):
    # класс Грузовик. Наследован от класса Автомобиль.
    def __init__(self):
        # в конструкторе мы исаользуем функцию super(), чтобы не переопределять полностью конструктор класса Truck, а
        # вызвать конструктор родителя передав ему параметры.
        super(self, Truck).__init__(self, brand, model, length, width, weight, max_speed, color)

    def body_change(self):
        # Метод опускания/подъема кузова.
        # мы добавили (расширили) родительский класс данным методом.
        pass

# пример КОМПОЗИЦИИ:
class CarModel:
    # класс описывающий модель автомобиля.
    def __init__(self, model, length, width, weight, max_speed):
        # конструктор, создает модель автомобиля по основным параметрам.
        self.model = model
        self.length = length
        self.weight = weight
        self.width = width
        self.max_speed = max_speed

class Car1:
    # класс автомобиль.
    def __init__(self, brand, model, length, width, weight, max_speed, color):
        # Конструктор класса. Задает основные парметры автомобиля.
        self.brand = brand
        self.model = CarModel(model, length, width, weight, max_speed) # создает экземпляр класса CarModel (объект).
        self.color = color

    def accelerate(self):
        # Метод, позволяющий автомобилю ускоряться.
        pass

    def brake(self):
        # Метод, позволяющий автомобилю тормозить.
        pass

    def right(self):
        # Метод, позволяющий автомобилю поворачивать направо.
        pass

    def left(self):
        # Метод, позволяющий автомобилю поворачивать налево.
        pass

    def open_door(self):
        # Метод, позволяющий открыть дверь.
        pass

# пример ПОЛИМОРФИЗМА:
class Bus(Car):
    # класс автобус. Наследован от класса автомобиль, но некоторые методы переопределены и ведут себя по-другому.
    def __init__(self, brand, color, max_capacity, length, width, weight, max_speed):
        # в данном классе конструктор переопределен и будет использован конструктор класса Bus.
        self.brand = brand
        self.color = color
        self.max_capacity = max_capacity
        self.length = length
        self.width = width
        self.weight = weight
        self.max_speed = max_speed

    def open_door(self):
        # Также переопределен метод открытия двери. В данном случае он открывает все двери в автобусе
        pass

# ЗАДАНИЕ 2
# В наследовании применяем расширение класса родителя (наследник задаёт более общий случай родителя):
class Helicopter:
    # Класс вертолет.
    def __init__(self, max_altitude, max_speed, max_weight, max_capacity):
        # задаются основные характеристики объекта.
        self.max_altitude = max_altitude
        self.max_speed = max_speed
        self.max_weight = max_weight
        self.max_capacity = max_capacity


    def vertical_takeoff(self):
        # Метод взлета (вертикальный)
        pass

    def vertical_landing(self):
        # Метод посадки (вертикальная)
        pass

class CombatHelicopter(Helicopter):
    # Класс боевой вертолет.
    def __init__(self):
        # используем конструктор родителя в иерархии наследования.
        super(self, FlyingObject).__init__(self, max_altitude, max_speed, max_weight, max_capacity)

    def attack(self):
        # Метод атаки.
        # Расширяем функционал родительского класса данным методом.
        pass

    def stealthy_flight(self):
        # Метод скрытного полета.
        # Расширяем функционал родительского класса данным методом.
        pass


# В наследовании применяем специализацию класса родителя (наследник задаёт более специализированный случай родителя):
class TransportVehicle:
    # Класс транспортное средство.
    def __init__(self, color, max_capacity, length, width, weight, max_speed):
        # Конструктор задает общие параметры для объекта.
        self.color = color
        self.max_capacity = max_capacity
        self.length = length
        self.width = width
        self.weight = weight
        self.max_speed = max_speed

    def accelerate(self):
        # Метод, позволяющий ускоряться.
        pass

    def brake(self):
        # Метод, позволяющий тормозить.
        pass

    def right(self):
        # Метод, позволяющий поворачивать направо.
        pass

    def left(self):
        # Метод, позволяющий поворачивать налево.
        pass

    def open_door(self):
        # Метод, позволяющий открыть дверь.
        pass

    def close_door(self):
        # Метод, позволяющий закрыть дверь.
        pass

class Bus1(TransportVehicle):
    # Класс автобус. Наследуем от класса транспортное средство.

    def __init__(self, color, max_capacity, length, width, weight, max_speed, number_wheels, number_doors):
        # Переопределяем конструктор родителя для частного случая. (добавили параметр кол-ва колес и кол-ва дверей)
        self.color = color
        self.max_capacity = max_capacity
        self.length = length
        self.width = width
        self.weight = weight
        self.max_speed = max_speed
        self.number_wheels = number_wheels # добавленный параметр
        self.number_doors = number_doors # добавленный параметр

    def open_door(self):
        # Переопределяем родительский метод для частного случая (все двери могут открываться одновременно)
        pass

    def close_door(self):
        # Переопределяем родительский метод для частного случая (все двери могут закрываться одновременно)
        pass
    # Теперь наш автобус обладает боле специализированными методами.

# ЗАДАНИЕ 3:

# "класс как модуль" в языке Python.

"""
В языке Python классы представляют собой базовую синтаксическую единицу. Своего рода строительный блок. 
Тут нет главной программы и подпрограмм, как в процедурных языках. 
Любая задача должна быть разбита на более элементарные составляющие (декомпозиция), 
затем должны быть выявлены связи между составляющими (нашими классами). 
Чтобы избежать повторного использования кода, применяется концепция наследования. Все классы, организованные 
при помощи наследования представляют собой иерархию классов, у который есть предки и в конце всей цепочки наследования 
базовый класс (в Python это класс object).
Принцип композиции, в отличие от наследования делает связи между классами (модулями) менее явными, 
что позволяет решать поставленные задачи более гибко (в тех случаях когда конечный проект требует 
частого внесения изменений).
 
"""

