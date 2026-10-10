class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = {}
        prefixSum[0] = 1

        currSum = 0
        count = 0

        for num in nums:
            currSum += num

            if (currSum-k) in prefixSum:
                count += prefixSum[currSum-k]
            

            if currSum not in prefixSum:
                prefixSum[currSum] = 0
            prefixSum[currSum] += 1

        return count