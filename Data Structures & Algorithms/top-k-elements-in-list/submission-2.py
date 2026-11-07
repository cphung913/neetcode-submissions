class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        ordered = sorted(count.items(), key=lambda x: -x[1])
        out = []

        for i in range(k):
            out.append(ordered[i][0])

        return out