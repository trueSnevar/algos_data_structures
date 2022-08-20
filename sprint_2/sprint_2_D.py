# coding: utf-8
# https://contest.yandex.ru/contest/22779/problems/D/

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item

def solution(node: Node, elem: str) -> int:
    """ Checks if a given elem
    exists in a given linked list.
    
    """
    idx, cur_node = 0, node
    while cur_node is not None:
        if cur_node.value == elem:
            return idx
        cur_node = cur_node.next_item
        idx += 1
    return -1

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2

if __name__ == '__main__':
    test()
