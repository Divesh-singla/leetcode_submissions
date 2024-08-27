class Solution:
    def removeStars(self, s: str) -> str:
        from collections import deque
        stack = deque()

        for x in s:
            if x=="*":
                stack.pop()
            else:
                stack.append(x)

        return ("".join(stack))