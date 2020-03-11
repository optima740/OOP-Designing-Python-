from abc import ABC, abstractmethod

class abstractPowerSet(ABC):

    @abstractmethod
    def __init__(self):
        # создает структуру данных под множество фиксированного размера
        # за основу берем хэш-таблицу (словарь), где key и value - имеют одинаковое значение
        pass

    # КОМАНДЫ:

    @abstractmethod
    # предусловие: добавляемое значение уникально, множество его не содержит
    # постусловие: новое значение добавлено во множество.
    def put(self):
        # добавляет новое значение во множество. Если добавляемое значение уже присутствует, то ничего не делает
        pass

    @abstractmethod
    # предусловие: удаляемое значение присутствует во множестве
    # постусловие: множество больше не содержит данного значения
    def remove(self):
        # удаляет значение из множества если оно присутствует, или ничего не делает
        pass

    @abstractmethod
    # постусловие: сформировано новое множество из общих (одинаковых) значений, которые присутствуют в обоих множествах
    def intersection(self):
        # пересечение текущего множества и set2
        pass

    @abstractmethod
    # постусловие: сформировани новое множество из значений каждого из множеств.
    def union(self):
        # объединение текущего множества и set2
        pass

    @abstractmethod
    # постусловие: сформировани новое множество из значений, которые не входят во второе множество (множество-параметр)
    def difference(self):
        # разница текущего множества и set2
        pass

    # ЗАПРОСЫ:

    @abstractmethod
    # постусловие: вычислено кол-во элементов множества
    def size(self):
        # возвращает размер множества
        pass

    @abstractmethod
    # постусловие: если значение имеется во множестве - возвращается True, иначе - False
    def get(self):
        # проверяет наличие значения во множестве
        pass

    @abstractmethod
    # постусловие: если текущее множество содержит все элементы другого множества - True, иначе - False
    def issubset(self):
        # проверяет, содержит ли текущее множество все элементы другого множества (множество-параметр)
        pass

    # СТАТУСЫ:

    CONST_PUT_NIL = 0             # метод еще не вызывался
    CONST_PUT_OK = 1              # метод отработал корректно
    CONST_PUT_ERR = 2             # добавляемое значение уже присутствует во множестве
    CONST_REMOVE_NIL = 0          # метод еще не вызывался
    CONST_REMOVE_OK = 1           # метод отработал корректно
    CONST_REMOVE_ERR = 2          # удаляемого значения нет в данном множестве
    CONST_INTERSECTION_NIL = 0    # метод еще не вызывался
    CONST_INTERSECTION_OK = 1     # метод отработал корректно
    CONST_UNION_NIL = 0           # метод еще не вызывался
    CONST_UNION_OK = 1            # метод отработал корректно
    CONST_DIFFERENCE_NIL = 0      # метод еще не вызывался
    CONST_DIFFERENCE_OK = 1       # метод отработал корректно
    CONST_SIZE_NIL = 0            # метод еще не вызывался
    CONST_SIZE_OK = 1             # метод отработал корректно
    CONST_GET_NIL = 0             # метод еще не вызывался
    CONST_GET_OK = 1              # метод отработал корректно
    CONST_ISSUBSET_NIL = 0        # метод еще не вызывался
    CONST_ISSUBSET_OK = 1         # метод отработал корректно

    # ЗАПРОСЫ ДЛЯ СТАТУСОВ:

    @abstractmethod
    def __get_put_status(self):
        pass

    @abstractmethod
    def __get_remove_status(self):
        pass

    @abstractmethod
    def __get_intersection_status(self):
        pass

    @abstractmethod
    def __get_union_status(self):
        pass

    @abstractmethod
    def __get_difference_status(self):
        pass

    @abstractmethod
    def __get_size_status(self):
        pass

    @abstractmethod
    def __get_for_get_status(self):
        pass

    @abstractmethod
    def __get_issubset_status(self):
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
    CONST_STR_TO_INT_OK = 1  # метод отработал корректно
    CONST_REMOVE_NIL = 0  # метод еще не вызывался
    CONST_REMOVE_OK = 1  # метод отработал корректно
    CONST_REMOVE_ERR = 2  # значение которое нужно удалить, отсутствует в хэш-таблице

    def __init__(self, sz):
        # создает структуру данных под hash-таблицу размером sz содержащая пустые слоты (None)
        # c постоянным шагом смещения при коллизии
        CONST_STEP = 1
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
                index = (index + self.step) - self.size
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
        while count <= self.size - 1:
            if self.slots[find_index] == value:
                self.__find_status = self.CONST_FIND_OK
                return find_index
            if find_index + self.step > self.size - 1:
                find_index = (find_index + self.step) - self.size
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

