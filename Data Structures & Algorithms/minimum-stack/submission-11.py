class MinStack:

    def __init__(self):
        self.stack = []
        self.mindict = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min:
            self.min = val
        self.mindict.append(self.min)

        

    def pop(self) -> None:
        self.stack.pop()
        self.mindict.pop()
        if len(self.mindict) > 0:
            self.min = self.mindict[-1]
        else:
            self.min = float('inf')
        print()

        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mindict[-1]


        
