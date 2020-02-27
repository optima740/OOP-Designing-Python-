from abc import ABC, abstractmethod
import ctypes

class My_DynArray(ABC):

    #КОНСТРУКТОР:

    @abstractmethod
    def __init__(self):
        # задает первоначальную емкость - capacity (порог), при пересечении которого массив увеличивается или уменьшается
        # создает в памяти объект ссылающийся на экземпляр типа py_object, размером capacity, который возвращает make_array()
        pass

    #КОМАНДЫ:

    #предусловие: указанный размер корректен
    #постусловие: создан экземпляр типа py_object размера capacity
    @abstractmethod
    def make_array(self):
        # выделяет память на необходимое кол-во элементов (capacity) типа py_object и создает экземпляр данного типа
        pass

    #предусловие: указанный размер корректен
    #постусловие: размер массива переопределен
    @abstractmethod
    def resize(self):
        # получает новый размер массива, создает новый экземпляр класса py_object, согласно новому размеру.
        # пререносит элементы из старого массива в новый
        pass

    #предусловие: добавляемый элемент помещается в текущую емкость массива. Иначе вызвать метод resize() и удвоить емкость
    #постусловие: новый элемент добавился в хвост массива
    @abstractmethod
    def append(self):
        # добавляет новый элемент в массив текущей емкости(если она позволяет).
        # иначе, удвоить емкость и добавить элемент.
        pass

    #предусловие: индекс нового элемента не выходит за пределы выделенного массива
    #постусловие: новый элемент присутствует под указанным индексом. размер массива корректен.
    @abstractmethod
    def insert(self):
        #вставляет новый элемент по указанному индексу. Если массив заполнен, то методом resize() он удваивается
        pass

    # предусловие: массив не пуст. индекс удаляемого элемента не выходит за пределы выделенного массива
    # постусловие: элемент удален. размер массива корректен
    @abstractmethod
    def delete(self):
        #удаляет элемент по указанному индексу. если после удаления размер массива стал меньше порогового значения,
        #методом resize() он уменьшается.
        pass

    #ЗАПРОСЫ:

    # предусловие: массив не пуст. искомый индекс не выходит за рамки массива
    # постусловие: получен элемент согласно заданному индексу
    @abstractmethod
    def get_item(self):
        # возвращает значение элемента соответсвующего указанному индексу
        pass

    @abstractmethod
    def len_array(self):
        #возвращает текущую длину массива
        pass

    #СТАТУСЫ:

    CONST_MAKE_ARRAY_NIL = 0    # ни разу не вызывался
    CONST_MAKE_ARRAY_OK = 1     # метод выполнился
    CONST_MAKE_ARRAY_ERR = 2    # указан некорректный размер
    CONST_RESIZE_NIL = 0        # ни разу не вызывался
    CONST_RESIZE_OK = 1         # метод выполнился
    CONST_RESIZE_ERR = 2        # указан некорректный размер
    CONST_APPEND_NIL = 0        # ни разу не вызывался
    CONST_APPEND_OK = 1         # метод выполнился
    CONST_INSERT_NIL = 0        # ни разу не вызывался
    CONST_INSERT_OK = 1         # метод выполнился
    CONST_INSERT_ERR = 2        # указанный индекс лежит за пределами массива
    CONST_DELETE_NIL = 0        # ни разу не вызывался
    CONST_DELETE_OK = 1         # метод выполнился
    CONST_DELETE_ERR = 2        # массив пуст или указанный индекс лежит за пределами массива
    CONST_GET_ITEM_NIL = 0      # ни разу не вызывался
    CONST_GET_ITEM_OK = 1       # метод выполнился
    CONST_GET_ITEM_ERR = 2      # массив пуст или указанный индекс лежит за пределами массива
    CONST_LEN_ARRAY_NIL = 0     # ни разу не вызывался
    CONST_LEN_ARRAY_OK = 1      # метод выполнился


    #ЗАПРОСЫ ДЛЯ СТАТУСОВ

    @abstractmethod
    def get_make_array_status(self):
        pass

    @abstractmethod
    def get_resize_status(self):
        pass

    @abstractmethod
    def get_append_status(self):
        pass

    @abstractmethod
    def get_insert_status(self):
        pass

    @abstractmethod
    def get_delete_status(self):
        pass

    @abstractmethod
    def get_for_get_item_status(self):
        pass

    @abstractmethod
    def get_len_array_status(self):
        pass

