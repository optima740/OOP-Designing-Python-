# ЗАДАНИЕ 13
"""
В данном задании, в качестве возможного решения, я реализовал класс ElementaryStruct, также входящий
 в общую систему классов (General,Any...NoneType). В классе ElementaryStruct была реализована операция сложения --
 def summation() для структур с полем 'a'. Класс TypeT является наследником класса ElementaryStruct. Класс Vector, также
 является  наследником класса ElementaryStruct. Т.о. мы можем предположить, что метод сложения (summation),
 который определен в классе ElementaryStruct, будет справедлив и для Vector[TypeT]. Vector, имеет свой переопределенный
 метод сложения (summаtion). Значит, Vector.summation() вызовет у элементов вектора тот же метод, но уже принадлежащий
 соответствующему собственному классу (или родительскому). Получается своего рода рекурсивное обращение. Каждый метод
 summation будет вызван у каждого типа свой.
 Не уверен, что правильно реализовал данное задание, именно в случае для сложения произвольных типов <T>. В моем случае,
 скорее, все-же получился конкретный тип (класс TypeT, с унаследованным полем а, для арифметических операций).
 Также несовсем понятен случай, если мы переопределим конструктор для класса TypeT, и уже не сможем гарантированно
 обращаться с данным типом, как с наследником типа ElementaryStruct. (поля а для операций сложения может и не быть,
 в случае переопределения конструктора)
 Тесты для Vector[Vector[Vector[T]]] в самом конце.
 """
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
        self.__type_of_status = self.CONST_TYPE_OF_OK
        return type(self)

    def is_type(self, object_type):
        self.__is_type_status = self.CONST_IS_TYPE_OK
        return isinstance(object_type, self.type_of())

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

class ElementaryStruct(Any):
    # описываем промежуточный класс, который имеет возможность производить сложение структур с полем а.

    CONST_SUMMATION_NIL = 0
    CONST_SUMMATION_OK = 1
    CONST_SUMMATION_ERR = 2

    def __init__(self, a):
        self.a = a
        self.__summation_status = self.CONST_SUMMATION_NIL
        self.__is_type_status = self.CONST_IS_TYPE_NIL
        self.__type_of_status = self.CONST_TYPE_OF_NIL

    def type_of(self):
        # переопределяем метод для определения типа нашей структуры.
        self.__type_of_status = self.CONST_TYPE_OF_OK
        return type(self)

    def summation(self, other_struct):
        # метод сложения полей двух объектов типа ElementaryStruct.
        if self.is_type(other_struct):
            self.__summation_status = self.CONST_SUMMATION_OK
            return self.a + other_struct.a
        self.__summation_status = self.CONST_SUMMATION_ERR

    def get_summation_status(self):
        return self.__summation_status


class TypeT(ElementaryStruct, Any):
    # пользовательский класс, наследник класса ElementaryStruct.
    pass


class Vector(ElementaryStruct, Any):
    # класс Vector.
    CONST_SIZE_OF_NIL = 0
    CONST_SIZE_OF_OK = 1
    CONST_SIZE_OF_ERR = 2
    CONST_GET_ITEM_NIL = 0
    CONST_GET_ITEM_OK = 1
    CONST_GET_ITEM_ERR = 2
    CONST_ADD_IN_NIL = 0
    CONST_ADD_IN_OK = 1

    def __init__(self):
        # создаем структуру Vector.
        self.vector = []
        self.__size_of_status = self.CONST_SIZE_OF_NIL
        self.__get_item_status = self.CONST_GET_ITEM_NIL
        self.__summation_status = self.CONST_SUMMATION_NIL
        self.__add_in_status = self.CONST_ADD_IN_NIL

    def add_in(self, item):
        self.__add_in_status = self.CONST_ADD_IN_OK
        self.vector.append(item)

    def type_of(self):
        # переопределяем метод для определения типа нашей структуры.
        self.__type_of_status = self.CONST_TYPE_OF_OK
        return type(self)

    def summation(self, other_struct):
        if isinstance(other_struct, self.type_of()) and self.size_of() != 0:
            # если обе структуры одинакового типа, то мы можем сравнить их длину.
            self.__summation_status = self.CONST_SUMMATION_OK
            if self.size_of() == other_struct.size_of():
                # если длина одинакова, то производим операцию сложения элементов (зная, что тип элементов - наследник
                # тогоже родительского класса, что и наш класс Vector).
                result = Vector()
                for i in range(self.size_of()):
                    a = self.vector[i]
                    b = other_struct.vector[i]
                    summ = a.summation(b)
                    if a.get_summation_status() != 2:
                        result.add_in(summ)
                return result
            else:
                void = NoneType()
                return void
        self.__summation_status = self.CONST_SUMMATION_ERR

    def size_of(self):
        if len(self.vector) != 0:
            self.__size_of_status = self.CONST_SIZE_OF_OK
            return len(self.vector)
        return 0

    def get_item(self, index_item):
        if self.type_of() != 0 and index_item < self.size_of():
            self.__get_item_status = self.CONST_GET_ITEM_OK
            return self.vector[index_item]
        self.__get_item_status = self.CONST_GET_ITEM_ERR

    def print_items(self):
        for i in range(self.size_of()):
            print(self.vector[i], end=' ')
        print()

    def get_summation_status(self):
        return self.__summation_status

    def get_for_get_item_status(self):
        return self.__get_item_status

    def get_add_in_status(self):
        return self.__add_in_status

