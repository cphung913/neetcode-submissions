class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                out.append(comb)
                return
            for i in range(start, n+1):
                backtrack(i+1, comb + [i])

        backtrack(1, [])
        return out