class Solution:
    def trap(self, height: List[int]) -> int:
        max_levels = [0] * len(height)
        current_level = 0
        total = 0
        
        for i in range(len(height)):
            current_level = max(current_level, height[i])
            max_levels[i] = current_level
        
        current_level = 0
        
        for i in range(len(height)-1, -1, -1):
            current_level = max(height[i], current_level)
            total += min(max_levels[i], current_level) - height[i]

        return total
