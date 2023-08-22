# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            if node:
                if node.val >= curr_max:
                    result[0] += 1
                    curr_max = node.val
                dfs(node.left, curr_max)
                dfs(node.right, curr_max)

        result = [0]
        dfs(root, root.val)
        return result[0]
