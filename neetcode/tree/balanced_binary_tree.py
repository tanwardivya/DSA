from typing import Any
class TreeNode:
    def __init__(self, val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def max_height(self,node: TreeNode) -> int:
    
        if not node:
            return 0

        left = self.max_height(node.left)
        right = self.max_height(node.right)

        return 1 + max(left,right)

    def balanced_binary_tree(self,root:TreeNode) -> bool:

        if not root:
            return True
        
        left_subtree_height = self.max_height(root.left)
        right_subtree_height = self.max_height(root.right)
       
        if abs(left_subtree_height - right_subtree_height) > 1:
            return False
        
        return self.balanced_binary_tree(root.left) and self.balanced_binary_tree(root.right)

def main():
    tn = TreeNode(3)
    tn.left = TreeNode(9)
    tn.right = TreeNode(20)
    tn.right.left = TreeNode(15)
    tn.right.right = TreeNode(7)
    solution = Solution()
    result = solution.balanced_binary_tree(tn)
    print(result)

if __name__ == "__main__":
    main()
