from typing import Any
class TreeNode:
    def __init__(self, val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def count_good_nodes(self, root: TreeNode)-> int:
        def dfs(node, max_val):
            if not node:
                return 0

            res = 1 if node.val >= max_val else 0
            max_val = max(max_val,node.val)
            res += dfs(node.left, max_val)
            res += dfs(node.right,max_val)
            return res
        return dfs(root, root.val)

def main():
    nd =  TreeNode(3)
    nd.left = TreeNode(1)
    nd.right = TreeNode(4)
    nd.left.left = TreeNode(3)
    nd.right.left = TreeNode(1)
    nd.right.right = TreeNode(5)
    solution = Solution()
    result = solution.count_good_nodes(nd)
    print("Total_count_good_nodes:", result)

    nd =  TreeNode(3)
    nd.left = TreeNode(3)
    nd.left.left = TreeNode(4)
    nd.left.right = TreeNode(2)
    solution = Solution()
    result = solution.count_good_nodes(nd)
    print("Total_count_good_nodes:", result)

    nd =  TreeNode(3)
    solution = Solution()
    result = solution.count_good_nodes(nd)
    print("Total_count_good_nodes:", result)


if __name__ == "__main__":
    main()
