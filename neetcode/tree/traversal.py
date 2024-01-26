from typing import Any
from collections import deque
class Node:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None
# Recursive version
def preorder(root:Node):
    result = []
    current = root
    
    def helper(current:Node):
        #base condition
        if current == None:
            return
        result.append(current.val) # visit(root)
        helper(current.left) # traverse left
        helper(current.right) # traverse right
        return
    helper(current)
    return result

def inorder(root:Node):
    result = []
    current = root
    
    def helper(current:Node):
        #base condition
        if current == None:
            return
        
        helper(current.left) # traverse left
        result.append(current.val) # visit(root)
        helper(current.right) # traverse right
        return
    helper(current)
    return result

def postorder(root:Node):
    result = []
    current = root
    
    def helper(current:Node):
        #base condition
        if current == None:
            return
        
        helper(current.left) # traverse left
        helper(current.right) # traverse right
        result.append(current.val) # visit(root)
        return
    helper(current)
    return result

def level_order(root:Node):
    if root == None:
        return

    result = []
    q = deque([root])

    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result

def main():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(4)
    root.right.left = Node(7)
    result = preorder(root)
    print('------preorder-------')
    print(result)
    result = inorder(root)
    print('------inorder-------')
    print(result)
    result = postorder(root)
    print('------postorder-------')
    print(result)
    result = level_order(root)
    print('------level_order-------')
    print(result)

if __name__ == "__main__":
    main()

