class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            target_term = target - nums[i]
            if target_term in hash_map:
                return [hash_map[target_term], i]
            hash_map[nums[i]] = i