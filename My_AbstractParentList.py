from abc import ABC, abstractmethod
class ParentNode:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        self.prev = None

class ParentList(ABC):

    def __init__(self):  # создает пустой связный список
        self.clear()

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
    CONST_POINTER_LEFT_NIL = 0   # left() еще не вызывался
    CONST_POINTER_LEFT_OK = 1    # курсор переместился на ону позицию влево
    CONST_POINTER_LEFT_ERR = 2   # элемента слева не существует или список пуст
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
    CONST_ADD_TAIL_NIL = 0      # add_tail() еще не вызывался
    CONST_ADD_TAIL_OK =1        # элемент добавлен в хвост

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

    def get_head(self):
        return self.__head_status

    def get_tail(self):
        return self.__tail_status

    def get_right(self):
        return self.__right_status

    @abstractmethod
    def get_left(self):
        pass

    def get_put_right(self):
        return self.__put_right_status

    def get_put_left(self):
        return self.__put_left_status

    def get_remove(self):
        return self.__remove_status

    def get_replace(self):
        return self.__replace_status

    def get_find(self):
        return self.__find_status

    def get_remove_all(self):
        return self.__remove_all_status

    def get_is_head(self):
        return self.__is_head_status

    def get_is_tail(self):
        return self.__is_tail_status

    def get_is_value(self):
        return self.__is_value_status

    def get_for_get(self):
        return self.__get_status

    # КОМАНДЫ:

    # предусловие: список не пуст
    # постусловте: курсор указывает на первый узел
    def head(self):
        # установить курсор на первый узел в списке
        if self.p_head is not None and self.p_tail is not None:
            self.pointer = self.p_head
            self.__head_status = self.CONST_POINTER_HEAD_OK
        else:
            self.__head_status = self.CONST_POINTER_HEAD_ERR

    # предусловие: список не пуст
    # постусловие: курсор указывает на последний узел
    def tail(self):
        # установить курсор на последний узел в списке
        if self.p_head is not None and self.p_tail is not None:
            self.pointer = self.p_tail
            self.__tail_status = self.CONST_POINTER_TAIL_OK
        else:
            self.__tail_status = self.CONST_POINTER_TAIL_ERR

    # предусловие: список не пуст, праве курсора есть элемент
    # постусловие: курсор передвинулся вправо
    def right(self):
        # сдвинуть курсор на один узел вправо
        if self.p_head is not None and self.p_tail is not None:
            if self.pointer.next is not None:
                self.pointer = self.pointer.next
                self.__right_status = self.CONST_POINTER_RIGHT_OK
                return
        self.__right_status = self.CONST_POINTER_RIGHT_ERR

    @abstractmethod
    # предусловие: список не пуст, левее курсора есть элемент
    # постусловие: курсор передвинулся влево
    def left(self):
        # сдвинуть курсор на один узел влево
       pass

    # предусловие: список не пуст
    # постусловие: новый элемент присутствует справа
    def put_right(self, value):
        # вставить следом за текущим узлом новый узел с заданным значением
        if self.p_head is not None and self.p_tail is not None:
            if self.pointer.next is not None:
                new_node = ParentNode(value)
                tmp = self.pointer.next
                self.pointer.next = new_node
                new_node.prev = self.pointer
                new_node.next = tmp
                new_node.next.prev = new_node
                self.__put_right_status = self.CONST_PUT_RIGHT_OK
                return
        self.add_tail(value)
        self.__put_right_status = self.CONST_PUT_RIGHT_OK

    # предусловие: список не пуст
    # постусловие: новый элемент присутствует слева
    def put_left(self, value):
        # вставить перед текущим узлом новый узел с заданным значением
        if self.p_head is not None and self.p_tail is not None:
            if self.pointer.prev is not None:
                new_node = ParentNode(value)
                tmp = self.pointer.prev
                self.pointer.prev = new_node
                new_node.next = self.pointer
                new_node.prev = tmp
                new_node.prev.next = new_node
            else:
                new_node = ParentNode(value)
                self.p_head = new_node
                new_node.next = self.pointer
                new_node.prev = None
                self.pointer.prev = new_node
            self.__put_left_status = self.CONST_PUT_LEFT_OK
        self.__put_left_status = self.CONST_PUT_LEFT_ERR

    # предусловие: список не пуст
    # постусловие: элемент удален.
    def remove(self):
        # удалить текущий узел (курсор смещается к правому соседу, если он есть,
        # в противном случае курсор смещается к левому соседу, если он есть)
        if self.p_head is not None and self.p_tail is not None:
            tmp_next = self.pointer.next
            tmp_prev = self.pointer.prev
            if tmp_next is None and tmp_prev is None:
                self.clear()
            elif tmp_next is not None and tmp_prev is None:
                self.p_head = tmp_next
                self.pointer.next = None
                self.pointer = self.p_head
                self.pointer.prev = None
            elif tmp_next is None and tmp_prev is not None:
                self.p_tail = tmp_prev
                self.pointer.prev = None
                self.pointer = self.p_tail
                self.pointer.next = None
            elif tmp_next is not None and tmp_prev is not None:
                self.pointer.next.prev = tmp_prev
                self.pointer.prev.next = tmp_next
                self.pointer.next = None
                self.pointer.prev = None
                self.pointer = tmp_next
            self.__remove_status = self.CONST_REMOVE_OK
            return
        self.__remove_status = self.CONST_REMOVE_ERR

    #постусловие: список пуст
    def clear(self):
        # очистить список
        self.p_head = None
        self.p_tail = None
        self.pointer = None
        self.__get_status = self.CONST_GET_NIL
        self.__add_tail_status = self.CONST_ADD_TAIL_NIL
        self.__replace_status = self.CONST_REPLACE_NIL
        self.__find_status = self.CONST_FIND_NIL
        self.__remove_all_status = self.CONST_REMOVE_ALL_NIL
        self.__remove_status = self.CONST_REMOVE_NIL
        self.__is_head_status = self.CONST_IS_HEAD_NIL
        self.__is_tail_status = self.CONST_IS_TAIL_NIL
        self.__is_value_status = self.CONST_IS_VALUE_NIL
        self.__left_status = self.CONST_POINTER_LEFT_NIL
        self.__put_right_status = self.CONST_PUT_RIGHT_NIL
        self.__put_left_status = self.CONST_PUT_LEFT_NIL
        self.__right_status = self.CONST_POINTER_RIGHT_NIL
        self.__tail_status = self.CONST_POINTER_TAIL_NIL
        self.__head_status = self.CONST_POINTER_HEAD_NIL

    # постусловие: новый элемент добавился в конец списка
    def add_tail(self, value):
        # добавить новый узел в хвост списка
        new_node = ParentNode(value)
        if self.p_head is not None and self.p_tail is not None:
            self.pointer.next = new_node
            self.p_tail = new_node
            new_node.next = None
            new_node.prev = self.pointer
            self.right()
        else:
            self.p_head = new_node
            self.p_tail = new_node
            new_node.next = None
            new_node.prev = None
            self.pointer = self.p_head
        self.__add_tail_status = self.CONST_ADD_TAIL_OK

    # предусловие: список не пуст
    # постусловие: значение текущего узла изменено на заданное
    def replace(self, value):
        # заменить значение текущего узла на заданное
        if self.p_head is not None and self.p_tail is not None:
            self.pointer.value = value
            self.__replace_status = self.CONST_REPLACE_OK
            return
        self.__replace_status = self.CONST_REPLACE_ERR

    # предусловие: список не пуст
    # постусловие: курсор переставлен по указанному значению
    def find(self, value):
        # установить курсор на следующий узел с искомым значением (по отношению к текущему узлу)
        if self.p_head is not None and self.p_tail is not None:
            self.head()
            node = self.p_head
            while node is not None:
                if self.pointer.value == value:
                    self.__find_status = self.CONST_FIND_OK
                    return
                self.right()
                node = node.next

        self.__find_status = self.CONST_FIND_ERR

    # предусловие: список не пуст
    # постусловие: в списке нет узлов с заданным значением
    def remove_all(self, value):
        # удалить в списке все узлы с заданным значением
        if self.p_head is not None and self.p_tail is not None:
            self.head()

            while True:
                self.find(value)
                self.remove()
                if self.__find_status == 2:
                    self.__remove_all_status = self.CONST_REMOVE_ALL_OK
                    return
        self.__remove_all_status = self.CONST_REMOVE_ALL_ERR

    # ЗАПРОСЫ:

    # предусловие: список не пуст
    def is_head(self):
        # находится ли курсор в начале списка?
        self.head_status = False
        if self.p_head is not None and self.p_tail is not None:
            if self.p_head == self.pointer and self.p_tail == self.pointer:
                self.head_status = True
                self.tail_status = True
            elif self.p_head == self.pointer and self.p_tail != self.pointer:
                self.head_status = True
                self.tail_status = False
            elif self.p_head != self.pointer and self.p_tail == self.pointer:
                self.head_status = False
                self.tail_status = True
            elif self.p_head != self.pointer and self.p_tail != self.pointer:
                self.head_status = False
                self.tail_status = False
            self.__is_head_status = self.CONST_IS_HEAD_OK
            return self.head_status
        self.__is_head_status = self.CONST_IS_HEAD_ERR


    # предусловие: список не пуст
    def is_tail(self):
        # находится ли курсор в конце списка?
        self.tail_status = False
        if self.p_head is not None and self.p_tail is not None:
            if self.p_head == self.pointer and self.p_tail == self.pointer:
                self.head_status = True
                self.tail_status = True
            elif self.p_head == self.pointer and self.p_tail != self.pointer:
                self.head_status = True
                self.tail_status = False
            elif self.p_head != self.pointer and self.p_tail == self.pointer:
                self.head_status = False
                self.tail_status = True
            elif self.p_head != self.pointer and self.p_tail != self.pointer:
                self.head_status = False
                self.tail_status = False
            self.__is_tail_status = self.CONST_IS_TAIL_OK
            return self.tail_status
        self.__is_tail_status = self.CONST_IS_TAIL_ERR

    def is_value(self):
        # установлен ли курсор на какой-либо узел в списке?
        # (по сути, непустой ли список)
        if self.pointer is None or (self.p_tail is None and self.p_head is None):
            self.value_status = False
        else:
            self.value_status = True
        self.__is_value_status = self.CONST_IS_VALUE_OK

    # предусловие: список не пуст
    def get(self):
        # получить значение текущего узла
        if self.pointer is None or (self.p_tail is None and self.p_head is None):
            self.__get_status = self.CONST_GET_OK
            return self.pointer.value
        self.__get_status = self.CONST_GET_ERR

    def size(self):
        # посчитать количество узлов в списке
        counter_node = 0
        if self.p_head is not None and self.p_tail is not None:
            node = self.p_head
            while node is not None:
                counter_node += 1
                node = node.next
        return counter_node


class LinkedList(ParentList):
    pass


class TwoWayList(ParentList):

    # предусловие: список не пуст, левее курсора есть элемент
    # постусловие: курсор передвинулся влево
    def left(self):
        # сдвинуть курсор на один узел влево
        if self.p_head is not None and self.p_tail is not None:
            if self.pointer.prev is not None:
                self.pointer = self.pointer.prev
                self.__left_status = self.CONST_POINTER_LEFT_OK
                return
        self.__left_status = self.CONST_POINTER_LEFT_ERR

    def get_left(self):

        return self.__left_status


