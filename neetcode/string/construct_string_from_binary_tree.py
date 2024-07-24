from typing import Optional
class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def tree_to_string(self, root: Optional[TreeNode])-> str:
        res = [] 

        def preorder(root):
            if not root:
                return
            
            res.append("(")
            res.append(str(root.val))

            if not root.left and root.right:
                res.append("()")

            preorder(root.left)
            preorder(root.right)
            res.append(")")

        preorder(root)
        return "".join(res)[1:-1]

def main():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)

    answer = solution.tree_to_string(root)
    print(answer)

if __name__ == "__main__":
    main()

