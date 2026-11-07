class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        buckets = [[] for i in range(len(nums)+1)]

        for key,value in count.items():
            buckets[value].append(key)

        res = []
        for i in range(len(buckets)-1,-1,-1):
            res.extend(buckets[i])

            if len(res) == k:
                return res


        

       



        