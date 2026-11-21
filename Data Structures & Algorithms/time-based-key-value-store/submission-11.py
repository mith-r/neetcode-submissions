class TimeMap:

    def __init__(self):
        self.time = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        
        self.time[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time:
            return ""
        
        values = self.time[key]

        low = 0
        high = len(values)


        best = -1

        while low < high:

            

            mid = low + (high-low)//2

           

            if values[mid][0] <= timestamp:
                best = mid
                low = mid + 1
            
            else:
                high = mid
      
        return values[best][1] if best != -1 else ""
        
