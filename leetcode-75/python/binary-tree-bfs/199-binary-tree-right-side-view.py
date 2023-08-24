# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None

        result = []
        q = deque([root])

        while q:
            curr_len = len(q)
            for i in range(curr_len):
                node = q.pop()
                if i == curr_len - 1:
                    result.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
        return result
