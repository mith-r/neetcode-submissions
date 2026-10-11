class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = deque()

        for i in s:
            if len(stack) == 0:
                stack.append((i,1))
            else:
                lastLetter, lastCount = stack[-1]

                if lastLetter == i:
                    stack.pop()

                    if lastCount + 1 != k:
                        stack.append((i,lastCount+1))
                
                else:
                    stack.append((i,1))

        res = ""
        for (x,y) in stack:
            for i in range(y):
                res += x

        return res

        