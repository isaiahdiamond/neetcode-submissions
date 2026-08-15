class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums) - 1):
            for i in range(num + 1, len(nums)):
                if (nums[num] + nums[i]) == target:
                    return [num,i]
