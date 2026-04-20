class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operations[i]))
        
        sum = 0
        while not len(stack) == 0:
            sum += stack.pop()
        
        return sum

            