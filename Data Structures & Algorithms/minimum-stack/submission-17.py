class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = float('inf')

        

    def push(self, val: int) -> None:
        self.curr_min = min(self.curr_min,val)
        self.stack.append((val,self.curr_min))
        

    def pop(self) -> None:
        del self.stack[-1]

        if (len(self.stack)) > 0:
            self.curr_min = self.stack[-1][1]
        else:
            self.curr_min = float('inf')
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
