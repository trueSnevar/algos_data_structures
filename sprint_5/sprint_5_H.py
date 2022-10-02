# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def solution(root) -> int:
    
    def find_solution(root, curr):
        if not root:
            return 0
        curr = curr * 10 + root.value
        if not root.left and not root.right:
            return curr
        return find_solution(root.left, curr) + find_solution(root.right, curr)
    
    return find_solution(root, 0)



def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)
    
    assert solution(node5) == 275

if __name__ == "__main__":
    test()