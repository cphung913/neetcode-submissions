class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_n = sorted(nums)
        res = []
        for i, val in enumerate(sort_n):
            if i > 0 and val == sort_n[i-1]:
                continue
            j = i + 1
            k = len(sort_n) - 1
            while j < k:
                calc = val + sort_n[j] + sort_n[k]
                if calc < 0:
                    j += 1
                elif calc > 0:
                    k -= 1
                else:
                    res.append([val, sort_n[j], sort_n[k]])
                    j += 1
                    while j < k and sort_n[j] == sort_n[j-1]:
                        j += 1
        return res