from typing import Any
class TreeNode:
    def __init__(self, val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def max_path_sum(self, root:TreeNode)->int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)
            leftmax = max(left_max,0)
            right_max = max(right_max, 0)

            res[0] = max(res[0], root.val + left_max +right_max)
            return root.val + max(left_max,right_max)

        dfs(root)
        return res[0]

def main():
    nd = TreeNode(-10)
    nd.left = TreeNode(9)
    nd.right = TreeNode(20)
    nd.right.left = TreeNode(15)
    nd.right.right = TreeNode(7)
    solution = Solution()
    result = solution.max_path_sum(nd)
    print(result)

    nd = TreeNode(1)
    nd.left = TreeNode(2)
    nd.right = TreeNode(3)
    solution = Solution()
    result = solution.max_path_sum(nd)
    print(result)

if __name__ == "__main__":
    main()