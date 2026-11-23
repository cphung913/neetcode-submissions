class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = [0] * 26
        s1_chars = [0] * 26
        for s in s1:
            s1_chars[ord(s) - ord('a')] += 1
        for i in range(len(s2) - len(s1) + 1):
            for j in range(len(s1)):
                chars[ord(s2[i+j]) - ord('a')] += 1
            if chars == s1_chars: return True
            chars = [0] * 26
        return False