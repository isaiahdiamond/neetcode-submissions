
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        start = 1
        for num in nums:
            before.append(start)
            start *= num

        after = []
        end = 1
        for num in reversed(nums):
            after.append(end)
            end *= num

        after.reverse()
        output = []
        for i in range(len(nums)):
            output_num = after[i] * before[i]
            output.append(output_num)
        
        return output 