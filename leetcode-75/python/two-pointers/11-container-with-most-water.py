class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area, h = 0, max(height)

        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            if (r - l) * h <= area:
                break

        return area
