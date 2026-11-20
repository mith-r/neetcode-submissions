class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #use minheap of distance, x, y coordinates
        #to save space could use maxheap and pop biggest to make sure size is k

        heap = []

        for point in points:

            x = point[0]
            y = point[1]

            distance = math.sqrt(x**2 + y**2)
            
            heapq.heappush_max(heap,[distance,x,y])

            if len(heap) > k:
                heapq.heappop_max(heap)
        
        res = []

        for point in heap:
            res.append(point[1:])
        
        return res

