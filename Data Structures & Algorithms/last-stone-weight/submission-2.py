class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            print(x)
            print(y)

            if x < y:
                y = y-x
                heapq.heappush_max(stones,y)
            elif y<x:
                x = x-y
                heapq.heappush_max(stones,x)
            print(stones)
            print()
        
        return stones[0] if len(stones) == 1 else 0
        