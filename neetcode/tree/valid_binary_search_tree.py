from typing import Any
class TreeNode:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def is_valid_binary_search_tree(self, root:TreeNode):
        def valid_BST(root:TreeNode, minval,maxval):
            if root is None:
                return True
            if not minval < root.val < maxval:
                return False

            return valid_BST(root.left, minval, root.val) and valid_BST(root.right,root.val,maxval)
        return valid_BST(root, float('-inf'), float('+inf'))

def main():
    nd = TreeNode(5)
    nd.left = TreeNode(4)
    nd.right = TreeNode(6)
    nd.right.left = TreeNode(3)
    nd.right.right = TreeNode(7)
    solution = Solution()
    result = solution.is_valid_binary_search_tree(nd)
    print("is_valid_binary_search_tree:", result)

if __name__ == "__main__":
    main()
