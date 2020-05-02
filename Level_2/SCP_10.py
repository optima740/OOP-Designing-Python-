# ЗАДАНИЕ 19.

""" Наследование вариаций."""

class APIView:
    # Родительский класс Представление.
    def __init__(self, request):
        # Инициализируем поле, содержащее пользовательский запрос.
        self.request = request

    def get_queryset(self):
        # Определяем метод который предоставляет данные из поля self.request.
        queryset = self.request.data
        return queryset

import UserModel
# Подключаем пользовательский класс в котором будем искать по фильтру.

class MyView(APIView):
    # Создаем пользовательский класс, наследник от APIView. Нового функционала он не несет,
    # нам необходимо изменить логику родительского метода.
    def get_queryset(self):
        # переопределяем родительский метод с целью получить доступ к полю родительского класса, для применениея своих
        # пользовательских условий фильтрации для запроса.
        queryset = self.request.user.username
        list_result = UserModel.objects.filter(username=queryset)# обращаемся к пользовательскому классу для фильтрации.
        return list_result

""" Наследование с конкретизацией."""

from abc import ABC

class AbstractRectangle(ABC):
    # абстрактный класс Прямоугольник.
    CONST_AREA_NIL = 0
    CONAT_AREA_OK = 1
    CONAT_ARER_ERR = 2
    # предусловие: длина и высота - положительные
    def __init__(self):
        # инициализация прямоугольника по длине и высоте.
        pass

    # постусловие: площадь не равна нулю.
    def get_area(self):
        # метод получения площади.
        pass

import  math
class Rectangle(AbstractRectangle):
    # Реализуем (конкретизируем) родительский класс.

    def __init__(self, a, b):
        # используем модуль величины, в случае, если были приняты отрицательные значения
        self.length = math.fabs(a)
        self.height = math.fabs(b)
        self.get_area_status = self.CONST_AREA_NIL

    def get_area(self, a, b):
        # Реализуем родительский метод нахождения площади
        result = a * b
        if result != 0:
            self.get_area_status = self.CONAT_AREA_OK
            return result
        self.get_area_status = self.CONAT_ARER_ERR

""" 
Структурное наследование.

Данный тип наследования, насколько я понял, это вариант множественного наследования. В том, случае если язык не 
поддерживает множественное наследование, то используют интерфейсы. Но суть в том, что наследник принимает несколько 
структурных свойств от разных классов-родителей.
Например, у нас есть родительские классы "гусеничная техника" и "орудие для стрельбы снарядами". 
Мы можем получить дочерний класс "наземная военная техника гусеничного типа", который структурно будет наследовать 
функционал обоих родителей. 
Не уверен, что в данном примере я не допустил ошибку новичка с is-a.
"""

class TrackedVehicles:
    # класс Гусеничное транспортное средство, со своим функционалом.
    def __init__(self, number_axes, max_speed):
        # задаются основные характеристики.
        self.axes = number_axes
        self.wheels = self.axes * 2
        self.max_speed = max_speed

    def acceleration(self):
        # метод ускорения.
        pass

    def braking(self):
        # метод торможения.
        pass

    def left_turn(self):
        # метод левый разворот.
        pass

    def right_turn(self):
        # метод правый разворот.
        pass

class Weapon:
    # класс Орудие для стрельбы снарядами.

    def __init__(self, calibre, distance, capacity_bullet, damage):
        # определяем основные характеристики
        self.calibre = calibre
        self.distance = distance
        self.capacity_bullet = capacity_bullet
        self.damage = damage

    def shoot(self):
        # метод стрельбы.
        pass

    def rotate_left(self):
        # метод поворота орудия влево.
        pass

    def rotate_right(self):
        # метод поворота орудия вправо.
        pass

class GroundMilitaryEquipmentTracked(Weapon, TrackedVehicles):
    # класс Наземная военная техника гусеничного типа. Объединяет в себе функционал обоих родителей.

    def __init__(self, armor, max_speed, color):
        # определяем собственный конструктор для класса, со своим набором характеристик.
        self.armor = armor
        self.max_speed = max_speed
        self.color = color
