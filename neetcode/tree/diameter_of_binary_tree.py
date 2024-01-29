from typing import Any, Optional
class TreeNode:
    def __init__(self, val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root:Optional[TreeNode]) -> int:
        result = 0

        def dfs(root):
            nonlocal result

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            result = max(result, left + right)

            return 1 + max(left,right)

        dfs(root)
        return result





def main():
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(5)
    node.left.left = TreeNode(3)
    node.left.right = TreeNode(4)
    node.left.left.left  = TreeNode(9)
    node.left.right.left = TreeNode(10)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(7)
    solution = Solution()
    finaldiameter = solution.diameterOfBinaryTree(node)
    print("resulted_diameter:", finaldiameter)

if __name__ == "__main__":
    main()



