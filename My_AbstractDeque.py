from abc import abstractmethod, ABC

class ParrentDeque(ABC):
    CONST_ADD_FRONT_NIL = 0  # addFront() еще не вызывался
    CONST_ADD_FRONT_OK = 1  # выполнился корректно
    CONST_ADD_TAIL_NIL = 0  # addTaile() еще не вызывался
    CONST_ADD_TAIL_OK = 1  # выполнился корректно
    CONST_REMOVE_FRONT_NIL = 0  # removeFront() еще не вызывался
    CONST_REMOVE_FRONT_OK = 1  # выполнился корректно
    CONST_REMOVE_FRONT_ERR = 2  # очередь пустая
    CONST_REMOVE_TAIL_NIL = 0  # removeTaile() еще не вызывался
    CONST_REMOVE_TAIL_OK = 1  # выполнился корректно
    CONST_REMOVE_TAIL_ERR = 2  # очередь пустая
    CONST_SIZE_NIL = 0  # size() еще не вызывался
    CONST_SIZE_OK = 1  # выполнился корректно

    def __init__(self):
        # создается структура под двустороннюю очередь.
        self.deque = []
        self.__addTail_status = self.CONST_ADD_TAIL_NIL
        self.__addFront_status = self.CONST_ADD_FRONT_NIL
        self.__removeTail_status = self.CONST_REMOVE_TAIL_NIL
        self.__removeFront_status = self.CONST_REMOVE_FRONT_NIL
        self.__size_status = self.CONST_SIZE_NIL

    # КОМАНДЫ:

    # постусловие: элемент добавлен в хвост очереди
    def addTail(self, item):
        # добавление в хвост
        self.deque.append(item)
        self.__addTail_status = self.CONST_ADD_TAIL_OK

    # предусловие: очередь не пустая
    # постусловие: элемент удален из головы
    def removeFront(self):
        # удаление из головы
        if self.size() > 0:
            self.__removeFront_status = self.CONST_REMOVE_FRONT_OK
            return self.deque.pop(0)
        self.__removeFront_status = self.CONST_REMOVE_FRONT_ERR

    # ЗАПРОСЫ:

    def size(self):
        # возвращает кол-во элементов в очереди
        self.__size_status = self.CONST_SIZE_OK
        return len(self.deque)

    # ЗАПРОСЫ ДЛЯ СТАТУСОВ:

    def __get_addTail_status(self):
        return self.__addTail_status

    def __get_removeFront_status(self):
        return self.__removeFront_status

    def __get_size_status(self):
        return self.__size_status

class Queue(ParrentDeque):
    CONST_ENQUEUE_OK = 1  # выполнился корректно
    CONST_DEQUEUE_OK = 1  # выполнился корректно
    CONST_DEQUEUE_ERR = 2  # очередь пустая

    def enqueue(self, item):
        self.addTail(item)
        self.__enqueue_status = self.CONST_ENQUEUE_OK

    def dequeue(self):
        self.removeFront()
        if self.__get_removeFront_status() < 2:
            self.__dequeue_status = self.CONST_DEQUEUE_OK
            return
        self.__dequeue_status = self.CONST_DEQUEUE_ERR

    def __get_enqueue_status(self):
        return self.__enqueue_status

    def __get_dequeue_status(self):
        return self.__dequeue_status


class Deque(ParrentDeque):

    # постусловие: элемент добавлен в голову очереди
    def addFront(self, item):
        # добавление в голову
        self.deque.insert(0, item)
        self.__addFront_status = self.CONST_ADD_FRONT_OK

    # предусловие: очередь не пустая
    # постусловие: элемент удален из хвоста очереди
    def removeTail(self):
        # удаление из хвоста
        if self.size() > 0:
            self.__removeTail_status = self.CONST_REMOVE_TAIL_OK
            return self.deque.pop(self.size() - 1)
        self.__removeTail_status = self.CONST_REMOVE_TAIL_ERR

    def __get_addFront_status(self):
        return self.__addFront_status

    def __get_removeTail_status(self):
        return self.__removeTail_status