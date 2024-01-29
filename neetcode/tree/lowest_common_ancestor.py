class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowest_ancestor_of_binary_search_tree(self, root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
        current = root

        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current

def main():
    node = TreeNode(6)
    node.left = TreeNode(2)
    node.right = TreeNode(8)
    node.left.left = TreeNode(0)
    node.left.right = TreeNode(4)
    node.right.left = TreeNode(7)
    node.right.right = TreeNode(9)
    node.left.right.left = TreeNode(3)
    node.left.right.right = TreeNode(5)
    solution = Solution()
    p = node.left
    q = node.right
    result = solution.lowest_ancestor_of_binary_search_tree(node, p, q)
    if result:
        print("lowest_ancestor_of_binary_search_tree:", result.val)
    else:
        print("lowest_ancestor_of_binary_search_tree not found")

    node = TreeNode(3)
    node.left = TreeNode(1)
    node.right = TreeNode(8)
    node.right.left = TreeNode(5)
    node.right.right = TreeNode(10)
    node.right.left.left = TreeNode(4)
    node.right.left.right = TreeNode(6)
    node.right.right.left = TreeNode(9)
    node.right.right.right = TreeNode(11)
    p = node.right.right.left
    q = node.right.right.right
    result = solution.lowest_ancestor_of_binary_search_tree(node, p, q)
    if result:
        print("lowest_ancestor_of_binary_search_tree:", result.val)
    else:
        print("lowest_ancestor_of_binary_search_tree not found")

if __name__ == "__main__":
    main()


