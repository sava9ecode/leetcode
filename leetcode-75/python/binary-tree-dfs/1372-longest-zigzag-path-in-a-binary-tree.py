# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root.left, True, 0), self.helper(root.right, False, 0))

    def helper(self, node, is_left, depth):
        if not node:
            return depth

        if is_left:
            depth = max(
                self.helper(node.right, False, depth + 1),
                self.helper(node.left, True, 0),
            )
        else:
            depth = max(
                self.helper(node.left, True, depth + 1),
                self.helper(node.right, False, 0),
            )

        return depth
