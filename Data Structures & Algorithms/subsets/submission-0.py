class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtrack(start, comb, size):
            if len(comb) == size:
                out.append(comb)
            for i in range(start, len(nums)):
                backtrack(i+1, comb + [nums[i]], size)

        for n in range(len(nums)+1):
            backtrack(0, [], n)
        return out
