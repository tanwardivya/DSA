from collections import deque
from typing import Any
class TreeNode:
    def __init__(self, val:Any):
        self.val = val
        self.left = None
        self.right = None

# #Recursive DFS
# class MaxDepth:
#     def max_depth(self,root:TreeNode)->int:
#         if not root:
#             return 0

#         return 1 + max(self.max_depth(root.left),self.max_depth(root.right))

#BFS 
class MaxDepth:
    def max_depth(self, root:TreeNode)->int:
        if not root:
            return 0

        level = 0
        q = deque([root])# initializing the queue witha single value that is the root value
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level


    # def preorder(self,root:TreeNode):
    #     result = []
    #     current = root

    #     def helper(current:TreeNode):
    #         if current == None:
    #             return
            
    #         result.append(current.val)
    #         helper(current.left)
    #         helper(current.right)
    #         return
    #     helper(current)
    #     return result

def main():
    tn = TreeNode(3)# instance of TreeNode class
    tn.left = TreeNode(9)
    tn.right = TreeNode(20)
    tn.right.left = TreeNode(15)
    tn.right.right = TreeNode(7)
    md = MaxDepth()#instance of MaxDepth class
    depth = md.max_depth(tn)#
    print(depth)
    # final_result = md.preorder(tn)
    # print(final_result)

if __name__ == "__main__":
    main()





            




    