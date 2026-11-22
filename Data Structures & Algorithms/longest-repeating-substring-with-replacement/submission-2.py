class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len = 0
        count = defaultdict(int)
        current = s[0]
        
        while r < len(s):
            count[s[r]] += 1
            if count[s[r]] > count[current]:
                current = s[r]
            if r + 1 - l - count[current] > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
            