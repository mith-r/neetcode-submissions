class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        #a subarray nums[j..i] is divisible by k iff prefix[i] == prefix[j] (mod k)

        #so we create an array of len(k) and then store everything that results in that divisor there
        #and then later when we get something that is that divisor we can add those to it

        remainders = [0] * k
        remainders[0] = 1
        count = 0

        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k
            print(remainder)

            count += remainders[remainder]

            remainders[remainder] += 1
        
        return count