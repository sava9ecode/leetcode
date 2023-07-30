class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum([nums[i] for i in range(k)])
        ans = curr
        for i in range(len(nums) - k):
            curr = curr - nums[i] + nums[i + k]
            ans = max(ans, curr)
        return ans / k
