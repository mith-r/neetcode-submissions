class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        queue = []
        passengers = 0
        for trip in trips:
            queue.append((trip[1],trip[0]))
            queue.append((trip[2],-trip[0]))

        queue = sorted(queue, key = lambda x:x[0])
        
        for item in queue:
            passengers += item[1]
            if passengers > capacity:
                return False
        
        return True
        



  


        