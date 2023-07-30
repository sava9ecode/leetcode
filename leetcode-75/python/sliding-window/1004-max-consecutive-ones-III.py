class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return r - i + 1
