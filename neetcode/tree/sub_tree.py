from typing import Any, Optional
class TreeNode:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None

def is_same_tree(p:TreeNode, q:TreeNode) -> bool:
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def is_subtree(root: TreeNode, subtree: TreeNode):
    if is_same_tree(root,subtree):
        return True
    if not root or not subtree:
        return False
    return is_subtree(root.left, subtree) or is_subtree(root.right,subtree)

def main():
    node = TreeNode(3)
    node.left = TreeNode(4)
    node.right = TreeNode(5)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(2)

    node_subtree = TreeNode(4)
    node_subtree.left = TreeNode(1)
    node_subtree.right = TreeNode(2)

    result = is_subtree(node, node_subtree)
    print("is subtree of another subtree:", result)

if __name__ == "__main__":
    main()


