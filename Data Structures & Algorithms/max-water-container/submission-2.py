class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l, r = 0, len(heights) - 1
        while r > l:
            most = max(most, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return most