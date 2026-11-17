class MedianFinder:

    def __init__(self):

        #initialzing two heaps, one for lower_half (max) and one for upper_half (min)
        self.upper_min = []
        self.lower_max = []
        

    def addNum(self, num: int) -> None:
        #if both are empty, add to min heap by default
        if len(self.upper_min) == len(self.lower_max) == 0:
            heapq.heappush(self.upper_min,num)
        
        #if num is greater than median, push to min_heap
        elif num > self.findMedian():
            heapq.heappush(self.upper_min,num)
        #else push to max_heap
        else:
            heapq.heappush_max(self.lower_max,num)

        #if they are unbalanced, rotate
        if len(self.upper_min) > len(self.lower_max) + 1:
            heapq.heappush_max(self.lower_max,heapq.heappop(self.upper_min))
        
        if len(self.lower_max) > len(self.upper_min) + 1:
            heapq.heappush(self.upper_min,heapq.heappop_max(self.lower_max))
        

    def findMedian(self) -> float:
        #if equal return mean
        if len(self.upper_min) == len(self.lower_max):
           return (self.upper_min[0] + self.lower_max[0])/2
        
        #if uneven return greater
        if len(self.upper_min) > len(self.lower_max):
            return self.upper_min[0]
        
        if len(self.upper_min) < len(self.lower_max):
            return self.lower_max[0]


        
        