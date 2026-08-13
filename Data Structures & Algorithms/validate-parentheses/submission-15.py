class Solution:
    def isValid(self, s: str) -> bool:
        match = {"]": "[", ")": "(", "}": "{"}
        stack = []
        for c in s:
            if c in match:
                if not stack:
                    return False
                last = stack.pop()
                if match[c] != last:
                    return False
            else:
                stack.append(c)
        return bool(not stack) 