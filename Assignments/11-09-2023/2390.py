class Solution:
    def removeStars(self, string: str) -> str:
        stack = []
        for i in string:
            if i == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "".join(stack)