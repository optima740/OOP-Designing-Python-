# ЗАДАНИЕ 18.
"""
Классический вариант наследования. Классы потомки, специализируют родительский класс.
Например, родительский класс «Пилотируемый воздушный объект». Имеет потомков: «Самолет» и «Вертолет». Оба класса
потомка являются подмножеством множества «Пилотируемый воздушный объект», специализируя его функционал.

В случае наследования с ограничением, класс потомок, ограничивает родительский функционал. Это своего рода частный
случай, родительского класса, которым мы не можем пренебречь, и нам необходимо выделить данный функционал в отдельный
класс. Например, родительский класс «Роликовые коньки». Существую роликовые коньки специально для агрессивного стиля
(агрессивы). Они используются для исполнения различных трюков на специальных площадках. Класс потомок «Агрессив
Роликовые коньки» будут иметь ограниченный родительский функционал, но он важен в нашей иерархии классов
«Роликовые коньки».

Наследование с расширением, наоборот (в отличие от наследования с ограничением)
расширяет родительский функционал. Например, у нас есть родительский класс «Военный самолет» со своим набором
функционала. Мы создаем потомка «Военный самолет вертикального взлета», для возможности использовать самолет еще и в
палубной авиации. Тем самым, родительский класс «Военный самолет» станет подмножеством, множества
«Военный самолет вертикального взлета».
"""