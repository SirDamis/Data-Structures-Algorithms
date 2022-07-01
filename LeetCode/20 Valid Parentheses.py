class Solution:
    def isValid(self, s: str) -> bool:
        char = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for val in s:
            if val in char:
                stack.append(val)
            elif len(stack) == 0 or char[stack.pop()] != val:
                return False
        return len(stack) == 0

