class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for number in range(nums.count(val)):
            nums.remove(val)

        return len(nums)


        