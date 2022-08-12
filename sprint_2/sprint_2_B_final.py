# -*- coding: utf-8 -*-
# successful submission: 69652441

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

from typing import List

def parse_rpn(expression: List) -> int:
    """ Parse math expression 
    written with the reversed polish notaion.

    Example input: 3 4 + 
    Output: 7

    """
    stack = []
    for char in expression:
        if char not in '/*+-':
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '/':
                res = a // b
            elif char == '*':
                res = a * b
            elif char == '+':
                res = a + b
            else:
                res = a - b
            stack.append(res)
    return stack.pop()

if __name__ == "__main__":
    exp = list(input().split(" "))
    print(parse_rpn(exp))