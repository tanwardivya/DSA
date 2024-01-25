from typing import Any
class TreeNode:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invert_tree(self,root:TreeNode)->TreeNode:
        if not root:
            return None

        #swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root


    def preorder(self, root:TreeNode):
        result = []
        current = root
        
        def helper(current:TreeNode):
            #base condition
            if current == None:
                return
            result.append(current.val) # visit(root)
            helper(current.left) # traverse left
            helper(current.right) # traverse right
            return
        helper(current)
        return result

def main():
    tn = TreeNode(4)
    #input = [4,2,7,1,3,6,9]
    tn.left = TreeNode(2)
    tn.right = TreeNode(7)
    tn.left.left = TreeNode(1)
    tn.left.right = TreeNode(3)
    tn.right.left = TreeNode(6)
    tn.right.right = TreeNode(9)
    solution = Solution()
    inverted_tree = solution.invert_tree(tn)
    result = solution.preorder(inverted_tree)
    print("inverted_binary_tree:", result)

if __name__ == "__main__":
    main()
