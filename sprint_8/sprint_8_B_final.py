# coding: utf-8
# Successful submission: 75340100

"""
ПРИНЦИП РАБОТЫ
    Необходимо создать Trie, префиксное дерево, в которое нужно вставить все слова входного
    списка строк, на которые потенциально можно разбить входную строки-шаблон (или нельзя).

    Далее, итерируясь по индексам символов строки-шаблона, будет проверять, можно ли найти
    в дереве Trie такой префикс строки-шаблона, который совпадал бы со словом из входного списка.
    В этом нам поможет свойство узла дерева, указывающее на терминальность узла. Таким образом, нужно
    отметить все индексы символов входной строки как True, если символы под этими индексами обозначают
    начальный и/или конечный символы в словах.
ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    - Базовым случаем динамики является пустая строка. Считаем, что она таковая всегда
      присутствует в префиксном дереве.

    - Переходом динамики является проверка каждой подстроки вхдной строки-шаблона
      на нахождение в построенном префиксном дереве Trie. Если очередной символ подстроки
      помечен в дереве как терминальный узел, то в соответствующий индекс массива динамики
      записываем True.

    - Ответ будет храниться в последнем элементе списка динамики, т.е. если последний символ
      входной строки шаблона одновременно является терминальным узлом (с учетом предыдущего разбиения),
      то значит, что и вся входная строка-шаблон может быть разбита на слова во входном списке строк.

                                 term  term                term    
      dp =  [True, False, False, True, True, False, False, True]
      s =   "  _      a     b      a     c     a      b      a  "
      words =         a     b      a     c
                                         c     a      b      a
                                               a      b      a

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Построение Trie занимает - O(L), где L — суммарная длина всех слов во входном списке строк.
    Прохождение по префиксному дереву - O(n^2), где n - длина входной строки-шаблона.
ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Хранение Trie требует O(L), где L — суммарная длина всех слов во входном списке строк.
    Список хранения динамики - O(n), где n - длина входной строки-шаблона.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_terminal = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_terminal
    
def is_splittable(s: str, root: Trie) -> bool:
    n = len(s)
    dp = [True] + [False] * n
    for i in range(n):
        node = root
        if dp[i]:
            for j in range(i, n + 1):
                if node.is_terminal:
                    dp[j] = True
                if j == len(s) or not node.children.get(s[j], False):
                    break
                node = node.children[s[j]]
    return dp[-1]

if __name__ == "__main__":
    s: str = input()
    n: int = int(input())
    trie = Trie()
    for _ in range(n):
        word = input()
        trie.insert(word)
    res: bool = is_splittable(s, trie.root)
    print("YES" if res else "NO")