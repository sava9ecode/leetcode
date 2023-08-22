# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        self.cache = {0: 1}
        self.dfs(root, targetSum, 0, cache)
        return self.result

    def dfs(self, root, target, curr_path_sum, cache):
        if not root:
            return None

        curr_path_sum += root.val
        old_path_sum = curr_path_sum - target
        self.result += self.cache.get(old_path_sum, 0)
        self.cache[curr_path_sum] = self.cache.get(curr_path_sum, 0) + 1

        self.dfs(root.left, target, curr_path_sum, cache)
        self.dfs(root.right, target, curr_path_sum, cache)

        self.cache[curr_path_sum] -= 1
