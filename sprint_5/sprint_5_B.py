# coding: utf-8

# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def solution(root):
    
    def dfs(node):
        if not node:
            return [True, 0]
        left, right = dfs(node.left), dfs(node.right)
        balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
        return [balanced, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)

if __name__ == "__main__":
    test()