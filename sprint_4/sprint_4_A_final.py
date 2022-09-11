# coding: utf-8
# Successful submition: 70315137

"""
ПРИНЦИП РАБОТЫ
    Поисковая система состоит из двух частей - построение индекса по имеющимся
    документам и, собственно, самого поиска.
    Индекс представляет собой hash-таблицу вида {word: {doc_index: number}, ...}, ...}, 
    то есть для каждого слова в документе формируется пара номер_документа: частота появлений слова.

    Далее на вход в систему подаются запросы. На вход системе будут подаваться запросы. 
    Запрос —– некоторый набор слов. По запросу надо вывести 5 самых релевантных документов.
    
    Релевантность документа оценивается следующим образом:
    для каждого уникального слова из запроса берётся число его вхождений в документ,
    полученные числа для всех слов из запроса суммируются.
    Итоговая сумма и является релевантностью документа.
    Чем больше сумма, тем больше документ подходит под запрос.
    
    Сортировка документов на выдаче производится по убыванию релевантности.
    Если релевантности документов совпадают —– то по возрастанию их порядковых номеров.
ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Данная система является более простой версией любой поисковой системы (Yandex, Google...).
    В процессе реализации наткнулся на интересную статью: 
    https://ext-cachev2-itt03.cdn.yandex.net/download.yandex.ru/company/iworld-3.pdf?lid=1529
ВРЕМЕННАЯ СЛОЖНОСТЬ
    n - количество документов, m - количество запросов.
    Построение индекса - О(n^2).
    Запрос - О(m log(m)), так как применяем сортировку.
ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Для построения индекса необходимо О(n) памяти.
"""

import sys

from collections import Counter, defaultdict
from typing import List, Dict


def build_search_index(documents: List[List[str]]) -> Dict[str, Dict[int, int]]:
    search_index = defaultdict(dict)
    for doc, words in enumerate(documents):
        for word, count in Counter(words).items():
            search_index[word][doc] = count
    return search_index

def get_relevant_docs(search_index: Dict[str, Dict[int, int]], query: str, limit=5) -> List[int]:
    occurencies = defaultdict(int)
    for word in set(query.split()):
        if word in search_index:
            for doc_idx, count in search_index[word].items():
                occurencies[doc_idx] -= count
    most_relevant = [(count, index) for index, count in occurencies.items()]
    res = sorted([(count, index) for count, index in most_relevant if count < 0])[:limit]
    return [index for _, index in res]

if __name__ == "__main__":
    n = int(input())
    docs = [[]] + [input().split() for _ in range(n)]
    search_index = build_search_index(docs)
    m = int(input())
    for _ in range(m):
        res = get_relevant_docs(search_index, input())
        sys.stdout.write(
            " ".join(map(str, res)) + "\n"
        )