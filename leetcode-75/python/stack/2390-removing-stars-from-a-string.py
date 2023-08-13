class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
                continue
            stack.append(char)

        return "".join(stack)
