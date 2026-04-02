class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            new_list = nums[:]
            new_list.pop(i)
            if num in new_list:
                return True
        return False
