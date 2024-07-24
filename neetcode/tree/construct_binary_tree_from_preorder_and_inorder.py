from typing import Any
from typing import List
from collections import deque
class TreeNode:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        if self == None:
            return

        result = []
        queue = deque([self])

        while queue:
            current = queue.popleft()
            result.append(str(current.val))
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return ','.join(result)



class Solution:
    def construct_tree(self, preorder:List[int],inorder:List[int])->TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.construct_tree(preorder[1 : mid + 1],inorder[:mid])
        root.right = self.construct_tree(preorder[mid + 1 :],inorder[mid + 1:])
        return root

def main():
    
    solution = Solution()
    preorder=[3,9,20,15,7]
    inorder = [9,3,15,20,7]
    result_tree = solution.construct_tree(preorder,inorder)
    print("Level traversal of constructed tree:", result_tree)

if __name__ == "__main__":
    main()
