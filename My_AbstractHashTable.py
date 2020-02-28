from abc import ABC, abstractmethod

class abstract_HashTable(ABC):

    @abstractmethod
    def __init__(self):
        # создает структуру данных под hash-таблицу размером sz содержащая пустые слоты (None)
        pass

    # ЗАПРОСЫ:

    # предусловие: в качестве значения поступает строка
    # постусловие: для входного значения value посчитана hash-функция
    @abstractmethod
    def hash_fun(self):
        # возвращает hash-функцию (индекс слота)
        pass

    # постусловие: найден индекс пустого (None) слота для значения или слотов для размещения нет
    @abstractmethod
    def seek_slot(self):
        # учитывая коллизии ищет индекс пустого слота для значения, слоты могут быть все заняты
        pass

    # постусловие: найден индекс слота с указанным значением или слотов с таким значением нет
    @abstractmethod
    def find(self):
        # ищет в слотах указанное значение. Если значение такое есть - возвращает индекс слота. Иначе - неудача
        pass

    # КОМАНДЫ:

    # предусловие: пустой слот имеется в хэш-таблице
    # постусловие: значение помещено в слот
    @abstractmethod
    def put(self):
        # помещает значение в слот
        pass

    # предусловие: заданное значение имеется в хэш-таблице
    # постусловие: значение удалено, слот очищен. Или неудача - заданного значения нет в хэш-таблице
    @abstractmethod
    def remove(self):
        # удаляет значение из слота
        pass

    # СТАТУСЫ:

    CONST_HASH_FUN_NIL = 0    # метод еще не вызывался
    CONST_HASH_FUN_OK = 1     # метод отработал корректно
    CONST_HASH_FUN_ERR = 2    # невозможно посчитать хэш-функцию для входного значения
    CONST_SEEK_SLOT_NIL = 0   # метод еще не вызывался
    CONST_SEEK_SLOT_OK = 1    # метод отработал корректно
    CONST_SEEK_SLOT_ERR = 2   # учитывая коллизии, нет свободных слотов
    CONST_FIND_NIL = 0  # метод еще не вызывался
    CONST_FIND_OK = 1   # метод отработал корректно
    CONST_FIND_ERR = 2  # указанного значения нет в слотах хэш-таблицы
    CONST_PUT_NIL = 0   # метод еще не вызывался
    CONST_PUT_OK = 1    # метод отработал корректно
    CONST_PUT_ERR = 2   # нет свободных слотов для размещения
    CONST_REMOVE_NIL = 0  # метод еще не вызывался
    CONST_REMOVE_OK = 1   # метод отработал корректно
    CONST_REMOVE_ERR = 2  # значение которое нужно удалить, отсутствует в хэш-таблице

    # ЗАПРОСЫ ДЛЯ СТАТУСОВ:

    @abstractmethod
    def get_hash_fun_status(self):
        pass

    @abstractmethod
    def get_seek_slot_status(self):
        pass

    @abstractmethod
    def get_find_status(self):
        pass

    @abstractmethod
    def get_put_status(self):
        pass

    @abstractmethod
    def get_remove_status(self):
        pass

