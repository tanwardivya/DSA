from typing import Any
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def right_side_view(self, root: TreeNode)-> List[int]:
        res = []
        
        if root == None:
            return res

        queue = deque([root])
        
        while queue:
            right_side = None # initially take right side equal to none
            queuelen = len(queue)

            for i in range(queuelen):
                node = queue.popleft()
                if node:
                    right_side = node # node could be null so check if it is not 
                    #null then update the right side to that node. because after 
                    # executing the entire loop we can see the right side of tree 
                    # has is the last node that is inside the current level of the 
                    # queue ie queuelen
                    queue.append(node.left)
                    queue.append(node.right)

            if right_side:
                res.append(right_side.val)
        return res

def main():
    nd = TreeNode(1)
    nd.left = TreeNode(2)
    nd.right = TreeNode(3)
    nd.left.right = TreeNode(5)
    nd.right.right = TreeNode(4)
    solution = Solution()
    result = solution.right_side_view(nd)
    print(result)

    nd = TreeNode(1)
    nd.right = TreeNode(3)
    solution = Solution()
    result = solution.right_side_view(nd)
    print(result)

    nd = None
    solution = Solution()
    result = solution.right_side_view(nd)
    print(result)

if __name__ == "__main__":
    main()
