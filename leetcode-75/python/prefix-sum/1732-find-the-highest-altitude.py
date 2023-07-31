class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res, prefix = 0, 0
        for i in gain:
            prefix += i
            res = max(res, prefix)
        return res
