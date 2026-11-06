class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        out = [intervals[0]]
        for l, r in intervals[1:]:
            if l <= out[-1][1]:
                out[-1][1] = max(r, out[-1][1])
            else:
                out.append([l, r])
        return out
