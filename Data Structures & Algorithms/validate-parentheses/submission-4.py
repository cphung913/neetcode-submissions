class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for x in s:
            if x in '({[':
                stack.append(x)
            else:
                if not stack:
                    return False
                y = stack.pop()
                if y == '[' and x != ']':
                    return False
                elif y == '{' and x != '}':
                    return False
                elif y == '(' and x != ')':
                    return False
        return len(stack) == 0
