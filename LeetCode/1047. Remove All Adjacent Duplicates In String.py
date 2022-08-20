class Solution:
    def removeDuplicates(self, s: str) -> str:
        # TC: O(N) SC: O(N)
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)


