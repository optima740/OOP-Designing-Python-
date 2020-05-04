# ЗАДАНИЕ 21.

"""
Наследование вида.
Рассмотрим ситуацию в которой требуется создать иерархию классов для описания работы фитнесс-центра.
У нас есть базовый класс «Абонемент», от которого будут наследованы следующие классы: «Годовой», «Полугодовой» и
«Разовый». Все они отличаются стоимостью, продолжительностью своего действия и набором включенных услуг. Кроме того,
в абонемент нам необходимо включить программу тренировок, например, для мужчин и для женщин.
Но в нашем фитнесс-центре подумывают в будущем и о занятиях для детей. Поэтому нам необходимо предусмотреть
возможность масштабирования программ тренировок. Для этого создадим базовый класс «Спортивная программа» от
которого наследуем (льготное наследование) классы «Тренировки для женщин», «Тренировки для мужчин»,
«Тренировки для детей». При помощи композиции (has-a) используем все в единой системе с абонементами.
"""

class Ticket(object):
    # описываем базовый класс для абонемента.
    def __init__(self, days, list_service, TrainingProgram, price):
        self.title = 'Ticket'
        self.period = days
        self.additional_services = list_service
        self.training_program = TrainingProgram
        self.price = price

    def use_training(self):
        # метод использования абонемента - уменьшает оставшиеся дни.
        if self.get_available() != 0:
            self.period -= 1
            return True
        return False

    def get_available(self):
        # метод показывает сколько осталось дней заниматься.
        return self.period

    def get_title_ticket(self):
        # возвращает заголовок - тип абонемента (период действия)
        return self.title

class AllYearTicket(Ticket):
    # Абонемент на весь год.
    def __init__(self, list_period, list_service, TrainingProgram, price):
        super().__init__(list_period, list_service, TrainingProgram, price)
        self.title = 'ALL_YEAR'

class HalfYearTicket(Ticket):
    # Абонемент на пол-года.
    def __init__(self, list_period, list_service, TrainingProgram, price):
        super().__init__(list_period, list_service, TrainingProgram, price)
        self.title = 'HALF_YEAR'

class SportProgram(object):
    # описываем базовый класс для программы тренировок.
    def __init__(self, program):
        self.title = 'Title'
        self.program = program

    def get_title(self):
        # возвращает заголовок. (для кого данная программа)
        return self.title


class ProgramForGirls(SportProgram):
    # класс-потомок содержащий тренеровки для девушек.
    def __init__(self, program):
        super().__init__(program)
        self.title = 'FOR_GIRLS'

class ProgramForBoys(SportProgram):
    # класс-потомок содержащий тренеровки для парней.
    def __init__(self, program):
        super().__init__(program)
        self.title = 'FOR_BOYS'