class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, out = [1]*len(nums), [0]*len(nums), []
        suffix[len(nums)-1] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            out.append(suffix[i] * prefix[i])
        return out
        