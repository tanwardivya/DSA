from typing import List, Optional

class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def inorder_traversal(self, root:Optional[TreeNode])-> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res
    
def main():
    # Example usage
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution = Solution()
    result = solution.inorder_traversal(root)
    print("Inorder Traversal:", result)

if __name__ == "__main__":
    main()