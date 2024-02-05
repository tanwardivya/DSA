from typing import Any
class TreeNode:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kth_smallest_element(self, root:TreeNode, k):
        
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
        return result[k-1]