class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        consect = 0
        longest = 0
        for i in nums:
            if i == 1: 
                consect += 1
                if consect > longest:
                    longest = consect 
            else:
                consect = 0
        
        return longest