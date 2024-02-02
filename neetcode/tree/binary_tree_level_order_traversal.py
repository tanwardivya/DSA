from typing import List
from typing import Any
from collections import deque
class TreeNode:
    def __init__(self,val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def level_order_traversal(self,root:TreeNode)->List[List[int]]:
        res = []# for storing the final list
        if root is None: # for case 3 when root = []
            return res
        queue = deque() #initialization of a queue
        queue.append(root) # appending the root value in queue

        while queue: # run the bfs while our queue is not empty, keep running the while loop until there are no nodes left in our queue
            queuelen = len(queue) # since the queue is not empty we get the length of queue so we get the nodes or values in the queue currently and we going to loop through every single one of those values this queue length is basically ensuring that we iterate through one level at a time 
            level = [] # and from that level we add those elements of the tree according to level in its own list and at last add this list to the result list
            for i in range(queuelen): # looping through every single value in the queue currently
                node = queue.popleft() # pop nodes from the left of the queue in fifo process
                if node: # check if the node is null
                    level.append(node.val) #if its is not null append the node value to level list append the children of this node
                    queue.append(node.left) # append the left child of this node to the queue
                    queue.append(node.right) #append the right child 
            if level: # make sure the level is non empty, because we know technically our queue could have null nodes so we're not adding them to the level list
                res.append(level)  
        return res

def main():
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    solution = Solution()
    result = solution.level_order_traversal(node)
    print(result)


    node = TreeNode(1)
    solution = Solution()
    result = solution.level_order_traversal(node)
    print(result)

    node = None
    solution = Solution()
    result = solution.level_order_traversal(node)
    print(result)

if __name__ == "__main__":
    main()
