class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, cnt, i = 0, 0, 0
        for j, num in enumerate(nums):
            cnt += num
            if cnt < (j - i):
                cnt -= nums[i]
                i += 1
            ans = max(ans, j - i)
        return ans
