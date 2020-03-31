# Замыкание иерархии.

# ЗАДАНИЕ 10.
"""В Python поддерживается множественное наследование. По этому мы можем создать, замыкающий нашу иерархию из
классов General и Any, класс None (класс NoneType, экземпляром которого будет являться объект Void). Это класс не
имеющий потомков, но являющийся наследником всех классов в иерархии, наследников от Any"""
from abc import ABC, abstractmethod

class General(ABC):
    # СТАТУСЫ:
    CONST_COPY_NIL = 0
    CONST_COPY_OK = 1
    CONST_COPY_ERR = 2
    CONST_CLONE_NIL = 0
    CONST_CLONE_OK = 1
    CONST_CLONE_ERR = 2
    CONST_EQUAL_NIL = 0
    CONST_EQUAL_OK = 1
    CONST_EQUAL_ERR = 2
    CONST_PRINT_NIL = 0
    CONST_PRINT_OK = 1
    CONST_IS_TYPE_NIL = 0
    CONST_IS_TYPE_OK = 1
    CONST_TYPE_OF_NIL = 0
    CONST_TYPE_OF_OK = 1
    CONST_TO_FORMAT_NIL = 0
    CONST_TO_FORMAT_OK = 1
    CONST_ASSIGNMENT_NIL = 0
    CONST_ASSIGNMENT_OK = 1

    # КОНСТРУКТОР:
    @abstractmethod
    def __init__(self):
        # создает объект.
        pass

    # КОМАНДЫ:

    # Предусловие: объект в который необходимо копировать существует.
    @abstractmethod
    def copy(self):
        # копирование содержимого объекта в другой, существующий.
        pass

    # Постусловие: новый объект создан.
    @abstractmethod
    def clone(self):
        # создает новый объект и копирует в него исходный (существующий) объект.
        pass

    @abstractmethod
    def assignment_attempt(self):
        # проверка присваивания.
        pass

    # ЗАПРОСЫ:

    @abstractmethod
    def to_format(self):
        # переводит в формат для удобного ввода-вывода, строковый тип. И восстановление из строкового типа в объект.
        pass

    @abstractmethod
    def print(self):
        # вывод на экран содержимого объекта. Если объект пуст - пустая строка.
        pass

    # Предусловие: сравниваемые объекты существуют.
    @abstractmethod
    def equal(self):
        # Возвращает True, если оба объекта эквивалентны (равны).
        pass

    @abstractmethod
    def type_of(self):
        # возвращает тип (непостредственный класс, экземпляром которого является объект).
        pass

    @abstractmethod
    def is_type(self):
        # возвращает True если тип объекта совпадает с указанным.
        pass

    # ЗАПРОСЫ СТАТУСОВ:

    @abstractmethod
    def get_copy_status(self):
        pass

    @abstractmethod
    def get_clone_status(self):
        pass

    @abstractmethod
    def get_to_format_status(self):
        pass

    @abstractmethod
    def get_print_status(self):
        pass

    @abstractmethod
    def get_is_type_status(self):
        pass

    @abstractmethod
    def get_type_of_status(self):
        pass

    @abstractmethod
    def get_equal_status(self):
        pass

    @abstractmethod
    def get_assignment_attempt(self):
        pass

