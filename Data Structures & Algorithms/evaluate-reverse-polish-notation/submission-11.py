class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()

        for i in tokens:
            if i in ["+","-","*","/"]:
                right = int(stack.pop())
                left = int(stack.pop())

                if i == "+":
                    left += right
                if i == "-":
                    left -= right
                if i == "*":
                    left = right * left
                if i == "/":
                    left = int(left/right)
                
                stack.append(left)
            else:
                stack.append(i)
            
        
        return int(stack[-1])
        