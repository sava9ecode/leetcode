# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.findLeaf(root1) == self.findLeaf(root2)

    def findLeaf(self, root):
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        return self.findLeaf(root.left) + self.findLeaf(root.right)
