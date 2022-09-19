# coding: utf-8

#Comment it before submitting

# class Node:  
#     def __init__(self, value, left=None, right=None):  
#         self.value = value  
#         self.right = right  
#         self.left = left


def solution(root) -> int:
    res = []

    def preorder(node):
        if not node:
            return
        res.append(node.value)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    result = max(res)
    return result


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3

if __name__ == "__main__":
    test()