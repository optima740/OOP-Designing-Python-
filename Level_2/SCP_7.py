# ЗАДАНИЕ 14.
"""
Небольшой пример иерархии классов: продукт, заказ. В качестве статуса заказа использован отдельный класс.
При необходимости расширить статусы (добавить новые, например: “ожидает оплаты” или “в доставке”) мы можем просто
наследовать новый класс-статус.
Правда, не совсем наверно эффективно в данном случае, что для одного поля (status) приходится создавать целый класс.
"""
class Product(object):
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Order(object):
    def __init__(self, id):
        self.id = id
        self.total_price = 0
        self.count = 0
        self.status = None

    def add_product(self, product):
        result_list = []
        result_list.append(product)
        self.calc_total_price(result_list)

    def calc_total_price(self, list_product):
        if len(list_product) > 0:
            for product in list_product:
                self.count += 1
                self.total_price += product.price

    def change_status(self, status_class):
        source_object = OrderInWorkStatus()
        if isinstance(source_object, status_class):
            self.status = status_class.status

    def print_order(self):
        print('total price=', self.total_price)
        print('count=', self.count)

class OrderInWorkStatus(object):
    def __init__(self):
        self.status = 'in work'

class OrderDoneStatus(OrderInWorkStatus):
    def __init__(self):
        self.status = 'done'

# ЗАДАНИЕ 15.
# Полиморфный вызов метода.
# Имеем простую иерархию:
class Parent(object):
    name = 'A'
    def get_status(self):
        print('its Parent')
    def get_name(self):
        print(self.name)

class Child(Parent):
    name = 'B'
    def get_status(self):
        # переопределяем метод
        print('its Child')

# создаем экземпляры классов:
P = Parent()
Ch = Child()

Ch.get_status()  # Полиморфный вызов - вызов переопределенного метода в классе потомка (Child)
Ch.get_name()  # т.к Child  метод в потомке отсутствует, то по списку наследования будет вызван метод родителя, но
               # переменная задействуется у класса потомка  (т.к. self - ссылка на собственный класс).

Ch = P           # полиморфное присваивание

Ch.get_status()  # в данном случае Ch хранит ссылку на экземпляр класса P (Parent), и будет вызван метод родиеля.

"""
Насколько я понял из теории, случай с ковариантным вызовом метода предполагает то,
что имея метод определенного типа (возможно обобщенного), мы передаем в качестве входного параметра аргумент. 
Данная операция будет успешна, если аргумент имеет тип ковариантный типу метода. (Тип данных аргумента, является 
подмножеством множества типа данных метода). Но в случае, если передаваемый аргумент является полиморфным объектом, то 
есть возможно принял другое значение, то мы не можем гарантировать валидность такой операции. И это приводит к 
неоднозначности. 
Из-за использования динамической типизации в Python могут возникать ситуации неоднозначности при вызове 
метода, т.к типизация параметров не явная. В следующем примере, я попытаюсь привести пример ковариантного вызова 
метода для случая с Python. 
    
"""
# Мы имеем два типа(класса). Тип А является базовым для типа B, (B - подмножество A).
class typeA(object):
    def __init__(self, arg):
        self.arg = arg


class typeB(typeA):
    pass
# Имеем два класса, Parent - является базовым для Child (Child - подмножество Parent)
class Parent1(object):

    def fooTypeA(self, arg: typeA):
        # тип функции является базовым типом
        A = typeA(arg)
        return A

class Child1(Parent1):

    def fooTypeB(self, arg: typeB):
        # тип функции является подмножеством базового типа A
        B = typeB(arg)
        return B

argA = typeA('typeA')  # аргумент типа А (базовый тип)
argB = typeB('typeB')  # аргумент типа В (подмножество типа А)

P1 = Parent1() # Создаем экземпляр класса, Parent - является базовым для Child

P1.fooTypeA(argB)  # вызываем метод типа TypeA. т.к тип аргумента, является подмножеством для типа функции,
# то мы имеем ковариантность.


