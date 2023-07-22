class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for n in nums:
            if n > second:
                return True
            elif n <= first:
                first = n
            else:
                second = n
        return False
