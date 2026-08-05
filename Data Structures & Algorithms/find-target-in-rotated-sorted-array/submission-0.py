class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        while first <= last:
            i = (first + last) // 2
            if nums[i] == target:
                return i
            if nums[first] <= nums[i]:
                if nums[first] <= target < nums[i]:
                    last = i - 1
                else:
                    first = i + 1
            else:
                if nums[i] < target <= nums[last]:
                    first = i + 1
                else:
                    last = i - 1
        return -1