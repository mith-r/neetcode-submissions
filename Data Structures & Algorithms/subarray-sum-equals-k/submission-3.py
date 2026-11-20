class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #perhaps have a running sum if you go left to right
        #and store number of ways to get to k if you subtract by something
        #so at any point, if thats in the hashmap, thats the amount of ways to do it

        curr = 0
        table = {0:1}

        count = 0

        for i in nums:
            curr += i
            remaining = curr-k

            if remaining in table:
                count += table[remaining]
            
            #now the pre part

            if curr not in table:
                table[curr] = 0
            table[curr] += 1
        
        return count



            
            
                




        