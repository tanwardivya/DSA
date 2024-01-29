from typing import Any, Optional
class TreeNode:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        current1 = p
        current2 = q
        def helper(current1: TreeNode, current2:TreeNode) -> bool:
            if not current1 and not current2:
                return True
            if not current1 or not current2 or current1.val != current2.val:
                return False
          
            return helper(current1.left, current2.left) and helper(current1.right,current2.right)
        
        return helper(current1,current2)

def main():
    solution = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    result = solution.isSameTree(root1,root2)
    print(result)

if __name__ == '__main__':
    main()