class My_DynArray:
    CONST_MAKE_ARRAY_NIL = 0  # ни разу не вызывался
    CONST_MAKE_ARRAY_OK = 1  # метод выполнился
    CONST_MAKE_ARRAY_ERR = 2  # указан некорректный размер
    CONST_RESIZE_NIL = 0  # ни разу не вызывался
    CONST_RESIZE_OK = 1  # метод выполнился
    CONST_RESIZE_ERR = 2  # указан некорректный размер
    CONST_APPEND_NIL = 0  # ни разу не вызывался
    CONST_APPEND_OK = 1  # метод выполнился
    CONST_INSERT_NIL = 0  # ни разу не вызывался
    CONST_INSERT_OK = 1  # метод выполнился
    CONST_INSERT_ERR = 2  # указанный индекс лежит за пределами массива
    CONST_DELETE_NIL = 0  # ни разу не вызывался
    CONST_DELETE_OK = 1  # метод выполнился
    CONST_DELETE_ERR = 2  # массив пуст или указанный индекс лежит за пределами массива
    CONST_GET_ITEM_NIL = 0  # ни разу не вызывался
    CONST_GET_ITEM_OK = 1  # метод выполнился
    CONST_GET_ITEM_ERR = 2  # массив пуст или указанный индекс лежит за пределами массива
    CONST_LEN_ARRAY_NIL = 0  # ни разу не вызывался
    CONST_LEN_ARRAY_OK = 1  # метод выполнился

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

        self.__make_array_status = self.CONST_MAKE_ARRAY_NIL
        self.__resize_status = self.CONST_RESIZE_NIL
        self.__append_status = self.CONST_APPEND_NIL
        self.__insert_status = self.CONST_INSERT_NIL
        self.__delete_status = self.CONST_DELETE_NIL
        self.__get_item_status = self.CONST_GET_ITEM_NIL
        self.__len_array_status = self.CONST_LEN_ARRAY_NIL


    def make_array(self, new_capacity):
        if new_capacity > 0:
            self.__make_array_status = self.CONST_MAKE_ARRAY_OK
            return (new_capacity * ctypes.py_object)()
        self.__make_array_status = self.CONST_MAKE_ARRAY_ERR

    def len_array(self):
        self.__len_array_status = self.CONST_LEN_ARRAY_OK
        return self.count

    def resize(self, new_capacity):
        if new_capacity > 0:
            new_array = self.make_array(new_capacity)
            for i in range(self.count):
                new_array[i] = self.array[i]
            self.array = new_array
            self.capacity = new_capacity
            self.__resize_status = self.CONST_MAKE_ARRAY_OK
            return
        self.__resize_status = self.CONST_RESIZE_ERR

    def append(self, item):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = item
        self.count += 1
        self.__append_status = self.CONST_APPEND_OK

    def insert(self, index, item):
        if self.len_array() > 0  and index > 0 and not index < self.count:
            if self.count == index:
                self.append(item)
            else:
                if self.count == self.capacity:
                    self.resize(2 * self.capacity)
                tmp_loc = self.make_array(self.count - index)
                j = 0
                for k in range(index, self.count):
                    tmp_loc[j] = self.array[k]
                    j += 1
                self.array[index] = item
                j = 0
                for k in range(index+1, self.count + 1):
                    self.array[k] = tmp_loc[j]
                    j += 1
                self.count += 1
        elif self.len_array() == 0 and index == 0:
            self.append(item)
        else:
            self.__insert_status = self.CONST_INSERT_ERR
            return
        self.__insert_status = self.CONST_INSERT_OK


    def delete(self, index):
        if self.len_array() > 0 and index > 0:
            capacity_to_del = int(self.capacity / 1.5)
            if index == (self.count - 1):
                if index > 0 and self.count > 1:
                    tmp_loc = self.make_array(self.count - 1)
                    for k in range(0, index):
                        tmp_loc[k] = self.array[k]
                    self.array = tmp_loc
                    self.count -= 1
                if self.count < (0.5 * self.capacity) and self.capacity > 16:
                    if capacity_to_del > 16:
                        self.resize(capacity_to_del)
                        self.__delete_status = self.CONST_DELETE_OK
                        return
                    else:
                        self.resize(16)
                if index == 0 and self.count == 1:
                    self.count = 0
                    self.array = self.make_array(self.capacity)
            else:
                tmp_loc = self.make_array(self.count-1)
                j = 0
                for k in range(self.count):
                    if k != index:
                        tmp_loc[j] = self.array[k]
                        j += 1
                self.array = tmp_loc
                self.count -= 1
                if self.count < (0.5 * self.capacity) and self.capacity > 16:
                    if capacity_to_del > 16:
                        self.resize(capacity_to_del)
                        self.__delete_status = self.CONST_DELETE_OK
                        return
                    else:
                        self.resize(16)
            self.__delete_status = self.CONST_DELETE_OK
        else:
            self.__delete_status = self.CONST_DELETE_ERR

    def get_item(self, index):
        if index >= 0 and index < self.count:
            self.__get_item_status = self.CONST_GET_ITEM_OK
            return self.array[index]
        self.__get_item_status = self.CONST_GET_ITEM_ERR

    def get_len_array_status(self):
        return self.__len_array_status

    def get_make_array_status(self):
        return self.__make_array_status

    def get_for_get_item_status(self):
        return self.__get_item_status

    def get_resize_status(self):
        return self.__resize_status

    def get_append_status(self):
        return self.__append_status

    def get_insert_status(self):
        return self.__insert_status

    def get_delete_status(self):
        return self.__delete_status




