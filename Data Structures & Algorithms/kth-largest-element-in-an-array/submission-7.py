class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        res = []
        
        for i in nums[:k]:
            heapq.heappush(res,i)
    
   

        for i in nums[k:]:
            if i > res[0]:
                heapq.heapreplace(res,i)

      
        
        return heapq.heappop(res)

        