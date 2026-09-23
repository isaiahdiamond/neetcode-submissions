class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dif = 0
        max_dif = 0
        for first in range(len(prices)):
            day_1 = prices[first]
            for second in range(first+ 1,len(prices)):
                day_2 = prices[second]
                dif = day_2 - day_1
                if dif > max_dif:
                    max_dif = dif

        return max_dif




