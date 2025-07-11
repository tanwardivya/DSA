from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_binary_tree_iterative_dfs(self, root:Optional[TreeNode])->Optional[TreeNode]:
        if not root: return None
        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
    
    def preorder(self, root:TreeNode):
        if not root: return

        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    
def main():
    tn = TreeNode(1)
    tn.left = TreeNode(2)
    tn.right = TreeNode(3)
    tn.left.left = TreeNode(4)
    tn.left.right = TreeNode(5)
    tn.right.left = TreeNode(6)
    tn.right.right = TreeNode(7)
    solution = Solution()
    
    original_tree = solution.preorder(tn)
    print("original_tree(Preorder Traversal)",original_tree)

    inverted_tree = solution.invert_binary_tree_iterative_dfs(tn)
    print("Inverted Tree (Preorder Traversal):",inverted_tree)
    
    result = solution.preorder(inverted_tree)
    print(result)

  

if __name__ == "__main__":
    main()


    