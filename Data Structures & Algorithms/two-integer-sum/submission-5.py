class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        answer = []
        for i in range(len(nums)):
            if nums[i] in differences:
                answer.append(differences[nums[i]])
                answer.append(i)
                return  answer
            differences[target - nums[i]] = i

