class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"{":"}", "(":")", "[": "]"}
        for c in s:
            if c in ["{","(","["]:
                stack.append(c)
            elif len(stack) > 0 and match[stack[-1]] == c:
                stack.pop()
            else:
                return False
        return len(stack) == 0

