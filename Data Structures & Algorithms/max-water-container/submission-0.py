class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first, last = 0, len(heights) - 1
        max_area = 0
        while first < last:
            area = min(heights[first], heights[last]) * (last - first)
            max_area = max(max_area, area)
            if heights[first] > heights[last]:
                last -= 1
            else:
                first += 1
        return max_area