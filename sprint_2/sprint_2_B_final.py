# -*- coding: utf-8 -*-
# successful submission: 69654571

"""
-- ПРИНЦИП РАБОТЫ --
Реализована функция-парсер обратной 
польской записи с использованием стека.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Поскольку операнды расположены перед
знаком арифметической операции, необходимо
сохранять их порядок следования после того, как
они были извлечены из входного списка. Для этой
цели подойтет структура данных, работающая 
по принципу FIFO. В этом случае при операции
деление сначала извлекается знаменатель, затем 
числитель. Результат вычисления одной операции
также кладется в стек. 


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Так как необходимо проитерироваться по 
каждому элемету входных данных (списка), временная
сложность будет линейно зависить от размера входных
данных, то есть О(n).


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В данной алгоритме используется 
дополнительная память в виде стека, то
я бы оценил и просранственную сложность O(n)
в худшем случае.
"""

import operator

from typing import List

def parse_rpn(expression: List) -> int:
    """ Parse math expression 
    written with the reversed polish notaion.

    Example input: 3 4 + 
    Output: 7

    """
    operations = {
        '/': operator.floordiv,
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub,
    }
    stack = []
    for char in expression:
        if char not in operations:
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            res = operations[char](a, b)
            stack.append(res)
    return stack.pop()

if __name__ == "__main__":
    exp = list(input().split(" "))
    print(parse_rpn(exp))