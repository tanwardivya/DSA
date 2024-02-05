from typing import Any
class TreeNode:
    def __init__(self, val:Any):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self,data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dsf()

def main():
    nd = TreeNode(1)
    nd.left = TreeNode(2)
    nd.right = TreeNode(3)
    nd.right.left = TreeNode(4)
    nd.right.right = TreeNode(5)
    solution = Solution()
    result = solution.serialize(nd)
    print(result)
    final_tree = result
    print(final_tree)

if __name__ == "__main__":
    main()