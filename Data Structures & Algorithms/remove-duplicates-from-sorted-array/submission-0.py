class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = set()

        for i in range(len(nums)-1,-1,-1):
            if nums[i] in seen:
                del nums[i]
            else:
                seen.add(nums[i])
        
        return len(nums)
        