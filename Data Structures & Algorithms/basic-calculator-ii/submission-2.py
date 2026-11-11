class Solution:
    def calculate(self, s: str) -> int:
        
        stack = deque()
        operations = ["*","-","+","/"]

        for i in range(len(s)):

            if s[i] in operations or len(stack) == 0:
                nextStr = ""
                j = i

                if i != 0:
                    j += 1
                
                while j < len(s) and s[j] not in operations:
                    nextStr += s[j]
                    j += 1

                curr = int(nextStr)
                if i == 0:
                    stack.append(curr)
            

            if s[i] == "*":
                prev = stack.pop()
                stack.append(curr*prev)

            if s[i] == "/":
                prev = stack.pop()
                stack.append(int(prev/curr))
            
            if s[i] == "+":
                stack.append(curr)

            if s[i] == "-":
                stack.append(curr * -1)

        return sum(list(stack))



            