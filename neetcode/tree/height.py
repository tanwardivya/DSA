from typing import Any
class TreeNode:
    def __init__(self, val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def max_height(self, root:TreeNode) -> int:
    
        if not root:
            return 0

        left = self.max_height(root.left)
        right = self.max_height(root.right)

        return 1 + max(left,right)

        
def main():
    tn = TreeNode(3)
    tn.left = TreeNode(9)
    tn.right = TreeNode(20)
    tn.right.left = TreeNode(15)
    tn.right.right = TreeNode(7)
    
    solution = Solution()
    result = solution.max_height(tn)
    print("Max_height:", result)

if __name__ == "__main__":
    main()