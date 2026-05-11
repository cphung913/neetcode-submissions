class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+ 1)]
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for key, v in hashmap.items():
            freq[v].append(key)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for f in freq[i]:
                result.append(f)
                if len(result) == k:
                    return result