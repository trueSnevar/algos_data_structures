# coding: utf-8
# successful sumbission: 71169645

"""
ПРИНЦИП РАБОТЫ
    Дано двоичное дерево поиска, из которого нужно удалить узел
    с соответствующим значением таким образом, чтобы дерево оставалось
    корректным после удаления узла.
    С этой целью применяем следующий алгоритм:
        1) Сначала ищем узел, который нужно удалить;
        2) после того, как узел найден, обрабатываем случаи:
            а) если у узла отсутствуют дочерние узлы (узел является листом), то просто удаляем.
            б) иначе, чтобы сохранить валидность двоичного дерева поиска,
               нужно: 
                - заменить удаляемый узел на узел с максимальным значением
                  в левом поддереве удаляемого узла (если левое поддерево существует);
                - заменить удаляемый узел на узел с минимальным значением из правого
                  поддерева (если правое поддерево существует);
                - если существуют оба поддерева, то ищем минимальный узел в правом
                  поддереве. 
ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    В условии задачи сказано, что дерево является двоичным деревом поиска,
    а значит, то есть в левом поддереве любого узла находятся узлы со значениями,
    которые строго меньше значения узла, а в правом поддереве - узлы со значениями
    больше либо равными узловому значению. Следовательно и искать узел для замены
    удаляемого нужно либо в самом правом листе левого поддерева, либо в самом левом 
    листе правого поддерева.
ВРЕМЕННАЯ СЛОЖНОСТЬ
    В худшем случае для поиска узла взамен удаляемого потребуется опуститься
    на всю глубину дерева, то есть временная сложность составит О(h), 
    где h - высота дерева.
ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Дополнительная память не используется. Однако, поскольку в реализации
    используется рекурсия, нужно помнить, что каждый новый вызов хранится
    в стеке, размер которого может достигать глубины дерева O(h), где h - 
    высота дерева.
"""


# Comment it before submitting
# class Node:  
#     def __init__(self, left=None, right=None, value=0):  
#         self.right = right
#         self.left = left
#         self.value = value

def remove(root, key):
    if not root:
        return None
    if root.value == key:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        min_node = get_min_node(root.right)
        root.right = remove(root.right, min_node.value)
        min_node.left = root.left
        min_node.right = root.right
        root = min_node
    elif root.value < key:
        root.right = remove(root.right, key)
    else:
        root.left = remove(root.left, key)
    return root

def get_min_node(node):
    while node.left:
        node = node.left
    return node
            
def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8

# if __name__ == "__main__":
#     test()