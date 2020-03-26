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

    def __init__(self):
        
