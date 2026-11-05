class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            seen = set()
            dups = set()
            for j in range(i+1, len(nums)):
                wanted = target - nums[j]
                if wanted in seen and wanted not in dups:
                    out.append([nums[i], wanted, nums[j]]) 
                    dups.add(wanted)
                seen.add(nums[j])
        return out
