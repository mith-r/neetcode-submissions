class MinStack:

    def __init__(self):
        self.stack = deque()
        self.curr_min = float("inf")
        

    def push(self, val: int) -> None:
        self.curr_min = min(val,self.curr_min)
        self.stack.append((val,self.curr_min))
        

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) > 0:
            self.curr_min = self.stack[-1][1]
        else:
            self.curr_min = float("inf")

    def top(self) -> int:
        return self.stack[-1][0]

        

    def getMin(self) -> int:
        
        return self.stack[-1][1]

        
