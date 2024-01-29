from typing import Any
from collections import deque
class TreeNode:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None
# Recursive version
def preorder(root:TreeNode):
    result = []
    current = root
    
    def helper(current:TreeNode):
        #base condition
        if current == None:
            return
        result.append(current.val) # visit(root)
        helper(current.left) # traverse left
        helper(current.right) # traverse right
        return
    helper(current)
    return result

def inorder(root:TreeNode):
    result = []
    current = root
    
    def helper(current:TreeNode):
        #base condition
        if current == None:
            return
        
        helper(current.left) # traverse left
        result.append(current.val) # visit(root)
        helper(current.right) # traverse right
        return
    helper(current)
    return result

def postorder(root: TreeNode):
    result = []
    current = root
    
    def helper(current:TreeNode):
        #base condition
        if current == None:
            return
        
        helper(current.left) # traverse left
        helper(current.right) # traverse right
        result.append(current.val) # visit(root)
        return
    helper(current)
    return result

def level_order(root:TreeNode):
    if root == None:
        return

    result = []
    queue = deque([root])

    while queue:
        current = q.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(7)
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

