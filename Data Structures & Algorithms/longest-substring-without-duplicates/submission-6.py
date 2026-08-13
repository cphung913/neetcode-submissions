class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, biggest = 0, 0, 0
        if len(s) <= 1:
            return len(s)
        while r < len(s):
            current = s[r]
            if current in s[l:r]:
                biggest = max(r-l, biggest)
                l += 1
            else:
                r += 1
        biggest = max(r-l, biggest)
        return biggest
            