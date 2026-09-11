class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        current = 0
        nums_set = set(nums)
        for x in nums_set:
            if x - 1 not in nums_set:
                current = 1
                while True:
                    if x + current in nums_set:
                        current += 1
                    else:
                        break
                longest = max(longest, current)
                current = 0
        return longest
                




