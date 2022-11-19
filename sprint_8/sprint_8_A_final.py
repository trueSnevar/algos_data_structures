# coding: utf-8
# Successful submission: 75349307

"""
ПРИНЦИП РАБОТЫ
    Наибольший общий префикс можно найти эффективно, используя достаточно прямой/наивный
    алгорит - нужно выбрать любую строку и списка входящих строк, и найти в первый попавшийся
    несовпадающий символ в любой другой строке.

    Проблема в том, что строки у нас запакованы, и сначала их нужно расшифровать.
    Для этого воспользуемся стэком - будем добавлять в стэк символы строки, пока не 
    встретим закрывающую квадратную скобку ']'. Это будет сигналом к тому, что можно
    распаковать стэк (в обратном порядке, естественно), пока не встретим уже открывающую
    скобку '[', при этом буквенные символы будем сохранять в подстроку. 
    Останется только вытащить из стэка числовые символы, идущие перед открывающей 
    скобкой и повторить сформированную подстроку n раз, где n - получившееся число
    из числовых символов. И так сделаем для всех строк входного списка.
    
ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    
    words = ['abacabaca', 'abacadaca', 'abaabaaba']

    В данном алгоритме нам неважно, какую строку взять в качестве шаблона. Даже если
    это будет самая короткая строка, то мы этот случай учтем и оставим поиск. В случае
    первого несовпадения также остановим поиск, а пока символы совпадают, записываем их
    в ответ, т.е. prefix.

    шаблон = a b a |c a b a c a
             a b a |c a d a c a
             a b a |a b a a b a
    
    prefix = aba

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Распаковка строк занимает О(L), L - где сумма длин всех входных зашифрованных строк.
    Построение префикса потребует в худшем случае О(min(|s|)), где |s| - длина строки, взятая
    в кач-ве шаблона.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Нам необходим массив размера О(L), L - где сумма длин всех декодированных строк.
    Также нам необходимо место для хранения префикса, который в худшем случае займет
    О(min(|s|)), где |s| - длина декодированной строки.
"""

from typing import List

def decode_string(s: str) -> str:
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            substring = ""
            while stack[-1] != '[':
                substring = stack.pop() + substring
            stack.pop() # remove '[' as well

            n = ""
            while stack and stack[-1].isdigit():
                n = stack.pop() + n
            stack.append(int(n) * substring)
    return "".join(stack)

def decode_strings(lst: List[str]) -> List[str]:
    res = []
    for s in lst:
        decoded = decode_string(s)
        res.append(decoded)
    return res

def longest_common_prefix(strs: List[str]) -> str:
    prefix = ""
    just_str = strs[0]
    for idx, char in enumerate(just_str):
        for s in strs:
            if idx == len(s) or s[idx] != char:
                return prefix 
        prefix += char
    
    return prefix

if __name__ == "__main__":
    n = int(input())
    data = []
    for _ in range(n):
        s = input()
        data.append(s)
    decoded_data = decode_strings(data)
    print(longest_common_prefix(decoded_data))

