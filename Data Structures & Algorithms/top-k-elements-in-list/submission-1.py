class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        counts = sorted(list(count.items()), key=lambda x: x[1])
        out = []
        for i in range(k):
            out.append(counts[-i-1][0])
        return out