class HashTable:
    
    CONST_HASH_FUN_NIL = 0  # метод еще не вызывался
    CONST_HASH_FUN_OK = 1  # метод отработал корректно
    CONST_HASH_FUN_ERR = 2  # невозможно посчитать хэш-функцию для входного значения
    CONST_SEEK_SLOT_NIL = 0  # метод еще не вызывался
    CONST_SEEK_SLOT_OK = 1  # метод отработал корректно
    CONST_SEEK_SLOT_ERR = 2  # учитывая коллизии, нет свободных слотов
    CONST_FIND_NIL = 0  # метод еще не вызывался
    CONST_FIND_OK = 1  # метод отработал корректно
    CONST_FIND_ERR = 2  # указанного значения нет в слотах хэш-таблицы
    CONST_PUT_NIL = 0  # метод еще не вызывался
    CONST_PUT_OK = 1  # метод отработал корректно
    CONST_PUT_ERR = 2  # нет свободных слотов для размещения
    CONST_STR_TO_INT_NIL = 0  # метод еще не вызывался
    CONST_STR_TO_INT_OK = 1   # метод отработал корректно
    CONST_REMOVE_NIL = 0  # метод еще не вызывался
    CONST_REMOVE_OK = 1  # метод отработал корректно
    CONST_REMOVE_ERR = 2  # значение которое нужно удалить, отсутствует в хэш-таблице

    def __init__(self, sz):
        # создает структуру данных под hash-таблицу размером sz содержащая пустые слоты (None)
        # c постоянным шагом смещения при коллизии
        CONST_STEP = 3
        self.size = sz
        self.step = CONST_STEP
        self.slots = [None] * self.size
        self.__hash_fun_status = self.CONST_HASH_FUN_NIL
        self.__seek_slot_status = self.CONST_SEEK_SLOT_NIL
        self.__find_status = self.CONST_FIND_NIL
        self.__put_status = self.CONST_PUT_NIL
        self.__str_to_int_status = self.CONST_STR_TO_INT_NIL
        self.__remove_status = self.CONST_REMOVE_NIL

    # постусловие: подготовлено значение для работы хэш-функции
    def __str_to_int(self, value):
        # вспомогательный метод перевода входного значения value для хэш-таблицы в строку исключая пробелы
        # подготавливает данные для хэш-функции
        value = str(value).strip()
        sum = 0
        for i in value:
            sum = sum + ord(i)
        self.__str_to_int_status = self.CONST_STR_TO_INT_OK
        return sum

    # постусловие: вычислен индекс слота
    def hash_fun(self, value):
        hash_result = self.__str_to_int(value) % self.size
        self.__hash_fun_status = self.CONST_HASH_FUN_OK
        return hash_result

    # постусловие: найден свободный слот для value, или неудача.
    def seek_slot(self, value):
        count = 0
        index = self.hash_fun(value)
        while count <= self.size - 1:
            if self.slots[index] is None:
                self.__seek_slot_status = self.CONST_SEEK_SLOT_OK
                return index
            if index + self.step > self.size - 1:
                index = (index+self.step) - self.size
            else:
                index += self.step
            count += 1
        self.__seek_slot_status = self.CONST_SEEK_SLOT_ERR

    # предусловие: пустой слот имеется в хэш-таблице
    # постусловие: возвращается индекс слота или неудача
    def put(self, value):
        # записываем значение по хэш-функции возвращается индекс слота или неудача,
        # если из-за коллизий элемент не удаётся разместить
        index_put = self.seek_slot(value)
        if self.__get_seek_slot_status() == 1 and index_put is not None:
            self.slots[index_put] = value
            self.__put_status = self.CONST_PUT_OK
            return index_put
        self.__put_status = self.CONST_PUT_ERR

    # постусловие: найден индекс слота с указанным значением или слотов с таким значением нет
    def find(self, value):
        # ищет в слотах указанное значение. Если значение такое есть - возвращает индекс слота. Иначе - неудача
        find_index = self.hash_fun(value)
        count = 0
        while count <= self.size-1:
            if self.slots[find_index] == value:
                self.__find_status = self.CONST_FIND_OK
                return find_index
            if find_index + self.step > self.size - 1:
                find_index = (find_index+self.step) - self.size
            else:
                find_index += self.step
            count += 1
        self.__find_status = self.CONST_FIND_ERR

    # предусловие: заданное значение имеется в хэш-таблице
    # постусловие: значение удалено(слот очищен). Или неудача - заданного значения нет в хэш-таблице
    def remove(self, value):
        # удаляет значение из хэш-таблицы. Если значение не найдено в статус прописываем неудачное выполнение.
        find_index = self.find(value)
        if find_index is not None and self.__get_find_status() == 1:
            self.slots[find_index] = None
            self.__remove_status = self.CONST_REMOVE_OK
            return
        self.__remove_status = self.CONST_REMOVE_ERR

    def __get_hash_fun_status(self):
        return self.__hash_fun_status

    def __get_seek_slot_status(self):
        return self.__seek_slot_status

    def __get_find_status(self):
        return self.__find_status

    def __get_put_status(self):
        return self.__put_status

    def __get_remove(self):
        return self.__remove_status

