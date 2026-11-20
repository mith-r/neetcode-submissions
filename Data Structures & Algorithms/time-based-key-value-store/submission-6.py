class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
      
        if key not in self.timemap:
            return ""
        
        vals = self.timemap[key]

        low = 0
        high = len(vals)-1

        best = -1

        while low <= high:

            center = low + (high-low)//2

            if vals[center][0] > timestamp:
                high = center - 1
            
            else:
                best = center
                low = center + 1
        
        if best == -1:
            return ""

        return vals[best][1]


        
