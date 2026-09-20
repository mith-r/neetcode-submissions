class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 0
            res[num] += 1
        
        res_sort = sorted(res, key = res.get, reverse=True)
        return res_sort[:k]