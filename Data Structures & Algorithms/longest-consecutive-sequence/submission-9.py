class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        longest = 0
        start = 0
        end = 0
        while end < len(nums):
            if nums[end] != nums[end-1] + 1:
                longest = max(longest, end-start)
                start = end
            end += 1
        longest = max(longest, end-start)
        return longest
            