from abc import ABC, abstractmethod

class My_Queue(ABC):

    @abstractmethod
    def __init__(self):
        # создается структура под нашу очередь
        pass
    # СТАТУСЫ:
    CONST_ENQUEUE_NIL = 0  # enqueue() еще не вызывался
    CONST_ENQUEUE_OK = 1   # выполнился корректно
    CONST_DEQUEUE_NIL = 0  # dequeue() еще не вызывался
    CONST_DEQUEUE_OK = 1   # выполнился корректно
    CONST_DEQUEUE_ERR = 2  # очередь пустая
    CONST_SIZE_NIL = 0     # size() еще не вызывался
    CONST_SIZE_OK = 1      # выполнился корректно

    # КОМАНДЫ:

    # постусловие: элемент добавлен в хвост
    @abstractmethod
    def enqueue(self):
        # вставка в хвост
        pass

    #предусловие: очередь не пустая
    #постусловие: элемент изъят из очереди
    @abstractmethod
    def dequeue(self):
        # извлечение из головы
        pass

    # ЗАПРОСЫ:

    @abstractmethod
    def size(self):
        # возвращает кол-во элементов в очереди
        pass

    # ЗАПРОСЫ ДЛЯ СТАТУСОВ:

    @abstractmethod
    def get_enqueu_status(self):
        pass
    @abstractmethod
    def get_dequeu_status(self):
        pass
    @abstractmethod
    def get_size_status(self):
        pass


class My_Queue:

    CONST_ENQUEUE_NIL = 0  # enqueue() еще не вызывался
    CONST_ENQUEUE_OK = 1  # выполнился корректно
    CONST_DEQUEUE_NIL = 0  # dequeue() еще не вызывался
    CONST_DEQUEUE_OK = 1  # выполнился корректно
    CONST_DEQUEUE_ERR = 2  # очередь пустая
    CONST_SIZE_NIL = 0  # size() еще не вызывался
    CONST_SIZE_OK = 1  # выполнился корректно
    
    def __init__(self):
        self.queue = []
        self.queue_status = self.CONST_ENQUEUE_NIL

    def enqueue(self, item):
        self.queue.append(item)
        self.__enqueue_status = self.CONST_ENQUEUE_OK

    def dequeue(self):
        if self.size() > 0:
            self.__dequeue_status = self.CONST_DEQUEUE_OK
            return self.queue.pop(0)
        self.__dequeue_status = self.CONST_DEQUEUE_ERR

    def size(self):
        self.__size_status = self.CONST_SIZE_OK
        return len(self.queue)
