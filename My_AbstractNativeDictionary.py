from abc import ABC, abstractmethod

class AbstractNativeDictionary(ABC):

    # постусловие: создана пустая структура для ассоциативного массива заданного размера
    @abstractmethod
    def __init__(self):
        # создает структуру для нашего ассоциативного массива
        pass

    # ЗАПРОСЫ:

    # предусловие: на вход поступает строка
    # постусловие: посчитан индекс для слота
    @abstractmethod
    def hash_fun(self):
        # по входному значению вычисляет индекс для слота и возвращает его
        pass

    # постусловие: метод вернул True или False
    @abstractmethod
    def is_key(self):
        # возвращает True, если ключ имеется в массиве. Иначе - возвращает False
        pass

    # предусловие: ключ присутствует в массиве
    # постусловие: возвращено значение соответствующее ключу
    @abstractmethod
    def get(self):
        # возврящает значение соответствующее ключу.
        pass

    # КОМАНДЫ:

    # постусловие: значение записано в массив в соответствии с ключем
    @abstractmethod
    def put(self):
        # записывает значение по ключу в массив
        pass

    # СТАТУСЫ:

    CONST_HASH_FUN_NIL = 0   # методо еще не вызывался
    CONST_HASH_FUN_OK = 1    # метод отработат корректно
    CONST_HASH_FUN_ERR = 2   # невозможно посчитать хэш-функцию для входного значения
    CONST_IS_KEY_NIL = 0   # методо еще не вызывался
    CONST_IS_KEY_OK = 1    # метод отработат корректно
    CONST_GET_NIL = 0   # методо еще не вызывался
    CONST_GET_OK = 1    # метод отработат корректно
    CONST_GET_ERR = 2   # в массивет нет указанного ключа
    CONST_PUT_NIL = 0  # методо еще не вызывался
    CONST_PUT_OK = 1   # метод отработат корректно
    CONST_PUT_ERR = 2  # невозможно добавить новое значение

    # ЗАПРОСЫ ДЛЯ СТАТУСОВ:

    @abstractmethod
    def get_hash_fun_status(self):
        pass

    @abstractmethod
    def get_is_key_status(self):
        pass

    @abstractmethod
    def get_for_get_status(self):
        pass

    @abstractmethod
    def get_put_status(self):
        pass

class NativeDictionary:

    CONST_HASH_FUN_NIL = 0  # методо еще не вызывался
    CONST_HASH_FUN_OK = 1  # метод отработат корректно
    CONST_HASH_FUN_ERR = 2  # невозможно посчитать хэш-функцию для входного значения
    CONST_IS_KEY_NIL = 0  # методо еще не вызывался
    CONST_IS_KEY_OK = 1  # метод отработат корректно
    CONST_GET_NIL = 0  # методо еще не вызывался
    CONST_GET_OK = 1  # метод отработат корректно
    CONST_GET_ERR = 2  # в массивет нет указанного ключа
    CONST_PUT_NIL = 0  # методо еще не вызывался
    CONST_PUT_OK = 1  # метод отработат корректно
    CONST_PUT_ERR = 2  # невозможно добавить новое значение

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.__hash_fun_status = self.CONST_HASH_FUN_NIL
        self.__is_key_status = self.CONST_IS_KEY_NIL
        self.__get_status = self.CONST_GET_NIL
        self.__put_status = self.CONST_PUT_NIL

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

    # предусловие: на вход поступает строка
    # постусловие: посчитан индекс для слота
    def hash_fun(self, value):
        # по входному значению вычисляет индекс для слота и возвращает его
        hash_result = self.__str_to_int(value) % self.size
        self.__hash_fun_status = self.CONST_HASH_FUN_OK
        return hash_result

    # постусловие: метод вернул True или False
    def is_key(self, key):
        # возвращает True, если ключ имеется в массиве. Иначе - возвращает False
        result = True
        index = self.hash_fun(key)
        if self.slots[index] != key:
            count = 0
            while count < self.size:
                if index + 1 <= self.size - 1:
                    index += 1
                elif index + 1 > self.size - 1:
                    index = 0
                if self.slots[index] == key:
                    self.__is_key_status = self.CONST_IS_KEY_OK
                    return result
                count += 1
            result = False
        self.__is_key_status = self.CONST_IS_KEY_OK
        return result

    # предусловие: ключ присутствует в массиве
    # постусловие: возвращено значение соответствующее ключу
    def get(self, key):
        # возврящает значение соответствующее ключу.
        if self.__get_is_key_status() == 1 and self.is_key(key) == True:
            index = self.hash_fun(key)
            while self.slots[index] != key:
                if index + 1 <= self.size-1:
                    index += 1
                else:
                    index = 0
            if self.slots[index] == key:
                self.__get_status = self.CONST_GET_OK
                return self.values[index]
        self.__get_status = self.CONST_GET_ERR

    # постусловие: значение записано в массив в соответствии с ключем
    def put(self, key, value):
        # записывает значение по ключу в массив
        index = self.hash_fun(key)
        if self.slots[index] is not None and self.slots[index] != key:
            count = 0
            while count < self.size:
                if index + 1 <= self.size-1:
                    index += 1
                else:
                    index = 0
                if self.slots[index] is None or self.slots[index] == key:
                    self.slots[index] = key
                    self.values[index] = value
                    self.__put_status = self.CONST_PUT_OK
                    return
                count += 1
            self.__put_status = self.CONST_PUT_ERR
        elif self.slots[index] is not None and self.slots[index] == key:
            self.slots[index] = key
            self.values[index] = value
        elif self.slots[index] is None:
            self.slots[index] = key
            self.values[index] = value
        self.__put_status = self.CONST_PUT_OK


    def __get_hash_fun_status(self):
        return self.__hash_fun_status

    def __get_is_key_status(self):
        return self.__is_key_status

    def __get_for_get_status(self):
        return self.__get_status

    def __get_put_status(self):
        return self.__put_status
