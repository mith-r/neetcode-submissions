class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        split = 0

        while left < right:

            curr = left + (right-left)//2

            if nums[curr+1] < nums[curr]:
                split = curr + 1
                break
            
            if nums[curr] > nums[right]:
                left = curr + 1
            
            if nums[curr] < nums[right]:
                right = curr

        left = 0
        right = split

        while left < right:

            curr = left + (right-left)//2

            if nums[curr] == target:
                return curr

            if nums[curr] > target:
                right = curr

            if nums[curr] < target:
                left = curr + 1

        left = split
        right = len(nums)

        while left < right:
            curr = left + (right-left)//2

            if nums[curr] == target:
                return curr

            if nums[curr] > target:
                right = curr

            if nums[curr] < target:
                left = curr + 1


        return -1         