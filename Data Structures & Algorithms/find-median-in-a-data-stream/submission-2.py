class MedianFinder:

    def __init__(self):
        self.lowermax = []
        self.uppermin = []
        

    def addNum(self, num: int) -> None:
        if len(self.lowermax) == 0 and len(self.uppermin) == 0:
            heapq.heappush(self.uppermin, num)
            return
        
        if num > self.findMedian():
            heapq.heappush(self.uppermin,num)
        else:
            heapq.heappush_max(self.lowermax,num)
        
        if len(self.lowermax) - 1 > len(self.uppermin):
            heapq.heappush(self.uppermin,heapq.heappop_max(self.lowermax))
        
        if len(self.uppermin) - 1 > len(self.lowermax):
            heapq.heappush_max(self.lowermax, heapq.heappop(self.uppermin))
        

    def findMedian(self) -> float:

        if len(self.lowermax) > len(self.uppermin):
            return self.lowermax[0]

        if len(self.lowermax) < len(self.uppermin):
            return self.uppermin[0]
        
        return (self.lowermax[0] + self.uppermin[0])/2
        

        
        