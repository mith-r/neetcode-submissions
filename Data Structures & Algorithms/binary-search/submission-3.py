class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        middle = size // 2
        
        print(nums)
        print(size)
        print(middle)
        print()

        if nums[middle] == target:
            return middle
        elif size == 1:
            return -1
        elif target > nums[middle]:
            if self.search(nums[middle:], target) != -1:
                return self.search(nums[middle:], target) + middle
            else:
                return -1
        elif target < nums[middle]:
            return self.search(nums[:middle], target)

        print(size)
        print(middle)


        