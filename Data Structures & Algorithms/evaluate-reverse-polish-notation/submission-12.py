class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = deque()

        for i in tokens:

            if i not in ["+","-","/","*"]:
                stack.append(int(i))
            else:
                second = stack.pop()
                first = stack.pop()

                if i == "+":
                    stack.append(first+second)
                if i == "-":
                    stack.append(first-second)
                if i == "*":
                    stack.append(first*second)
                if i == "/":
                    stack.append(int(first/second))
        
        return stack.pop()
