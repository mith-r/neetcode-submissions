class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        i = 0
        curr_max = 0
        num_flips = 0

        length = 0

        for j in range(len(nums)):
            length += 1
            
            if nums[j] == 0:

                num_flips += 1
        

                while num_flips > k:

                    if nums[i] == 0:
                        num_flips -= 1

                    i += 1
                    length -= 1
                
   

            curr_max = max(curr_max,length)
         

        return curr_max