class Any(General):

    CONST_INIT_STATUS_OK = 1
    CONST_INIT_STATUS_ERR = 2

    def __init__(self, length, width):
        self.__copy_status = self.CONST_COPY_NIL
        self.__clone_status = self.CONST_CLONE_NIL
        self.__equal_status = self.CONST_EQUAL_NIL
        self.__print_status = self.CONST_PRINT_NIL
        self.__is_type_status = self.CONST_IS_TYPE_NIL
        self.__type_of_status = self.CONST_TYPE_OF_NIL
        self.__to_format_status = self.CONST_TO_FORMAT_NIL
        self.__assignment_status = self.CONST_ASSIGNMENT_NIL
        if length > 0 and width > 0:
            self.length = length
            self.width = width
            self.__init_status = self.CONST_INIT_STATUS_OK
        else:
            self.__init_status = self.CONST_INIT_STATUS_ERR

    def get_init_status(self):
        return self.__init_status

    def copy(self, object2):
        if object2.get_init_status() == 1 and self.get_init_status() == 1:
            property_object1 = (self.length, self.width)
            object2.length = property_object1[0]
            object2.width = property_object1[1]
            self.__copy_status = self.CONST_COPY_OK
            return
        self.__copy_status = self.CONST_COPY_ERR

    def clone(self,):
        object2 = Any(1, 1)
        self.copy(object2)
        if object2.get_init_status() == 1:
            self.__clone_status = self.CONST_CLONE_OK
            return object2
        else:
            self.__clone_status = self.CONST_CLONE_ERR

    def to_format(self, arg=None):
        if arg is not None:
            new_object = Any(arg[0], arg[1])
            self.__to_format_status = self.CONST_TO_FORMAT_OK
            return new_object
        else:
            print_list = []
            print_list.append(str(self.length))
            print_list.append(str(self.width))
            self.__to_format_status = self.CONST_TO_FORMAT_OK
            return print_list

    def print(self):
        print_list = self.to_format()
        for item in print_list:
            print(item)

    def equal(self, object2):
        if self.get_init_status() == 1 and object2.get_init_status() == 1:
            object1_property = self.to_format()
            object2_property = object2.to_format()
            self.__equal_status = self.CONST_EQUAL_OK
            if len(object1_property) == len(object2_property):
                for i in range (len(object1_property)):
                    if object1_property[i] != object2_property[i]:
                        return False
                return True
        self.__equal_status = self.CONST_EQUAL_ERR

    def type_of(self):
        self_object = Any(1, 1)
        self.__type_of_status = self.CONST_TYPE_OF_OK
        return type(self_object)


    def is_type(self, object_type):
        self.__is_type_status = self.CONST_IS_TYPE_OK
        if object_type is not self.type_of():
            return False
        return True

    def assignment_attempt(self, target, source):
        self.__assignment_status = self.CONST_ASSIGNMENT_OK
        if source.is_type(target) and source.get_is_type_status() == 1:
            target = source
        else:
            void = NoneType()
            target = void

    def get_assignment_attempt(self):
        return self.__assignment_status

    def get_clone_status(self):
        return self.__clone_status

    def get_copy_status(self):
        return self.__copy_status

    def get_equal_status(self):
        return self.__equal_status

    def get_is_type_status(self):
        return self.__is_type_status

    def get_to_format_status(self):
        return self.__to_format_status

    def get_type_of_status(self):
        return self.__type_of_status

    def get_print_status(self):
        return self.__print_status

class Shape(Any):
    pass

class NoneType(Shape, Any):
    pass

# ЗАДАНИЕ 10.
"""
В Python благодаря соглашению в синтаксисе принято обозначать "слабо приватные" методы одинарным нижним подчеркиванием 
перед именем: _name, а "сильно приватные" методы - двойным нижним подчеркиванием: __name . При этом в случае _name мы 
имеем запрет доступа к методу при импорте (from module import*), а в случае с __name имеем запрет на обращение через 
экземпляр класса. (object.__name - обратиться нельзя). Но все равно существуют способы прямого обращения к методу даже 
при объявлении его как __name. 
Также существует способ использовать библиотеку accessify. И ее декораторы @private и @protected.
"""
from accessify import protected, private

# 1. метод публичен в родительском классе А и публичен в его потомке В.
class A1:

    def method(self):
        print("A1")

class B1(A1):
    def method(self):
        print("B1<-A1")

# 2. метод публичен в родительском классе А и скрыт в его потомке В.
"""При обращении к методу через экземпляр класса B (при запуске программы), получаем ошибку интерпретатора, но 
возможность обратиться при написании кода, PyCharm нам также без препятствий предоставляет. 
"""
class A2:

    def method(self):
        print("A2")

class B2(A2):

    @private
    def method(self):
        print("A2<-B2")
# 3. метод скрыт в родительском классе А и публичен в его потомке В.
"""
Такой же эффект получаем и в данном случае. Интерпретатор выдает ошибку при обращении к методу через объект класса.
"""
class A3:

    @private
    def method(self):
        print("A3")

class B3(A3):

    def method(self):
        print("A3<-B3")

# 4. метод скрыт в родительском классе А и скрыт в его потомке B.

class A4:

    @private
    def __method(self):
        print("A4")

class B4(A4):

    @private
    def __method(self):
        print("A4<-B4")

"""Таким образом, получается, что в Python при помощи стандартных средств языка, мы можем реализовать только варианты
1 и 4. Остальные варианты нам становятся доступны при помощи подключаемой библиотеки accessify, что не скрывает метод
полностью для средств IDE, но генерирует ошибку при запуске программы"""











