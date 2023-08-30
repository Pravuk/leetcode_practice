from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        match = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in match:
                stack.append(char)
            elif len(stack) == 0 or match[stack[-1]] != char:
                return False
            else:
                stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("(){}[{()}]"))
    pass