class NoneType(Vector, TypeT, ElementaryStruct, Any):
    # замыкающий класс
    def __init__(self):
        pass

from unittest import TestCase

class TestForVector(TestCase):
    # создаем объекты типа T
    T1 = TypeT(1)
    T2 = TypeT(2)
    T3 = TypeT(3)
    # создаем вектора
    v1 = Vector()
    v2 = Vector()
    # и добавляем в них элементы типа Т (Vector[TypeT])
    v1.add_in(T1)
    v1.add_in(T2)
    v2.add_in(T1)
    v2.add_in(T3)
    # вектора разной длины
    va1 = Vector()
    vb2 = Vector()
    va1.add_in(T1)
    va1.add_in(T2)
    va1.add_in(T3)
    vb2.add_in(T1)
    # создаем вектора для хранения векторов (Vector[Vector])
    vv1 = Vector()
    vv2 = Vector()
    vvv1 = Vector()
    vvv2 = Vector()
    # добавляем в них вектора с элементами типа Т (Vector[Vector[TypeT]])
    vv1.add_in(v1)
    vv2.add_in(v2)
    vvv1.add_in(vv1)
    vvv2.add_in(vv2)

    def test_SizeVector(self):
        self.assertEqual(self.v1.size_of(), 2, 'incorrect size vector v1')
        self.assertEqual(self.v2.size_of(), 2, 'incorrect size vector v2')
        self.assertEqual(self.vv1.size_of(), 1, 'incorrect size vector vv1')
        self.assertEqual(self.vv2.size_of(), 1, 'incorrect size vector vv2')
        self.assertEqual(self.va1.size_of(), 3, 'incorrect size vector va1')
        self.assertEqual(self.vb2.size_of(), 1, 'incorrect size vector vb2')
    def test_SummVectors(self):
        summ = self.v1.summation(self.v2)
        self.assertEqual(self.v1.get_summation_status(), 1, 'incorrect summation v1 and v2')
        self.assertEqual(summ.type_of(), self.v1.type_of(), 'incorrect return type after summation')
        self.assertEqual(summ.size_of(), 2, 'incorrect size of result')
        summ1 = self.vv1.summation(self.vv2)
        self.assertEqual(self.vv1.get_summation_status(), 1, 'incorrect summation vv1 and vv2')
        self.assertEqual(summ1.type_of(), self.vv1.type_of(), 'incorrect return type after summation')
        self.assertEqual(summ1.size_of(), 1, 'incorrect size of result')
        summ2 = self.vvv1.summation(self.vvv2)
        self.assertEqual(self.vvv1.get_summation_status(), 1, 'incorrect summation vvv1 and vvv2')
        self.assertEqual(summ2.type_of(), self.vvv1.type_of(), 'incorrect return type after summation')
        self.assertEqual(summ2.size_of(), 1, 'incorrect size of result')
        # суммирование векторов различной длины
        res = self.va1.summation(self.vb2)
        self.assertEqual(self.va1.get_summation_status(), 1, 'incorrect summation status')
        self.assertEqual(type(res), type(NoneType()), 'incorrect return type after summation different vectors')
"""
t = TestForVector()
print(t.test_SizeVector())
print(t.test_SummVectors())
"""

