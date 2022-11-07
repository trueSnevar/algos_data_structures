# coding: utf-8
# successful submission: 74015879

"""
ПРИНЦИП РАБОТЫ
    Расстояние Левенштейна показывает разность между двумя
    последовательностями символов и вычисляется, как сумма
    минимлального количества односимвольных операций, необходимых
    для преобразования одной строки (последовательности символов) в другую.
    Всего существует три типа операций над символов - вставка, изменение и 
    удаление.

    Следовательно, принцип работы алгоритма заключается в следующем:
    если два рассматриваемых символа являются одинаковыми, то ничего не
    требуется делать - количество операций не увеличивается. Если же два
    рассматриваемых символа различны, необходимо из трех вариантов
    вышеперечисленных операций выбрать такую, которая окажется наиболее 
    выгодной для дальнейшего преобразования рассматриваемых последовательностей.

ДОКАЗАТЕЛЬСТВО КОРРЕКТОСТИ
    Для решения задачи воспользуемся методом динамического
    программирования "назад", то есть будем рассматривать
    полученные на вход строки с их последних символов.

    В двумерном массиве (матрице) dp, на пересечении
    столбца и строки (i, j) будет хранится количество
    операций, необходимых для преобразования одной строки
    в другую.

    Базовым случаем динамики будет сравнение двух пустых
    строк (кол-во операций = 0), а также преобразование, 
    когда одна из строк пустая. Во втором случае количество
    операций = длине непустой строки.

    Переходом динамики будет вычисление кол-ва операций при
    сравнении символов dp[i][j] в зависимости от условий по 
    следущим формулам:

        1) если рассматриваемые символы совпадают, то кол-во
        операций не изменится, следовательно нужно просто 
        скопировать значение для предыдущих символов (на самом
        деле они следущие за рассматриваемыми, так как мы идем
        в обратном порядке), которое хранится в ячейке dp[i+1][j+i];

        2) Если символы не совпадают, то у нас есть три варианта действий:
            
            1. вставить символ из 2й строки в первую. В этом случае нам необходимо
            остаться на текущем символе из первой строки, и передвинуть 
            указатель символа из второй строки на следующий: (i, j+1)

            2. Удалить символ из 1й строки. В случае удаления необходимо
            сдвинуть указатель на 1й строки, оставив указатель на символ 2й 
            строки на текущей позиции: (i+1, j).

            3. Заменить символ из 1й строки на символ из второй строки. В этом
            случае необходимо сдвинуть оба указателя: (i+1, j+1).

        А так как мы ищем минимальное расстояние, то необходимо взять наиболее
        выгодное (минимальное) значение из трех предыдущих вариантов, прибавив единицу для
        выполнения текущей операции: dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        Ответ будет хранится на пересечении первых символов последовательностей, то есть в 
        ячейке dp[0][0]:

        a  c  d  " "
      a 1  2  2  3
      b 2  1  1  2
      d 2  1  0  1
    " " 3  2  1  0 

    НО! Данное решение можно упростить, применив одномерный массив. Это даст нам значительный
    выигрыш по используемой памяти. Несложно увидеть, что на каждой итерации мы используем лишь
    две строки двумерного массива - текущую и предыдущую, поэтому нет нужды хранить матрицу целиком,
    можно ограничиться двумя строками, при этом на выходе получится одномерный массив, и ответ будет
    храниться в его последнем элементе.
ВРЕМЕННАЯ СЛОЖНОСТЬ
    Необходимо рассмотреть и сравнить каждый символ из 1й последовательности с
    каждым символом из 2й последовательности, а значит временная сложность составит
    O(n * m)

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Для хранения результатов вычислений динамики нам понадобится массив,
    размером наименьшей из длин строк + 1, а значит памяти потребуется O(min(m,n)) = O(n).

"""

def get_levenshtein_distance(str1: str, str2: str) -> int:
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    n, m = len(str1), len(str2)

    dp = [c for c in range(n + 1)]

    for i in range(n):
        prev_row, dp = dp, [i+1] + [0] * m
        for j in range(m):
            if str1[i] == str2[j]:
                dp[j+1] = prev_row[j]
            else:
                dp[j+1] = 1 + min(dp[j], prev_row[j], prev_row[j+1])

    return dp[m]

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(get_levenshtein_distance(s1, s2))