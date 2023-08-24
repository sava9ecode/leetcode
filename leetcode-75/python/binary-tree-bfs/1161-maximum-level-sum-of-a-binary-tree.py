# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        q = deque([root])
        cntLvl, maxLvl = 1, 1
        maxSum = float("-inf")

        while q:
            currSum = 0
            for _ in range(len(q)):
                node = q.pop()
                currSum += node.val
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)

            maxLvl = cntLvl if currSum > maxSum else maxLvl
            maxSum = max(maxSum, currSum)
            cntLvl += 1

        return maxLvl
