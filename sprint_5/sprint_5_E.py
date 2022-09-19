# coding: utf-8

# Comment it before submitting

# class Node:  
#     def __init__(self, value, left=None, right=None):  
#         self.value = value  
#         self.right = right  
#         self.left = left


def solution(root) -> bool:
    visited = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        visited.append(node.value)
        inorder(node.right)
    inorder(root)
    for i in range(1, len(visited)):
        if visited[i-1] >= visited[i]:
            return False
    return True

def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

if __name__ == "__main__":
    test()