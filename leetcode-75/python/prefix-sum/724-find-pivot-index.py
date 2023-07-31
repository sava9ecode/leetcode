class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum, rightsum = 0, sum(nums)
        for i, n in enumerate(nums):
            rightsum -= n
            if leftsum == rightsum:
                return i
            leftsum += n
        return -1
