class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        time = 1
        
        timeheap = []
        res = []

        for i in range(len(tasks)):
            heapq.heappush(timeheap,(tasks[i][0],tasks[i][1],i))

        available = []

        while len(timeheap) > 0:

            while len(timeheap) > 0 and timeheap[0][0] <= time:
                heapq.heappush(available,(timeheap[0][1],timeheap[0][2]))
                heapq.heappop(timeheap)
            
            if len(available) > 0:
                recent = heapq.heappop(available)
           
                res.append(recent[1])
                time += recent[0]
            else:
                time = timeheap[0][0]
        
        while len(available) > 0:
       
            res.append(heapq.heappop(available)[1])
        
        return res
        