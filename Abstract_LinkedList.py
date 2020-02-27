""" 2.2 Операция tail() не сводима к другим операциям, т.к если данную операцию заменить
на операцию смещения курсора из текущего места в конец списка, то мы получим сложность O(n).
Но, при операции tail() мы просто обращаемся по адресу на последний элемент списка - т.о. имеем сложность O(1)

    2.3 У нас есть функция find(value), которая смещает курсор с текущей позиции на узел с искомым значением.
И есть запрос is_tail, таким образом, мы передвигаемся до конца списка по искомым значениям, и
при помощи операции get(), можем получить значение текущего узла.
"""

from abc import ABC, abstractmethod

class LinkedList(ABC):
    def __init__(self):  # создает пустой связный список
        pass

    # СТАТУСЫ КОМАНД:
    CONST_POINTER_HEAD_NIL = 0  # head() еще не вызывался
    CONST_POINTER_HEAD_OK = 1   # курсор указывает на первый элемент
    CONST_POINTER_HEAD_ERR = 2  # список пуст
    CONST_POINTER_TAIL_NIL = 0  # tail() еще не вызывался
    CONST_POINTER_TAIL_OK = 1    # курсор указывает на последний элемент
    CONST_POINTER_TAIL_ERR = 2   # список пуст
    CONST_POINTER_RIGHT_NIL = 0  # right() еще не вызывался
    CONST_POINTER_RIGHT_OK = 1   # курсор переместился на ону позицию вправо
    CONST_POINTER_RIGHT_ERR = 2  # элемента справа не существует или список пуст
    CONST_PUT_RIGHT_NIL = 0      # put_right() еще не вызывался
    CONST_PUT_RIGHT_OK = 1       # новый элемент размещен справа от текущего
    CONST_PUT_RIGHT_ERR = 2      # список пуст
    CONST_PUT_LEFT_NIL = 0      # put_left() еще не вызывался
    CONST_PUT_LEFT_OK = 1       # новый элемент размещен слева от текущего
    CONST_PUT_LEFT_ERR = 2      # список пуст
    CONST_REMOVE_NIL = 0        # remove() еще не вызывался
    CONST_REMOVE_OK = 1         # текущий элемент удален из списка
    CONST_REMOVE_ERR = 2        # список пуст
    CONST_REPLACE_NIL = 0       # replace() еще не вызывался
    CONST_REPLACE_OK = 1        # значение узла заменено на заданное
    CONST_REPLACE_ERR = 2       # список пуст
    CONST_FIND_NIL = 0          # find() еще не вызывался
    CONST_FIND_OK = 1           # курсор переместился на узел с искомым значением
    CONST_FIND_ERR = 2          # узел с заданным значением не найден или список пуст
    CONST_REMOVE_ALL_NIL = 0    # remove_all() еще не вызывался
    CONST_REMOVE_ALL_OK = 1     # все узлы с заданным значением удалены из списка
    CONST_REMOVE_ALL_ERR = 2    # в списке нет ни одного узла с заданным значением или список пуст

    # СТАТУСЫ ЗАПРОСОВ:
    CONST_IS_HEAD_NIL = 0   # is_head() еще не вызывался
    CONST_IS_HEAD_OK = 1    # курсор в начале списка (True) или нет (False)
    CONST_IS_HEAD_ERR = 2   # список пуст
    CONST_IS_TAIL_NIL = 0   # is_tail() еще не вызывался
    CONST_IS_TAIL_OK = 1    # курсор в конце списка (True) или нет (False)
    CONST_IS_TAIL_ERR = 2   # список пуст
    CONST_IS_VALUE_NIL = 0  # is_value() еще не вызывался
    CONST_IS_VALUE_OK = 1   # список не пуст (True) или список пуст (False)
    CONST_GET_NIL = 0       # get() еще не вызывался
    CONST_GET_OK = 1        # значение узла на котором находится курсор
    CONST_GET_ERR = 2       # список пуст

    # ЗАПРОСЫ ДЛЯ СТАТУСОВ:
    @abstractmethod
    def get_pointer_head(self):
        pass

    @abstractmethod
    def get_pointer_tail(self):
        pass

    @abstractmethod
    def get_pointer_right(self):
        pass

    @abstractmethod
    def get_put_right(self):
        pass

    @abstractmethod
    def get_put_left(self):
        pass

    @abstractmethod
    def get_remove(self):
        pass

    @abstractmethod
    def get_replace(self):
        pass

    @abstractmethod
    def get_find(self):
        pass

    @abstractmethod
    def get_remove_all(self):
        pass

    @abstractmethod
    def get_is_head(self):
        pass

    @abstractmethod
    def get_is_tail(self):
        pass

    @abstractmethod
    def get_is_value(self):
        pass

    @abstractmethod
    def get_for_get(self):
        pass

    # КОМАНДЫ:

    @abstractmethod
    # предусловие: список не пуст
    # постусловте: курсор указывает на первый узел
    def head(self):
        # установить курсор на первый узел в списке
        pass

    # предусловие: список не пуст
    # постусловие: курсор указывает на последний узел
    @abstractmethod
    def tail(self):
        # установить курсор на последний узел в списке
        pass

    # предусловие: список не пуст
    # постусловие: курсор передвинулся вправо
    @abstractmethod
    def right(self):
        # сдвинуть курсор на один узел вправо
        pass

    # предусловие: список не пуст
    # постусловие: новый элемент присутствует справа
    @abstractmethod
    def put_right(self, value):
        # вставить следом за текущим узлом новый узел с заданным значением
        pass

    # предусловие: список не пуст
    # постусловие: новый элемент присутствует слева
    @abstractmethod
    def put_left(self, value):
        # вставить перед текущим узлом новый узел с заданным значением
        pass

    # предусловие: список не пуст
    # постусловие: элемент удален.
    @abstractmethod
    def remove(self):
        # удалить текущий узел (курсор смещается к правому соседу, если он есть,
        # в противном случае курсор смещается к левому соседу, если он есть)
        pass

    #постусловие: список пуст
    @abstractmethod
    def clear(self):
        # очистить список
        pass

    # постусловие: новый элемент добавился в конец списка
    @abstractmethod
    def add_tail(self, value):
        # добавить новый узел в хвост списка
        pass

    # предусловие: список не пуст
    # постусловие: значение текущего узла изменено на заданное
    @abstractmethod
    def replace(self, value):
        # заменить значение текущего узла на заданное
        pass

    # предусловие: список не пуст
    # постусловие: курсор переставлен по указанному значению
    @abstractmethod
    def find(self, value):
        # установить курсор на следующий узел с искомым значением (по отношению к текущему узлу)
        pass
    # предусловие: список не пуст
    # постусловие: в списке нет узлов с заданным значением
    @abstractmethod
    def remove_all(self, value):
        # удалить в списке все узлы с заданным значением
        pass


    # ЗАПРОСЫ:

    # предусловие: список не пуст
    @abstractmethod
    def is_head(self):
        # находится ли курсор в начале списка?
        pass

    # предусловие: список не пуст
    @abstractmethod
    def is_tail(self):
        # находится ли курсор в конце списка?
        pass

    # предусловие: список не пуст
    @abstractmethod
    def is_value(self):
        # установлен ли курсор на какой-либо узел в списке?
        # (по сути, непустой ли список)
        pass

    # предусловие: список не пуст
    @abstractmethod
    def get(self):
        # получить значение текущего узла
        pass

    @abstractmethod
    def size(self):
        # посчитать количество узлов в списке
        pass