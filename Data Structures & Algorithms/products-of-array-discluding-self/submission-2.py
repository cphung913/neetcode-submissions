class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        before = [1] * length
        after = [1] * length

        for i in range(1, length):
            before[i] = before[i-1] * nums[i-1]
            after[length-i-1] = after[length-i] * nums[length-i]
        return [before[i]*after[i] for i in range(length)]
