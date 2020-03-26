# Общая структкра иерархии классов в проекте.
# ЗАДАНИЕ 9.

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

# ЗАДАНИЕ 10.
"""
Насколько я понял, в Python нет стандартного функционала предусмотренного в синтаксисе языка, для явного запрета 
переопределения методов в классах наследниках. Но данный функционал можно попробовать реализовать, например, при 
помощи двойного нижнего подчеркивания перед именем метода (что по определенному соглашению делает 
его видимым только внутри своего класса), и созданием метода-геттера для нашего "скрытого" метода. Таким образом, при 
обращении к методам объекта, мы получим доступ только к соответствующему геттеру и можем выбрать какой именно метод нам 
нужен родительский или дочерний. 
Но данный способ весьма условный, т.к имеется функционал, который позволяет все-таки обращаться напрямую к подобным 
"скрытым" методам с двойным нижним подчеркиванием. В качестве другого способа в качестве модификатора доступа, 
можно попробовать использовать библиотеку accessify, импортировав специальные методы-декораторы protected и private, 
которые соответственно закрывают доступ к методу, относительно которого они применены
Но по факту, от самого механизма переопределения метода нас это не ограничивает.
 
"""

from accessify import protected, private
class parent:

    @private
    def __something(self):
        print('This is parent something')

    def get_parent_something(self):
        self.__something()

class child(parent):

    @private
    def __something(self):
        print('This is child something')

    def get_child_something(self):
        self.__something()











        