class PowerSet(HashTable):
    CONST_PUT_NIL = 0  # метод еще не вызывался
    CONST_PUT_OK = 1  # метод отработал корректно
    CONST_PUT_ERR = 2  # добавляемое значение уже присутствует во множестве
    CONST_REMOVE_NIL = 0  # метод еще не вызывался
    CONST_REMOVE_OK = 1  # метод отработал корректно
    CONST_REMOVE_ERR = 2  # удаляемого значения нет в данном множестве
    CONST_INTERSECTION_NIL = 0  # метод еще не вызывался
    CONST_INTERSECTION_OK = 1  # метод отработал корректно
    CONST_UNION_NIL = 0  # метод еще не вызывался
    CONST_UNION_OK = 1  # метод отработал корректно
    CONST_DIFFERENCE_NIL = 0  # метод еще не вызывался
    CONST_DIFFERENCE_OK = 1  # метод отработал корректно
    CONST_SIZE_NIL = 0  # метод еще не вызывался
    CONST_SIZE_OK = 1  # метод отработал корректно
    CONST_GET_NIL = 0  # метод еще не вызывался
    CONST_GET_OK = 1  # метод отработал корректно
    CONST_ISSUBSET_NIL = 0  # метод еще не вызывался
    CONST_ISSUBSET_OK = 1  # метод отработал корректно

    def __init__(self):
        super(PowerSet, self).__init__(20000)
        self.util_index = []
        self.size_count = 0
        self.__put_status = self.CONST_PUT_NIL
        self.__remove_status = self.CONST_REMOVE_NIL
        self.__intersection_status = self.CONST_INTERSECTION_NIL
        self.__union_status = self.CONST_UNION_NIL
        self.__difference_status = self.CONST_DIFFERENCE_NIL
        self.__size_status = self.CONST_SIZE_NIL
        self.__get_status = self.CONST_GET_NIL
        self.__issubset_status = self.CONST_ISSUBSET_NIL

    # постусловие: если значение имеется во множестве - возвращается True, иначе - False
    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        index_get = self.find(value)
        self.__get_status = self.CONST_GET_OK
        if self.__get_find_status() == 1 and index_get is not None:
            return True
        else:
            return False

    # предусловие: добавляемое значение уникально, множество его не содержит
    # постусловие: новое значение добавлено во множество.
    def put(self, value):
        if self.get(value) is False:
            index_put = self.seek_slot(value)
            if self.__get_seek_slot_status() == 1 and index_put is not None:
                self.slots[index_put] = value
                self.size_count += 1
                self.util_index.append(index_put)
                self.__put_status = self.CONST_PUT_OK
                return
        self.__put_status = self.CONST_PUT_ERR
        # всегда срабатывает

    def __seek_for_del(self, value):
        # вспомогательный метод для удаления.
        # ищет слот со значением и возвращает его индекс для удаления
        count = 0
        index = self.hash_fun(value)
        while count <= self.size_n - 1:
            if  self.slots[index] == value:
                return index
            if index + self.step > self.size_n - 1:
                index = (index + self.step) - self.size_n
            else:
                index += self.step
            count += 1

    # предусловие: удаляемое значение присутствует во множестве
    # постусловие: множество больше не содержит данного значения
    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        if self.get(value):
            index_remove = self.__seek_for_del(value)
            if index_remove is not None and self.slots[index_remove] == value:
                self.slots[index_remove] = None
                self.size_count -= 1
                self.util_index.remove(index_remove)
                self.__remove_status = self.CONST_REMOVE_OK
                return True
        else:
            self.__remove_status = self.CONST_REMOVE_ERR
            return False

    # постусловие: сформировано новое множество из общих (одинаковых) значений, которые присутствуют в обоих множествах
    def intersection(self, set2):
        # пересечение текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            if set2.get(value):
                set3.put(value)
        self.__intersection_status = self.CONST_INTERSECTION_OK
        return set3

    # постусловие: сформировани новое множество из значений каждого из множеств.
    def union(self, set2):
        # объединение текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            set3.put(value)
        for i in set2.util_index:
            value = set2.slots[i]
            set3.put(value)
        self.__union_status = self.CONST_UNION_OK
        return set3

    # постусловие: сформировани новое множество из значений, которые не входят во второе множество (множество-параметр)
    def difference(self, set2):
        # разница текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            if set2.get(value) is False:
                set3.put(value)
        self.__difference_status = self.CONST_DIFFERENCE_OK
        return set3

    # постусловие: если текущее множество содержит все элементы другого множества - True, иначе - False
    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        self.__issubset_status = self.CONST_ISSUBSET_OK
        for i in set2.util_index:
            value = set2.slots[i]
            if self.get(value) is False:
                return False
        return True

    def size(self):
        self.__size_status = self.CONST_SIZE_OK
        return self.size_count

    def __get_put_status(self):
        return self.__put_status

    def __get_remove_status(self):
        return self.__remove_status

    def __get_intersection_status(self):
        return self.__intersection_status

    def __get_union_status(self):
        return self.__union_status

    def __get_difference_status(self):
        return self.__difference_status

    def __get_size_status(self):
        return self.__size_status

    def __get_for_get_status(self):
        return self.__get_status

    def __get_issubset_status(self):
        return self.__issubset_status