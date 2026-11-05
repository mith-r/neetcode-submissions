class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        for i in s:
            if i in {'(','{','['}:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                curr = stack.pop()

                if curr == '(' and i!= ')':
                    return False
                if curr == '{' and i != '}':
                    return False
                if curr == '[' and i != ']':
                    return False

        return len(stack) == 0        