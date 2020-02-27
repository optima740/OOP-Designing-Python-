from abc import ABC, abstractmethod

class BoundedStack(ABC):
    CONST_POP_NIL = 0   # pop() еще не вызывался
    CONST_POP_OK = 1    # последняя pop() отработала нормально
    CONST_POP_ERR = 2   # стек пуст
    CONST_PEEK_NIL = 0  # peek() еще не вызывался
    CONST_PEEK_OK = 1   # последняя peek() вернула корректное значение
    CONST_PEEK_ERR = 2  # стек пуст
    CONST_PUSH_NIL = 0  # push() еше не вызывался
    CONST_PUSH_OK = 1   # последняя push() вернула корректное значение
    CONST_PUSH_ERR = 2  # стек заполнен

    def __init__(self):
        pass  # постусловие: создан пустой стек

    # команды

    # предусловие: стек не заполнен полностью
    # постусловие: добавлен новый элемент
    @abstractmethod
    def push(self):
        pass

    # предусловие: стек не пустой
    # постусловие: удален верхий элемент
    @abstractmethod
    def pop(self):
        pass
    # из стека удалены все значения, стек пуст
    @abstractmethod
    def clear(self):
        pass

    # запросы
    #предусловие: стек не пустой
    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass

    # доп запросы
    @abstractmethod
    def get_pop_status(self):
        pass

    @abstractmethod
    def get_peek_status(self):
        pass

    @abstractmethod
    def get_push_status(self):
        pass

class BoundedStack:
    CONST_POP_NIL = 0  # pop() еще не вызывался
    CONST_POP_OK = 1  # последняя pop() отработала нормально
    CONST_POP_ERR = 2  # стек пуст
    CONST_PEEK_NIL = 0  # peek() еще не вызывался
    CONST_PEEK_OK = 1  # последняя peek() вернула корректное значение
    CONST_PEEK_ERR = 2  # стек пуст
    CONST_PUSH_NIL = 0  # push() еше не вызывался
    CONST_PUSH_OK = 1  # последняя push() вернула корректное значение
    CONST_PUSH_ERR = 2  # стек заполнен

    def __init__(self, n=32):
        self.__max_size = n
        self.clear()

    def size(self):
        return len(self.__stack)

    def push(self, item):
        if self.size() < self.__max_size:
            self.__stack.append(item)
            self.__push_status = self.CONST_PUSH_OK
        else:
            result = 0
            self.__push_status = self.CONST_PUSH_ERR
            return result

    def clear(self):

        self.__stack = [] * self.__max_size
        self.__peek_status = self.CONST_PEEK_NIL
        self.__pop_status = self.CONST_POP_NIL
        self.__push_status = self.CONST_PUSH_NIL

    def peek(self):
        if self.size() > 0:
            result = self.__stack[-1]
            self.__peek_status = self.CONST_PEEK_OK
        else:
            result = 0
            self.__peek_status = self.CONST_PEEK_ERR
        return result

    def pop(self):
        if self.size() > 0:
            self.__stack.pop(-1)
            self.__pop_status = self.CONST_POP_OK
        else:
            self.__pop_status = self.CONST_POP_ERR

    def get_pop_status(self):
        return self.__pop_status

    def get_peek_status(self):
        return self.__peek_status

    def get_push_status(self):
        return self.__push_status

