# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


# 1st solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q, cnt = deque([root]), 0
        while q:
            flag = False
            for _ in range(len(q)):
                node = q.pop()
                if node:
                    flag = True
                    q.appendleft(node.left)
                    q.appendleft(node.right)
            if flag:
                cnt += 1
        return cnt


# 2nd solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return (
            1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
        )
