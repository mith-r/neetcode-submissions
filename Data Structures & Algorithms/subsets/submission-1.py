class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total=[]
        curr = []

        def subset(i):

            if i == len(nums):
                total.append(curr.copy())
                return
            
            #version where we don't include i
           

            #version where we include i
            curr.append(nums[i])
            subset(i+1)

            curr.pop()
            subset(i+1)

            return
        
        subset(0)

        return total
        
        
        